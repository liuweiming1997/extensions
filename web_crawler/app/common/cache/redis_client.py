import redis

from common.config.config_base import Config_Base
from common.singleton.metaclass_base import Singleton

redis_client = redis.StrictRedis(
    host=Config_Base.REDIS_HOST,
    port=Config_Base.REDIS_PORT,
    decode_responses=True
)

def get_client():
    return redis_client

class RedisClient(metaclass=Singleton):

    def get(self, key):
        return get_client().get(key)

    def set(self, key, value):
        return get_client().set(key, value)

    def delete(self, key):
        return get_client().delete(key)
