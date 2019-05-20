# sendQQMail
a python script for send email by QQ Mail.

主要包含两部分：
1. 使用python发送邮件，使用`smtplib`和`email`,后续可能补充邮件发送模式。参考资料：
    - [简单三步，用 Python 发邮件](https://zhuanlan.zhihu.com/p/24180606)

2. 使用`apscheduler`模块做定时任务管理，下面是参考资料：
    - [Python - 定时调度 - apscheduler](https://blog.csdn.net/qq_33961117/article/details/88990040)
    - [Python 定时任务的实现方式](https://lz5z.com/Python%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E7%9A%84%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%BC%8F/)



> 如想要稳定运行，可以使用相关的进程管理工具，或者自己写shell脚本，监控运行。这里使用node生态的PM2进行管理，比较方便。


```shell
pm2 start crontab.py

# 关闭
pm2 stop crontab
pm2 delete crontab

# 直接杀掉所有
pm2 kill
```
