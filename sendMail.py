# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 11:41:35 2019

@author: dxm
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendMail(receivers,messg):
    username = 'yourname'
    sender = 'youremail@youremail'   #发件邮箱
    passwd = 'yourpassword'    # 邮箱授权码
    subject = 'something' #主题
# 创建一个带附件的实例
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receivers
#创建正文，将文本文件添加到MIMEMultipart中
    msg.attach(MIMEText(messg,'plain','utf-8'))
#    服务器和端口号
    s = smtplib.SMTP_SSL('server',"{0}".format(PORT))
    s.login(username,passwd)
    s.sendmail(sender,receivers,msg.as_string())
    print(receivers+' Send Succese')
    
if __name__=="__main__":
    sendMail('receiver@email.com','msg balabala')
    
    
