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


# def send_email(parse_info):
#     """
#     :description: 编辑邮件正文,并且发送邮件
#     :param parse_info: 邮箱配置信息
#     :return:
#     """
#     host = parse_info.get('smtp_host_info', 'host')
#     port = parse_info.getint('smtp_host_info', 'port')
#
#     username = parse_info.get('sender_info', 'username')
#     password = parse_info.get('sender_info', 'password')
#
#     sender = parse_info.get('email_info', 'sender')
#     receiver = parse_info.get('email_info', 'receiver')
#     subject = parse_info.get('email_info', 'subject')
#
#     # 定义邮件框架
#     msg = MIMEMultipart()
#
#     # 添加邮件正文(HTML)
#     mst_text = MIMEText(HtmlTemplate.html_template, 'html', 'utf-8')
#     msg.attach(mst_text)
#
#     # 读取报告图片
#     image_name = select_report('D:/CI_Program/Python_Program/HighPin_VIK/ReportAndLog/ScreenCapture/')
#     fp_image = open('D:/CI_Program/Python_Program/HighPin_VIK/ReportAndLog/ScreenCapture/' + image_name, 'rb')
#     msg_image = MIMEImage(fp_image.read())
#     fp_image.close()
#
#     # 添加邮件正文图片
#     msg_image.add_header('Content-ID', '<image1>')
#     msg.attach(msg_image)
#
#     # 添加邮件附件(图片附件)
#     image_name = select_report('D:/CI_Program/Python_Program/HighPin_VIK/ReportAndLog/ScreenCapture/')
#     fp_image = open('D:/CI_Program/Python_Program/HighPin_VIK/ReportAndLog/ScreenCapture/' + image_name, 'rb')
#     msg_image_attach = MIMEText(fp_image.read(), 'base64', 'utf-8')
#     msg_image_attach['Content-Type'] = 'application/octet-stream'
#     msg_image_attach['Content-Disposition'] = 'attachment; filename=' + image_name
#     msg.attach(msg_image_attach)
#     fp_image.close()
#
#     # 添加邮件标题
#     msg['Subject'] = Header(subject, 'utf-8')
#     msg['from'] = sender
#     msg['to'] = receiver
#     # 给多个人发送需要使用列表
#     receiver_list = receiver.split(',')
#
#     # 发送邮件(SSL)
#     smtp = smtplib.SMTP_SSL(host=host, port=port)
#     smtp.login(username, password)
#     smtp.sendmail(sender, receiver_list, msg.as_string())
#     smtp.quit()
#
#     # 发送邮件
#     # smtp = smtplib.SMTP(host=host, port=port)
#     # smtp.login(username, password)
#     # smtp.sendmail(sender, receiver_list, msg.as_string())
#     # smtp.quit()

def send_email_html_content(parse_info):
    """
    :description: 编辑邮件正文,并且发送邮件
    :param parse_info: 邮箱配置信息
    :return:
    """
    host = parse_info.get('smtp_host_info', 'host')
    port = parse_info.getint('smtp_host_info', 'port')

    username = parse_info.get('sender_info', 'username')
    password = parse_info.get('sender_info', 'password')

    sender = parse_info.get('email_info', 'sender')
    receiver = parse_info.get('email_info', 'receiver')
    subject = parse_info.get('email_info', 'subject')

    # 定义邮件框架
    msg = MIMEMultipart()

    # 使用内嵌html的格式
    report_name = select_report('D:/CI_Program/Python_Program/HighPin_VIK/ReportAndLog/Report/')
    report_handler = open('D:/CI_Program/Python_Program/HighPin_VIK/ReportAndLog/Report/' + report_name, mode='r', encoding='UTF-8')
    report_html_content = report_handler.read()
    # 修改邮件正文的字体大小
    report_html_content = report_html_content.replace('font-size: 80%', 'font-size: 100%')

    # 添加邮件正文(HTML)
    mst_text = MIMEText(report_html_content, _subtype='html', _charset='UTF-8')
    msg.attach(mst_text)

    # 添加邮件附件
    report_attach_name = select_report('D:/CI_Program/Python_Program/HighPin_VIK/ReportAndLog/Report/')
    report_attach = open('D:/CI_Program/Python_Program/HighPin_VIK/ReportAndLog/Report/' + report_attach_name, 'rb')
    mst_attach = MIMEText(report_attach.read(), 'base64', _charset='UTF-8')
    mst_attach['Content-Type'] = 'application/octet-stream'
    mst_attach['Content-Disposition'] = 'attachment; filename=' + report_attach_name
    msg.attach(mst_attach)

    # 添加邮件标题
    msg['Subject'] = Header(subject, 'utf-8')
    msg['from'] = sender
    msg['to'] = receiver
    # 给多个人发送需要使用列表
    receiver_list = receiver.split(',')

    # 发送邮件(SSL)
    smtp = smtplib.SMTP_SSL(host=host, port=port)
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
    # send_email(p_info)
    send_email_html_content(p_info)
