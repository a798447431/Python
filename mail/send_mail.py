#!/usr/bin/env python
# coding=utf-8
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def get_info():
    with open("./user.json", "r") as info:
        return json.loads(info.read())

server = smtplib.SMTP('smtp.163.com')
userinfo = get_info()

server.login(userinfo['username'], userinfo['password'])
message = "明天下午见一面如何?"
content = MIMEText(message, _subtype='plain')
file = MIMEApplication(open("a.doc", "rb").read())
file.add_header('content-disposition', 'attachment', filename = 'a.doc')
msg = MIMEMultipart()
msg.attach(content)
msg.attach(file)
msg['Subject'] = "第一份邮件"
server.sendmail(userinfo['username'], userinfo['username'], msg.as_string())
server.close()
