# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from monitor import models
from django.core.exceptions import ObjectDoesNotExist
from utils.tools import log


class ClientHandler(object):
    """
    获取客户端配置信息
    """
    def __init__(self, client_id):
        self.client_id = client_id
        self.client_configs = {
            "services": {}
        }

    def fetch_configs(self):
        try:
            host_obj = models.Host.objects.get(id=self.client_id)  # get是获取一个对象
            template_list = list(host_obj.templates.select_related())  # 查询全部的host的templates

            for host_group in host_obj.host_groups.select_related():  # 遍历主机组
                # 这里是获取每个主机全部的templates + 主机的主机组中的全部的templates 后面有重复的直接去重即可
                template_list.extend(host_group.templates.select_related())
            for template in template_list:
                for service in template.services.select_related():  # loop each service
                    # 生成客户端的配置文件
                    # 每个服务有对应的插件的名字 时间间隔
                    # 返回的json格式
                    """
                    {
                        'services': {
                            'service.name': ['plugin_name', interval]
                        }
                    }
                    """
                    # 这里如果用重复的会进行去重
                    self.client_configs['services'][service.name] = [service.plugin_name, service.interval]
            return self.client_configs
        except ObjectDoesNotExist as e:  # 捕获查询不到的时候 使用objects.get会出现查询不到的情况
            log("ClientHandler/fetch_configs err", e)
