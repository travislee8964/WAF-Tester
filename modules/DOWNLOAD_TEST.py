#! /usr/bin/env python
# coding:utf-8
from lib.request_util import *
import variable
import time

def check_download_usecase(info,domain,method,i):
    print("-" * 16)
#    print i,":",info
    info = "/"+info
    res = check_usecase(info,method,None,None,domain)

    if res == 403:
        print i,":",res,"   usecase:",info
    else:
        print '\033[1;31;40m', i,":",res,"   usecase:",info, '\033[0m'

def DOWNLOAD_TEST(domain,method,usecase):
    download_file = open(usecase)
    file_content_lines = download_file.readlines()
    download_file.close()
    i = 0
    for line in file_content_lines:
        info = line.strip()
        i+=1
        if info != "":
            check_download_usecase(info,domain,method,i)
            time.sleep(variable.TIMESLEEP)
