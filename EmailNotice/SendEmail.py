# -*- coding: utf-8 -*-
__author__ = 'Peng.Zhao'

import os
import smtplib
import configparser
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from EmailNotice import HtmlTemplate


def read_config(conf_path):
    file_path_name = conf_path
    parse = configparser.ConfigParser()
    parse.read(file_path_name)
    return parse


def send_email(parse_info):
    host = parse_info.get('smtp_host_info', 'host')
    port = parse_info.getint('smtp_host_info', 'port')

    username = parse_info.get('sender_info', 'username')
    password = parse_info.get('sender_info', 'password')

    sender = parse_info.get('email_info', 'sender')
    receiver = parse_info.get('email_info', 'receiver')
    subject = parse_info.get('email_info', 'subject')

    # 定义邮件框架
    msg = MIMEMultipart()

    # 添加邮件正文(HTML)
    mst_text = MIMEText(HtmlTemplate.html_template, 'html', 'utf-8')
    msg.attach(mst_text)

    # 读取报告图片
    image_name = select_report('D:/CI_Program/Python_Program/HighPin_VIK/ReportAndLog/ScreenCapture/')
    fp_image = open('D:/CI_Program/Python_Program/HighPin_VIK/ReportAndLog/ScreenCapture/' + image_name, 'rb')
    msg_image = MIMEImage(fp_image.read())
    fp_image.close()

    # 添加邮件正文图片
    msg_image.add_header('Content-ID', '<image1>')
    msg.attach(msg_image)

    # 添加邮件附件(HTML报告)
    html_name = select_report('D:/CI_Program/Python_Program/HighPin_VIK/ReportAndLog/Report/')
    fp_report = open('D:/CI_Program/Python_Program/HighPin_VIK/ReportAndLog/Report/' + html_name, 'rb')
    msg_html = MIMEText(fp_report.read(), 'base64', 'utf-8')
    msg_html['Content-Type'] = 'application/octet-stream'
    msg_html['Content-Disposition'] = 'attachment; filename=' + html_name
    msg.attach(msg_html)

    # 添加邮件标题
    msg['Subject'] = Header(subject, 'utf-8')
    msg['from'] = sender
    msg['to'] = receiver
    # 给多个人发送需要使用列表
    receiver_list = receiver.split(',')

    # 发送邮件(SSL)
    # smtp = smtplib.SMTP_SSL(host=host, port=port)
    # smtp.login(username, password)
    # smtp.sendmail(sender, receiver_list, msg.as_string())
    # smtp.quit()

    # 发送邮件
    smtp = smtplib.SMTP(host=host, port=port)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver_list, msg.as_string())
    smtp.quit()


def select_report(file_path):
    # 选择文件夹中最新的一份儿文件
    report_list = os.listdir(file_path)
    report_list = sorted(report_list)
    return report_list[-1]


def send_report(configure_path):
    p_info = read_config(configure_path)
    send_email(p_info)

