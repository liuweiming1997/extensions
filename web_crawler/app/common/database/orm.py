from collections import Iterable

from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker, scoped_session

from common.config.config_base import Config_Base

class Database:

    _instance = None
    _engine = None

    @classmethod
    def init(cls):
        if cls._instance:
            return
        cls._instance = cls()

    def __init__(self):
        self._engine = create_engine(
            "mysql+mysqldb://{user}:{password}@{host}:{port}/{database}?charset=utf8".format(
                user=Config_Base.MYSQL_ROOT_USER,
                password=Config_Base.MYSQL_ROOT_PASSWORD,
                host=Config_Base.DB_HOST,
                database=Config_Base.MYSQL_DATABASE
            ),
            echo=False, 
            pool_size=2, 
            max_overflow=0,
            pool_recycle=3600,
            encoding="utf-8",
        )
        self._session_factory = scoped_session(sessionmaker(self._engine))

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls.init()
        return cls._instance

    @classmethod
    def get_session(cls):
        return cls.get_instance()._session_factory()

    @classmethod
    def get_one_by(cls, model_type, *filters):
        return cls.get_session().query(model_type).filter(*filters).first()

    @classmethod
    def get_many_by(cls, model_type, *filters, order_by=None, offset=None, limit=None):
        query = cls.get_session().query(model_type).filter(*filters)
        if order_by:
            query = query.order_by(desc(order_by))
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)
        return query.all()

    @classmethod
    def add(cls, obj):
        if isinstance(obj, Iterable):
            cls.get_session().add_all(obj)
        else:
            cls.get_session().add(obj)

    @classmethod
    def delete_one_by(cls, model_type, *filters):
        session = cls.get_session()
        try:
            session.query(model_type).filter(*filters).delete()
            session.commit()
        except Exception as e:
            session.rollback()

    @classmethod
    def commit(cls):
        cls.get_session().commit()

    @classmethod
    def flush(cls):
        cls.get_session().flush()

    @classmethod
    def rollback(cls):
        cls.get_session().rollback()
