#!/usr/bin/env python
# coding=utf-8
import mail_helper as mh
import poplib
import email

class MailServer(object):
    def __init__(self):
        self.server = poplib.POP3_SSL('pop.163.com')
        userinfo = mh.Configer()
        self.server.user(userinfo['username'])
        self.server.pass_(userinfo['password'])
        self.config = userinfo
        print(self.server.getwelcome())
        
    def print_stat(self):
        stats = self.server.stat()
        print(stats)
        return stats

    def get_all_mail(self):
        stats = self.print_stat()
        for x in range((self.config['checkpoint']) + 1, stats[0] + 1):
            num = 0
            num += 1
            try:
                resp, byte_lines, octets = self.server.retr(x)
            except:
                pass
            else:
                self.config['checkpoint'] = x
                self.config.save()
                msg = email.message_from_string(b'\r\n'.join(byte_lines).decode('utf-8', 'ignore'))
                header = mh.get_email_headers(msg)
                attachments = mh.get_email_content(msg, header, "./data")
                try:
                    print(f"{num} -> {header['Subject']}")
                    #print(header['From'])
                    #print(header['To'])
                except:
                    print("Error Happens")

    def test(self):
        resp, byte_lines, octets = self.server.retr(1)
        print("-----------------")
        print(resp)
        print("-----------------")
        print(byte_lines)
        print("-----------------")
        print(octets)
        msg = email.message_from_string(b'\n'.join(byte_lines).decode('utf-8'))
        header = mh.get_email_headers(msg)
        print(header['Subject'])
        print(header['From'])
        print(header['To'])
        #print(msg)

if __name__ == "__main__":
    server = MailServer()
    server.print_stat()
    server.get_all_mail()
