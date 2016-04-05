# -*- coding: utf-8 -*-
__author__ = 'Peng.Zhao'

import requests
import time


def test_get_fun(test_case):
    """
    :description: 发起GET请求
    :param test_case: 传入的测试用例数据_字典
    :return: 请求返回正文
    """
    resp = requests.get(
        url=test_case['url'],
        params=test_case['getParams'],
        data=test_case['postParams'],
        json=test_case['json'],
        headers=test_case['headers'],
        cookies=test_case['cookies'],
        timeout=60
    )
    requests.session().close()
    # time.sleep(1)
    return resp


def test_post_fun(test_case):
    """
    :description: 发起POST请求
    :param test_case: 传入的测试用例数据_字典
    :return: 请求返回正文
    """
    resp = requests.post(
        url=test_case['url'],
        params=test_case['getParams'],
        data=test_case['postParams'],
        json=test_case['json'],
        headers=test_case['headers'],
        cookies=test_case['cookies'],
        timeout=60
    )
    requests.session().close()
    # time.sleep(1)
    return resp
