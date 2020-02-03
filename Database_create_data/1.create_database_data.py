#!/usr/bin/env python
# coding=utf-8

import pymysql
import random

def insertData():
    coon = pymysql.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    passwd = "szt3536132",
    db = "info",
    charset = "utf8")
    
    cur = coon.cursor()
    for i in range(1, 5000):
        user_name = random.choice(['Lucy','Tom','Lily','Amy','Dave','Aaron','Baron']) + str(i)
        user_account = user_name
        pwd = '1' + str(random.choice([3, 5, 7, 8])) + str(random.random())[2:11]
        system_role = random.choice(['教练员', '受训者', '系统管理员']) 
        user_sex = random.choice(['男','女'])
        organization = random.choice(['哈船科技', 'XXXX']) + str(i)
        organization_code = '1' + str(random.choice([3, 5, 7, 8])) + str(random.random())[2:11] 
        duty = random.choice(['教练员', '受训者', '系统管理员']) + str(i)
        duty_code = '1' + str(random.choice([3, 5, 7, 8])) + str(random.random())[2:11] 
        info_sql = "insert into info.userinfo(account_num, passwd, system_role, username, usersex, organization, organization_code, duty, duty_code)values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(user_account, pwd, system_role, user_name, user_sex, organization, organization_code, duty, duty_code)
        cur.execute(info_sql)
        coon.commit()
    cur.close()
    coon.commit()
    coon.close()

if __name__ == '__main__':
    insertData()
    print("数据插入结束!")
