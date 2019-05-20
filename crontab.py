#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
from send_qq_mail import PersonMail
from datetime import datetime
from string import Template


def compute_birth_days(birth_day='-03-21'):
    now = datetime.now()
    birth = datetime.strptime(str(now.year) + birth_day, '%Y-%m-%d')
    if birth < now:
        birth = datetime.strptime(str(now.year + 1) + birth_day, '%Y-%m-%d')

    return (birth - now).days


def compute_together_days(start_time="2019-04-28"):
    start = datetime.strptime(start_time, '%Y-%m-%d')
    now = datetime.now()
    return (now - start).days


# 发送邮件
def send_email():
    receivers = ["1111111@qq.com", "2222222@qq.com"]
    subject = "subject"
    templ = Template("今天是我们在一起的第$together_days天，\
    距离你的生日还有$birth_days天, 这里可以来一些网上爬取的故事、古诗巴拉巴拉")
    content = templ.substitute(together_days=compute_together_days(), birth_days=compute_birth_days())

    pengpeng_email = PersonMail(receivers)
    pengpeng_email.write_msg(subject, content)
    result = pengpeng_email.send_email()
    print("Ok send" if result == 1 else "Fail send")


# 指定定时任务
def exec_scheduler():
    # BlockingScheduler
    sched = BlockingScheduler()
    sched.add_job(send_email, 'cron', minute=30)  # 每分钟发一次
    # sched.add_job(send_email, 'cron', hour=8)  # 每天早上8点发一次
    sched.start()


if __name__ == '__main__':
    exec_scheduler()
