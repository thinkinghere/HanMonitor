# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
HostID 是在服务端配置好的
"""
configs = {
    'HostID': 1,
    "Server": "127.0.0.1",
    "ServerPort": 8000,
    "urls": {
        'get_configs': ['api/client/config', 'get'],  # acquire all the services will be monitored
        'service_report': ['api/client/service/report/', 'post'],  # report data to monitor

    },
    'RequestTimeout': 30,
    'ConfigUpdateInterval': 300,  # 5 mins as default 5mins 更新一次配置
}
