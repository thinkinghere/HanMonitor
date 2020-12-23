# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import CommandHandler

if __name__ == "__main__":
    client = CommandHandler(sys.argv)
