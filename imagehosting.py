#!/usr/bin/env python
# coding=utf-8
import oss2
import time
import uuid
import os
import sys
import time
import pyperclip

BUCKET_NAME = "szt-imagehosting"
ENDPOINT = 'http://oss-cn-beijing.aliyuncs.com'
ACCESS_KEY_ID = "LTAI4FjsKkphtSPY4XaBg1WK"
ACCESS_KEY_SECRET = 'VwatIyufaE8xYSveFupmLEiOgxEQv9'

URL = ['']

def Upload_File(File):
    auth = oss2.Auth(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
    bucket = oss2.Bucket(auth, ENDPOINT, BUCKET_NAME)
    Time = time.strftime("%Y-%m-%d_%H:%M")
    Uuid = uuid.uuid4()
    Path = Time + '/' + str(Uuid) + '.png'
    with open(File, 'rb') as fileobj:
        fileobj.seek(0, os.SEEK_SET)
        #current = fileobj.tell()
        bucket.put_object(Path, fileobj)
    get_str = "![](http://%s.%s/%s)" % (BUCKET_NAME, ENDPOINT, Path)
    URL[0] = URL[0] + get_str + " "

def Is_Img(str):
    if str in ['.jpg', '.png', 'jpeg', '.gif']:
        return True
    else:
        return False

if len(sys.argv) == 1:
    tmp = pyperclip.paste()
    print(tmp)
    if Is_Img(tmp[-4:len(tmp)]):
        Upload_File(tmp)
        pyperclip.copy(URL[0])
    else:
        print("参数不是图片")
else :
    for i in range(1, len(sys.argv)):
        LocFile = sys.argv[i]
        if os.path.exists(LocFile):
            if Is_Img(os.path.splitext(LocFile)[1]):
                Upload_File(LocFile)
            else:
                print("参数不是图片")
                exit
        else:
            print("文件不存在")
            exit
    pyperclip.copy(URL[0])
