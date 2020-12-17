# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from monitor import views

"""
    'client/config/<id>': 客户端根据id获取配置信息
    'client/service/report/': 客户端获取到的信息上报到服务端 
"""
urlpatterns = [
    url(r'client/config/(\d+)/$', views.client_config),
    url(r'client/service/report/$', views.service_report),
]
