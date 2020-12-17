# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
HostID 是在服务端配置好的
"""
configs = {
    'HostID': 3,
    "Server": "127.0.0.1",
    "ServerPort": 8000,
    "urls": {
        'get_configs': ['api/client/config', 'get'],  # acquire all the services will be monitored
        'service_report': ['api/client/service/report/', 'post'],

    },
    'RequestTimeout': 30,
    'ConfigUpdateInterval': 300,  # 5 mins as default
}
