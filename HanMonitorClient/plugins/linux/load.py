#!/usr/bin/env python
# coding:utf-8

import commands
import sys


def monitor():
    shell_command = 'uptime'

    status, result = commands.getstatusoutput(shell_command)
    if status != 0:  # cmd exec error
        value_dic = {'status': status}
    else:
        # value_dic = {}
        # uptime = result.split(',')[:1][0]
        # print(result)
        load1, load5, load15 = '', '', ''
        if sys.platform == 'darwin':
            load1, load5, load15 = result.split('load averages:')[1].split()  # mac上用空格分隔
        elif 'linux' in sys.platform:
            load1, load5, load15 = result.split('load average: ')[1].split(',')  # Linux上用,分隔,名称是load average: 后面还有个空格
        value_dic = {
            # 'uptime': uptime,
            'load1': load1,
            'load5': load5,
            'load15': load15,
            'status': status
        }
    return value_dic


print(monitor())

if __name__ == '__main__':
    test_res = (0, ' 10:15:03 up 5 days,  5:24,  3 users,  load average: 0.00, 0.01, 0.05')
    uptime = test_res[1].split('load average:')[1].split(',')
    print 'uptime result is', uptime
