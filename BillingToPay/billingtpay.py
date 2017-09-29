#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/9/25 16:29
# @Author  : xujn
# @Version : 1.0

import pymysql
import requests   # pip3 install requests

billing_code = 'I124401-201709-0000037'

read = open('billing_code.txt', 'r')
code_list = list(map(lambda s: s.strip(), read.readlines()))
print(code_list)

# connection_billing = pymysql.connect(host='10.249.5.77',
#                                      port=8073,
#                                      user='test',
#                                      password='test',
#                                      db='SMP_BL_ADB',
#                                      charset='utf8mb4',
#                                      cursorclass=pymysql.cursors.DictCursor,
#                                      autocommit=True)
# connection_pay = pymysql.connect(host='10.249.5.77',
#                                  port=8074,
#                                  user='test',
#                                  password='test',
#                                  db='SMP_PM_ADB',
#                                  charset='utf8mb4',
#                                  cursorclass=pymysql.cursors.DictCursor,
#                                  autocommit=True)
# sql = "UPDATE `t_sac_billing_info` SET BILLING_STATUS_ENUM_ID='5000117' WHERE BILLING_CODE='{}';".format(billing_code)
# sql_p = "SELECT * FROM `t_sac_payment_b_grp_sum_info` WHERE BILLING_CODE='{}';".format(billing_code)
#
# data = {}
# try:
#     with connection_billing.cursor() as cursor:
#         cursor.execute(sql)
# except:
#     print("mysql connection error")
#     import traceback
#
#     print(traceback.print_exc())
# finally:
#     cursor.close()
#     connection_billing.close()
#
# #
# # try:
# #     s = urllib2.urlopen("http://10.249.5.74:8080/smp-web/invcDataTimedTask/invcBillingGroupSummaryTimedTask").read()
# #     # print s
# # except urllib2.HTTPError:
# #    print('open url error')
# resq = requests.get('http://10.249.5.74:8080/smp-web/invcDataTimedTask/invcBillingGroupSummaryTimedTask')
# # print(resq)
#
#
#
# try:
#     with connection_pay.cursor() as cursor_p:
#         cursor_p.execute(sql_p)
#         data = cursor_p.fetchone()
# except:
#     import traceback
#
#     print(traceback.print_exc())
# finally:
#     connection_pay.close()
#
# print(data)
