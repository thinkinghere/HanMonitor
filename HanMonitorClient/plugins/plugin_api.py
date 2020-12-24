# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from linux import sysinfo, load, cpu_mac, cpu, memory, network, host_alive

"""
    插件名字和调用函数的对应关系
    反射
"""


def LinuxCpuPlugin():
    return cpu.monitor()


def host_alive_check():
    # 查看主机是否存活
    return host_alive.monitor()


def GetMacCPU():
    # return cpu.monitor()
    return cpu_mac.monitor()


def LinuxNetworkPlugin():
    return network.monitor()


def LinuxMemoryPlugin():
    return memory.monitor()


def LinuxLoadPlugin():
    return load.monitor()


if __name__ == '__main__':
    print LinuxCpuPlugin()
    print host_alive_check()
