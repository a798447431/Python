#!/usr/bin/env python
# coding=utf-8
from test_login1 import CodeSpider

if __name__ == "__main__":
    list = ['https://www.jisuanke.com/course/792', 'https://www.jisuanke.com/course/786']
    for i in list:
        tmp = CodeSpider(i)
        tmp.get_url()
        tmp.get_code()
        del(tmp)

