#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 设置SMTP服务器以及登录信息
SERVER = {
    'host': "smtp.qq.com",
    'port': 465
}

USER = {
    "email": "1129103770@qq.com",  # 邮箱登录账号
    "password": "okdftbfmihrxiajc"  # 发送人邮箱的授权码
}


class PersonMail(object):
    def __init__(self, receivers, sender=USER["email"]):
        self.From = sender
        self.To = receivers
        self.msg = ''

    def write_msg(self, subject, content):
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        self.msg = MIMEText(content, 'plain', 'utf-8')
        self.msg['From'] = Header(self.From)
        self.msg['To'] = Header(str(";".join(self.To)))
        self.msg['Subject'] = Header(subject)

    def send_email(self):
        try:
            smtp_client = smtplib.SMTP_SSL(SERVER["host"], SERVER["port"])
            smtp_client.login(USER["email"], USER["password"])
            smtp_client.sendmail(self.From, self.To, self.msg.as_string())
            smtp_client.quit()
            return 1
        except smtplib.SMTPException as e:
            print("error", e)
            return 0


if __name__ == '__main__':
    def test():
        receivers = ["1129103770@qq.com"]
        # receivers = ["981827572@qq.com", "1129103770@qq.com"]

        pengpeng_email = PersonMail(receivers)
        pengpeng_email.write_msg("来自鹏鹏的邮件", "我们已经在一起22天了，小兴奋")
        result = pengpeng_email.send_email()
        print(result)

    test()
