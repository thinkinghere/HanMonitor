# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time


def log(*args, **kwargs):
    format_str = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format_str, value)
    kwargs = kwargs if kwargs else ''
    args = args if args else ''
    print "{} {} {}".format(dt, args, kwargs)


if __name__ == '__main__':
    log(12312)
