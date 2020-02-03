#!/usr/bin/env python
# coding=utf-8

import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header

class SendMessage:
    def __init__(self):
        return
    def send(self, to_msg, to_add):
        mail_host =  "smtp.163.com"
        mail_user = "szt3536132@163.com"
        mail_pass = "szt3536132"
        sender = 'szt3536132@163.com'
        receivers = [to_add]
        content = to_msg
        message = MIMEMultipart('related')
        message['From'] = "szt3536132@163.com"
        message['To'] = to_add
        subject = 'PDF附件测试！！！！'
        message['Subject'] = Header(subject, 'utf-8')
        att1 = MIMEText(open('./test.pdf', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="test.pdf"'
        message.attach(att1)
        
        msgAlternative = MIMEMultipart('alternative')
        message.attach(msgAlternative)
        
        msgAlternative.attach(MIMEText(content, 'html', 'utf-8'))

        fp = open('./test.jpg', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        
        msgImage.add_header('Content-ID', '<image1>')
        message.attach(msgImage)

        try:
            smtp0bj = smtplib.SMTP()
            smtp0bj.connect(mail_host, 25)
            smtp0bj.login(mail_user, mail_pass)
            smtp0bj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件" + e.strerror)

def main():
    sender = SendMessage()
    mail_msg = """
    <p>html发送测试</p>
    <p><a href="https://www.haizeix.com/">海贼科技</a></p>
    <p><img src="cid:image1"></p>
    """
    sender.send(mail_msg, 'szt3536132@163.com')

if __name__ == '__main__':
    main()
