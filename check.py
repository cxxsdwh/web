import random
import time


user_agents = [
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
               'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/601.7.8',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/601.1.56 (KHTML, like Gecko) Version/9.0 Safari/601.1.56'
               ]

def get_user_agent():
    i = random.randint(0, 9)
    return user_agents[i]

import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头
def sendmail(subj='changed',text='send by python'):
    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = 'cfafintech@126.com'
    password = '123456fin'
    # 收信方邮箱
    to_addr = '70464465@163.com'
    # 发信服务器
    smtp_server = 'smtp.126.com'
    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText('send by python','plain','utf-8')
    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header(subj)
    # 开启发信服务，这里使用的是加密传输
    server = smtplib.SMTP_SSL()
    server.connect(smtp_server,465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()


import requests
import hashlib

md5 = hashlib.md5()

headers = {'user-agent': get_user_agent()}
r = requests.get('http://13.70.2.133:10001', headers=headers)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'lxml')

body=soup.find(attrs={'class':'text-center p-3'})
md5.update(body.encode('utf8'))
curr=md5.hexdigest()
with open('./data.txt','r') as data:
    prev=data.read()
print(time.strftime('%a, %d %b %Y %H:%M:%S GMT+8',time.localtime(time.time())))
if prev != curr:
    with open('./data.txt','w') as data:
        prev=data.write(curr)
    print("changed")
    sendmail(subj='changed',text='http://13.70.2.133:10001')
else :
    print("unchanged")
data.close()

