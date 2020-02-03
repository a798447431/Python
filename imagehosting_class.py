#!/usr/bin/env python
# coding=utf-8

import oss2
import time
import uuid
import os
import sys
import time
import pyperclip


class Upload:
    BUCKET_NAME = "szt-imagehosting"
    ENDPOINT = 'http://oss-cn-beijing.aliyuncs.com'
    __ACCESS_KEY_ID = "LTAI4FjsKkphtSPY4XaBg1WK"
    __ACCESS_KEY_SECRET = 'VwatIyufaE8xYSveFupmLEiOgxEQv9'
    
    def __init__(self, BUCKET_NAME, ENDPOINT, ACCESS_KEY_ID, ACCESS_KEY_SECRET):
        self.BUCKET_NAME = BUCKET_NAME
        self.ENDPOINT = ENDPOINT
        self.ACCESS_KEY_ID = ACCESS_KEY_ID
        self.ACCESS_KEY_SECRET = ACCESS_KEY_SECRET
        self.auth = oss2.Auth(self.ACCESS_KEY_ID, self.ACCESS_KEY_SECRET)
        self.bucket = oss2.Bucket(self.auth, self.ENDPOINT, self.BUCKET_NAME)

    def ossupload(self, remote_name, src_name = "/tmp/haizeitmp.jpg"):
        self.bucket.put_object_from_file(remote_name, src_name)

