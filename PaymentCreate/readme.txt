# @Author  : xujn

需求：根据合同号和项目号修改IS_CAN_PAY字段，使开票单可支付。

符合支付规则,
累计可支付金额小于等于0！

环境：python2.7+pymysql
						pymysql安装(pip install pymysql)

功能：合同号+项目号     ----------->
										查询
	  合同号+无项目号   ----------->

eg: python pmcreate.py CU12-1001-2012-000665  ZGE11BA0D00001.121001
或者python pmcreate.py CU12-1001-2012-000665



