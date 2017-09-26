#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/8/25 10:40
# @Author  : xujn
# @Version : 1.0
import pymysql
connection = pymysql.connect(host='10.249.5.78',
                             port=8073,
                             user='test',
                             password='test',
                             db='SMP_BL_ADB',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# SELECT
# 	BILLING_CODE,
# 	BILLING_PAYMENT_RULE_CODE,
# 	PAYMENT_RULE_CODE,
# 	INVC_HANDLED_PERSON_NAME
# FROM
# 	`t_sac_payment_b_grp_sum_info`
# WHERE
# # 	PAYMENT_RULE_CODE='1'
# 	BILLING_CODE='I125101-201708-0000008';

# SELECT
# 	PAYMENT_INFO_CODE,
# 	BILLING_PAYMENT_RULE_CODE,
# 	PAYMENT_RULE_CODE
# # 	*
# FROM t_sac_payment_info
# WHERE PAYMENT_INFO_CODE='P121001-201708-0000036'

