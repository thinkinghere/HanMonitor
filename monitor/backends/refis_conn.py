# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import redis
from utils.tools import log


def redis_pool_conn(django_settings):
    pool = redis.ConnectionPool(host=django_settings.REDIS_CONN['HOST'],
                                port=django_settings.REDIS_CONN['PORT'],
                                db=django_settings.REDIS_CONN['DB'])
    r = redis.Redis(connection_pool=pool)
    return r


class RedisConnection:
    def __init__(self, django_settings):
        self.django_settings = django_settings
        self.host = self.django_settings.REDIS_CONN['HOST']
        self.port = self.django_settings.REDIS_CONN['PORT']
        self.db = self.django_settings.REDIS_CONN['DB']

    def redis_pool_conn(self):
        """
        redis connection_pool
        :param django_settings:
        :return: conn
        """
        pool = redis.ConnectionPool(host=self.host, port=self.port, db=self.db)
        conn = redis.Redis(connection_pool=pool)
        return conn