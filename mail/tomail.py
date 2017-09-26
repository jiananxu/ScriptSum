#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/9/7 17:00
# @Author  : xujn
# @Version : 1.0
import smtplib
from email.mime.text import MIMEText
msg = MIMEText('hello', 'plain', 'utf-8')
msg['From']="214234342423@163.com"
msg['To']='1170182824@qq.com'
msg['Subject']='subject'
# 输入Email地址和口令:
from_addr = "15696334323@163.com"
password = "a123456"
# 输入SMTP服务器地址:
smtp_server = "smtp.163.com"
# 输入收件人地址:
to_addr = "1170182824@qq.com"

import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()