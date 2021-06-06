#!/usr/bin/env python
# coding=utf-8
__author__ = 'yinjia'


import os
import sys

from FTPClient.bin import ftpclient

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

if __name__ == "__main__":
    ftpclient.run()
