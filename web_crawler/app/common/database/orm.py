from collections import Iterable

from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker, scoped_session

from common.config.config_base import Config_Base
from common.lib.logger import log

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
            "mysql+mysqldb://{user}:{password}@{host}/{database}?charset=utf8".format(
                user=Config_Base().MYSQL_ROOT_USER,
                password=Config_Base().MYSQL_ROOT_PASSWORD,
                host=Config_Base().DB_HOST,
                database=Config_Base().MYSQL_DATABASE
            ),
            echo=True, 
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
            order_by = [order_by] if not isinstance(order_by, list) else order_by
            for item in order_by:
                if item[0] == '-':
                    query = query.order_by(desc(item[1:]))
                else:
                    query = query.order_by(item)

        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)
        result = query.all()
        return result

    @classmethod
    def add(cls, obj):
        if isinstance(obj, Iterable):
            cls.get_session().add_all(obj)
        else:
            cls.get_session().add(obj)

    @classmethod
    def delete_one_by(cls, model_type, *filters):
        session = cls.get_session()
        session.query(model_type).filter(*filters).delete()

    @classmethod
    def commit(cls):
        cls.get_session().commit()

    @classmethod
    def flush(cls):
        cls.get_session().flush()

    @classmethod
    def rollback(cls):
        cls.get_session().rollback()

    @classmethod
    def remove_session(cls):
        try:
            cls.get_session().close()
        except Exception as e:
            log.error(str(e))
        finally:
            cls.get_instance()._session_factory.remove()
