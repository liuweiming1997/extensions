import json

from common.cache.redis_client import RedisClient
from common.lib.logger import log


UPCOMING_KEY = 'dianying_of_upcoming'
ONSHOW_KEY = 'diamying_of_onshow'

class DianYingCache:
    @classmethod
    def set_upcoming_dianying(cls, upcoming_dianying_list):
        RedisClient().set(UPCOMING_KEY, json.dumps(upcoming_dianying_list))

    @classmethod
    def set_onshow_dianying(cls, onshow_dianying_list):
        RedisClient().set(ONSHOW_KEY, json.dumps(onshow_dianying_list))

    @classmethod
    def get_upcoming_dianying_list(cls):
        result = []
        try:
            result = json.loads(RedisClient().get(UPCOMING_KEY))
        except TypeError as e:
            log.error(e)
        return result

    @classmethod
    def get_onshow_dianying_list(cls):
        result = []
        try:
            result = json.loads(RedisClient().get(ONSHOW_KEY))
        except TypeError as e:
            log.error(e)
        return result        
