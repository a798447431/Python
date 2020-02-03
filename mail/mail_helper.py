#!/usr/bin/env python
# coding=utf-8

class Configer(dict):
    def __init__(self, filepath = "./user.json"):
        self.filepath = filepath
        import json
        with open(self.filepath, 'r') as info_in:
            dict.__init__(self, json.loads(info_in.read()))
    def save(self):
        import json
        with open(self.filepath, "w") as info_out:
            info_out.write(json.dumps(self, indent = 4))

def decode_str(s):
    from email.header import decode_header
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def get_email_headers(msg):
    headers = {}
    for header in ['From', 'To', 'Cc', 'Subject']:
        value = msg.get(header)
        if value:
            from email.utils import parseaddr
            if header == "From":
                name, addr = parseaddr(value)
                name = decode_str(name)
                fromaddr = u'%s <%s>' % (name, addr)
                headers['From'] = fromaddr
            if header == 'To':
                all_to = value.split(',')
                to = []
                for x in all_to:
                    name, addr = parseaddr(x)
                    name = decode_str(name)
                    to_addr = u'%s <%s>' % (name, addr)
                    to.append(to_addr)
                headers['To'] = to
            if header == 'Subject':
                subject = decode_str(value)
                headers['Subject'] = subject
    return headers

def get_email_content(msg, header, savepath):
    if 'Subject' not in header.keys():
        print("invalid header")
        return None
    attachments = []
    import os
    try:
        savepath = os.path.join(savepath, header['Subject'])
    except:
        return None

    for subpart in msg.walk():
        filename = subpart.get_filename()
        savepath = os.path.join(savepath, header['Subject'])
        
        if filename:  
            if not os.path.exists(savepath):
                try:
                    os.makedirs(savepath)
                except:
                    return None
            filename = decode_str(filename)
            data = subpart.get_payload(decode = True)
            savefilename = os.path.join(savepath, filename)
            attachments = open(savepath, 'wb')
            attachments.write(data)
            attachments.close()
            attachments.append(attachments)
    return attachments

        
