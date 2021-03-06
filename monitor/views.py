# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.conf import settings
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from monitor.backends import data_optimization
from monitor.backends.refis_conn import redis_pool_conn, RedisConnection
from monitor.serializer import ClientHandler
from utils.tools import log

REDIS_OBJ = RedisConnection(settings).redis_pool_conn()


# log(REDIS_OBJ.set("redis set test", 123))


def client_config(request, client_id):
    """
    向服务端提供配置信息
    :param request:
    :param client_id:
    :return:
    """
    config_obj = ClientHandler(client_id)
    config = config_obj.fetch_configs()

    if config:
        return HttpResponse(json.dumps(config))


@csrf_exempt
def service_report(request):
    """
    客户端上报信息
    :param request:
    :return:
    """
    print("client data:", request.POST)
    if request.method == 'POST':
        try:
            """获取host service_name"""
            print('host=%s, service=%s' % (request.POST.get('client_id'), request.POST.get('service_name')))
            data = json.loads(request.POST['data'])
            # print(data)
            # StatusData_1_memory_latest
            client_id = request.POST.get('client_id')
            service_name = request.POST.get('service_name')
            # 把数据存下来
            # 使用data_optimization函数对数据进行优化
            data_saveing_obj = data_optimization.DataStore(client_id, service_name, data, REDIS_OBJ)

            # redis_key_format = "StatusData_%s_%s_latest" %(client_id,service_name)
            # data['report_time'] = time.time()
            # REDIS_OBJ.lpush(redis_key_format,json.dumps(data))

        except IndexError as e:
            print('----->err:', e)
    res_data = "client:{}, host:{} ---report success---".format(request.POST.get('client_id'), request.META.get("REMOTE_ADDR"))
    return HttpResponse(json.dumps(res_data))
