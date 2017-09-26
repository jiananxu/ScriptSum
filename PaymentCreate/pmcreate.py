#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-08 11:34:34
# @Author  : xujn
# @Version : 1

import os
import pymysql
import sys

print "argv:", sys.argv
# Connect to the database

connection = pymysql.connect(host='10.249.5.77',
                             port=8068,
                             user='test',
                             password='test',
                             db='SMP_AG_BBD_ADB',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

con_num = sys.argv[1]

if len(sys.argv) == 2:
    pro_num = ''
else:
    pro_num = sys.argv[2]

cursor = connection.cursor()
cursor2 = connection.cursor()

sql_update = "UPDATE t_sac_basic_con_item SET IS_CAN_PAY=1  WHERE CONTRACT_NUM='%s' AND PROJECT_NUMBER='%s';" % (
    con_num, pro_num)
sql_query = "SELECT * FROM `t_sac_basic_con_item` WHERE CONTRACT_NUM = '%s' AND PROJECT_NUMBER = '%s';" % (
    con_num, pro_num)

# 更新
try:
    cursor.execute(sql_update)
    #  commit update
    connection.commit()
    print "******commit success*****"
except:
    #   回滚
    connection.rollback()
    print "*****update error，rollback******"
cursor.close()

# 查询更新结果
try:
    cursor2.execute(sql_query)
    data = cursor2.fetchall()
    print '******Read    ' + str(len(data)) + "    data(update result)*****"
    print '*CONTRACT_NUM*', '           ', '*PROJECT_NUMBER*', '       ', '*IS_CAN_PAY*'
    for d in data:
        print '{}   {}            {}'.format(d['CONTRACT_NUM'], d['PROJECT_NUMBER'], d['IS_CAN_PAY'])
except:
    print 'read error'

cursor2.close()
connection.close()
