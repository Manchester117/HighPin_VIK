# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import os
import importlib


def load_test_case():
    """
    :description: 动态载入测试用例
    :return: 返回测试用例对象
    """
    # 定义测试用例列表
    test_list = []

    # 获取当前TestCase的路径
    test_case_path = os.path.abspath('../TestCase/')

    # 获取当前TestCase中的文件列表
    test_case_file_list = os.listdir(test_case_path)

    # 如果TestCase中有测试用例,则将测试用例名加入到列表当中
    if len(test_case_file_list) > 0:
        for test_name in test_case_file_list:
            # 测试用例的开头字母必须为TestCase_
            if test_name.startswith('TestCase_'):
                # 去掉.py后缀
                test_list.append(test_name[:-3])

    # 返回测试用例引用列表
    test_module_list = []
    for test_item in test_list:
        # 引入测试用例
        test_module = importlib.import_module('TestCase.' + test_item)
        # test_module = importlib.import_module('HighPin_VIK.TestCase.' + test_item)
        test_module_list.append(test_module)
    # print(test_module_list)
    return test_module_list
