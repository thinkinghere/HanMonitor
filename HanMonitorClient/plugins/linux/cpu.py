#!/usr/bin/env python
# coding:utf-8

# apt-get install sysstat

import commands


def monitor(frist_invoke=1):
    # centos7 install sar: yum install sysstat -y
    """
    # sar 1 3 代表每隔1秒，显示3次，CPU使用的情况
    [root@centos-linux gradle-6.7.1]# sar 1 3
    Linux 3.10.0-1160.6.1.el7.x86_64 (centos-linux.shared) 	2020年12月24日 星期四 	_x86_64_	(2 CPU)

    11時58分52秒 CST     CPU     %user     %nice   %system   %iowait    %steal     %idle
    11時58分53秒 CST     all      0.51      0.00      0.00      0.00      0.00     99.49
    11時58分54秒 CST     all      0.50      0.00      0.50      0.00      0.00     99.00
    11時58分55秒 CST     all      0.00      0.00      0.00      0.00      0.00    100.00
    Average:        all      0.34      0.00      0.17      0.00      0.00     99.50
    :param frist_invoke:
    :return:
    """
    shell_command = 'sar 1 3| grep "^Average:"'
    status, result = commands.getstatusoutput(shell_command)
    if status != 0:
        value_dic = {'status': status}
    else:
        value_dic = {}
        # print('---res:',result)
        # 通过Average: 过滤出数据
        # Average:        all      0.34      0.00      0.17      0.00      0.00     99.50
        #                 all      % user   % nice    % system  % iowait   % steal  % idle
        # split data ['Average:', 'all', '0.33', '0.00', '0.17', '0.00', '0.00', '99.50']
        all, user, nice, system, iowait, steal, idle = result.split()[1:]
        value_dic = {
            'user': user,
            'nice': nice,
            'system': system,
            'idle': idle,
            'status': status
        }
    return value_dic


if __name__ == '__main__':
    print monitor()
