#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-15
# @Author  : xujn
# @Version : 1
# @QQ      : 1170182824
import pymysql
import sys


# # 【命令行参数】
settle_acc_code = ''

if len(sys.argv) == 2:
    settle_acc_code = sys.argv[1]
else:
    print '请正确输入'


# 可以自行定义结算单号，如用此行代码，请注释掉【命令行参数】中代码
# settle_acc_code = 'J122201-201709-000010'

# connection to mysql
connection = pymysql.connect(host='10.249.5.77',
                             port=8073,
                             user='test',
                             password='test',
                             db='SMP_BL_ADB',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
# read data result from mysql

# SIT 数据库
# connection = pymysql.connect(host='10.249.5.78',
#                              port=8073,
#                              user='test',
#                              password='test',
#                              db='SMP_BL_ADB',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)
sql_extract = "SELECT SETTLE_ACC_CODE,ORDER_REC_TRA_ID ,PROCESSED_FLAG FROM `t_sac_billing_confirm_stl_inf` WHERE `SETTLE_ACC_CODE`='%s';" % (
    settle_acc_code)

data_extract = {}
try:
    with connection.cursor() as cursor_extract:
        cursor_extract.execute(sql_extract)
        data_extract = cursor_extract.fetchall()

except Exception:
    print "mysql connection error"
    import traceback
    print traceback.print_exc()


# 提取处理
def billing_msg_extract(data):
    list_flag_0 = [d for d in data if d['PROCESSED_FLAG'] == 0]
    list_flag_1 = [d for d in data if d['PROCESSED_FLAG'] == 1]
    list_flag_2 = [d for d in data if d['PROCESSED_FLAG'] == 2]

    # PROCESSED_FLAG=0
    if len(list_flag_0) != 0:
        for f0 in list_flag_0:
            print '结算单号: %s | 订单接收信息ID: %d  开票信息未提取'.decode('utf-8') % (
            str(f0['SETTLE_ACC_CODE']), f0['ORDER_REC_TRA_ID'])
    else:
        pass

    # PROCESSED_FLAG=2
    if len(list_flag_2) != 0:
        for f2 in list_flag_2:
            print '结算单号: %s | 订单接收信息ID: %d  开票信息提取中'.decode('utf-8') % (
            str(f2['SETTLE_ACC_CODE']), f2['ORDER_REC_TRA_ID'])
    else:
        pass
    # PROCESSED_FLAG=1
    if len(list_flag_1) != 0:
        for f1 in list_flag_1:
            print '结算单号: %s | 订单接收信息ID: %d  开票信息提取成功'.decode('utf-8') % (
            str(f1['SETTLE_ACC_CODE']), f1['ORDER_REC_TRA_ID'])
    else:
        pass
    return list_flag_1


# 拆分预处理
def split_process(data_split_list):
    print "************************************拆分失败*********************************".decode('utf-8')
    for data in [d0 for d0 in data_split_list if d0['IS_SPLIT_FLAG'] is 0]:
        print data['ERR_MSG'],
        print ' | ORDER_REC_TRA_ID: ' + str(data['ORDER_REC_TRA_ID'])
    print "************************************拆分成功*********************************".decode('utf-8')
    for data in [d1 for d1 in data_split_list if d1['IS_SPLIT_FLAG'] is 1]:
        # print "*****************************************************************************"
        print '接收行ID[ORDER_REC_TRA_ID]:       '.decode('utf-8') + str(data['ORDER_REC_TRA_ID'])
        print 'ERR_MSG:                         '.decode('utf-8') + data['ERR_MSG'].decode('utf-8')
        print '结算模式[SETTLE_PATTERN_ENUM_ID]:  '.decode('utf-8') + enum_code(data['SETTLE_PATTERN_ENUM_ID'])
        print '推送组织[OPERATION_ORG_CODE]:     '.decode('utf-8') + settle_code(data['OPERATION_ORG_CODE'])
        print "*****************************************************************************\n"


def enum_code(code):
    code = str(code)
    name_id_dict = {'5000086': '集团一点结算',
                    '5000087': '省分一点结算',
                    '5000088': '集团代付',
                    '5000089': '地市合同省代付',
                    '5000090': '集团合同省分支付'
                    }

    for i in name_id_dict.iterkeys():
        if code.count(i) == 1:
            return name_id_dict[i]
        else:
            pass


def settle_code(code):
    code = str(code)
    name_code_dict = {

        '122201': '吉林省',
        '124401': '广东省',
        '121001': '集团'

    }
    jilin = ["liubb33"]
    guangdong = ["zengqsh1", "lindy8", "chenzh68", "fenghy11", "laizj1", "ligr33", "limy31", "liwd84", "liwf35",
                 "lianghao1", "lincl6", "lindy8", "linjp9", "liuxj220", "lvn3", "shiyu15", "suhy16", "tianp6",
                 "wangwj157", "wujl90", "wuwei6", "yanliming", "yushao1", "yuanm7", "zhangsk25", "zhangsy178",
                 "zhangyuan3", "lix83", "lish226", "lix83", "liys191", "liangjp23", "luolan6"
                 ]
    jituan = ["wangty", "wanghongqin", "zhangyb", "jiaoying", "changna", "mengj9", "tong.li", "wangwj2", "zhaoli2",
              "wangty"]
    # in
    for i in name_code_dict.iterkeys():
        if code.count(i) == 1:
            if code == '122201':
                print '吉林可使用制单人账号: '.decode('utf-8') + str(jilin)
                return name_code_dict[i]
            if code == '124401':
                print '广东可使用制单人账号: '.decode('utf-8') + str(guangdong)
                return name_code_dict[i]
            if code == '121001':
                print '集团可使用制单人账号: '.decode('utf-8') + str(jituan)
                return name_code_dict[i]
            else:
                print '暂不支持其他省份制单人查看'.decode('utf-8')
                return ''


# 拆分处理
def billing_msg_split(list_flag_1):
    order_rec_tra_id_list = [f1['ORDER_REC_TRA_ID'] for f1 in list_flag_1]
    data_split = []
    try:
        with connection.cursor() as cursor_split:
            for order_rec_tra_id in order_rec_tra_id_list:
                # print order_rec_tra_id
                cursor_split.execute(
                    "SELECT "
                    "t_sac_billing_from_info.ORDER_REC_TRA_ID,"
                    "IS_SPLIT_FLAG,"
                    "ERR_MSG ,"
                    "SETTLE_PATTERN_ENUM_ID ,"
                    "OPERATION_ORG_CODE FROM "
                    "t_sac_billing_from_info_s,t_sac_billing_from_info"
                    " WHERE "
                    "t_sac_billing_from_info.ORDER_REC_TRA_ID = '%s' "
                    "AND "
                    "t_sac_billing_from_info_s.BILLING_FROM_INFO_ID = t_sac_billing_from_info.BILLING_FROM_INFO_ID;"
                    % order_rec_tra_id)
                data_split.append(cursor_split.fetchone())
    except:
        print '拆分错误'.decode('utf-8')
    split_process(data_split)
    # return


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")

    # data = [{u'SETTLE_ACC_CODE': u'J124401-201708-000006', u'ORDER_REC_TRA_ID': 10000011665L, u'PROCESSED_FLAG': 0},
    #         {u'SETTLE_ACC_CODE': u'J124401-201708-000006', u'ORDER_REC_TRA_ID': 10000011667L, u'PROCESSED_FLAG': 1},
    #         {u'SETTLE_ACC_CODE': u'J124401-201708-000006', u'ORDER_REC_TRA_ID': 10000013066L, u'PROCESSED_FLAG': 2}]

    # 提取数据
    l_f_1 = billing_msg_extract(data_extract)
    # 拆分数据
    billing_msg_split(l_f_1)
