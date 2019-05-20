# sendQQMail
a python script for send email by QQ Mail.

主要包含两部分：
1. 使用python发送邮件，使用`smtplib`和`email`,后续可能补充邮件发送模式。

2. 使用`apscheduler`模块做定时任务管理



> 如想要稳定运行，可以使用相关的进程管理工具，或者自己写shell脚本，监控运行。这里使用node生态的PM2进行管理，比较方便。


```shell
pm2 start crontab.py

# 关闭
pm2 stop crontab
pm2 delete crontab

# 直接杀掉所有
pm2 kill
```
