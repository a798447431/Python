#!/usr/bin/env python
# coding=utf-8

import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import os

logpath = '/home/szt/Code/Python/test_dir/breaking_point.log'

def get_email_content(mailbox_account, passwd):
    pop3_server = 'pop.163.com'
    server = poplib.POP3(pop3_server)
    server.set_debuglevel(1)
    print(server.getwelcome().decode('utf-8'))

    server.user(mailbox_account)
    server.pass_(passwd)
    
    email_num, email_size = server.stat()
    print("消息数量：{0}，消息总大小：{1}".format(email_num, email_size))

    rsp, msg_list, rsp_siz = server.list()
    print("服务器的响应：{0},\n消息列表：{1},\n返回信息大小：{2}".format(rsp, msg_list, rsp_siz))
    print("邮件总数：{}".format(len(msg_list)))

    total_mail_numbers = len(msg_list)
    print("total_mail_numbers : ", total_mail_numbers) 
    number = read_log()
    
    for i in range(number, total_mail_numbers + 1):
        resp, lines, octets = server.retr(i)
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        msg = Parser().parsestr(msg_content)
        dirname = get_header(msg)
        get_file(msg, dirname)
        get_content(msg)
        writer_log(i + 1)

def decode_str(str):
    value, charset = decode_header(str)[0]
    if charset:
        value = value.decode(charset)
    return value

def get_header(msg):
    for header in ['From', 'To', 'Subject']:
        value = msg.get(header, '')
        if value:
            if header == 'Subject':
                value = decode_str(value)
            elif header in ['From', 'To']:
                hdr, addr = parseaddr(value)
                name = decode_str(addr)
                value = name
        print(header + " : " + value)
    return value

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos+8:].strip()
    return charset

def get_file(msg, dirname):
    for part in msg.walk():
        filename= part.get_filename()
        if filename != None:
            filename = decode_str(filename)
            data = part.get_payload(decode = True)
            tmp_path = '/home/szt/Code/Python/test_dir/' + dirname
            isExists = os.path.exists(tmp_path)
            if not isExists:
                os.makedirs(tmp_path)
            path = tmp_path + '/' + filename
            fp = open(path, "wb")
            fp.write(data)
            fp.close()
            print(filename, 'download')

def get_content(msg):
    for part in msg.walk():
        content_type = part.get_content_type()
        charset = guess_charset(part)
        if part.get_filename() != None:
            continue
        email_content_type = ''
        content = ''
        if content_type == 'text/plain':
            email_content_type = 'text'
        elif content_type == 'text/html':
            email_content_type = 'html'
        if charset:
            try:
                content = part.get_payload(decode=True).decode(charset)
            except AttributeError:
                print('type error')
            except LookupError:
                print("unknown encoding: utf-8")
        if email_content_type == '':
            continue
        print(email_content_type + " ----- " + content)
            
def read_log():
    with open(logpath, 'r') as f:
        number = f.read()
        number = int(number)
        f.close()
    return number

def writer_log(number):
    with open(logpath, 'w') as f:
        f.write(str(number))
        f.close()


if __name__ == '__main__':
    get_email_content('szt3536132@163.com', 'szt3536132')
    
