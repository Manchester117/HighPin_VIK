# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import os
import json
import importlib
from openpyxl.reader.excel import load_workbook
from ReadTestCaseExcel import ReadExcelData


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
    else:
        print('没有需要执行的测试用例...')

    # 返回测试用例引用列表
    test_module_list = []
    for test_item in test_list:
        # 引入测试用例
        test_module = importlib.import_module('TestCase.' + test_item)
        # test_module = importlib.import_module('HighPin_VIK.TestCase.' + test_item)
        test_module_list.append(test_module)
    # print(test_module_list)
    return test_module_list


def load_test_case_for_excel():
    """
    :description: 载入测试用例Excel
    :return: 返回所有测试数据结构
    """
    # 定义测试用例列表用于存放Excel的Workbook对象
    excel_work_book_list = []

    # 获取当前TestCase的路径(Excel)
    test_case_path = os.path.abspath('../TestCase/')

    # 获取当前TestCase中的文件列表(Excel)
    test_case_excel_list = os.listdir(test_case_path)

    if len(test_case_excel_list) > 0:
        for test_excel in test_case_excel_list:
            # 如果文件后缀是.xlsx,那么就把这个文件转化为WorkBook对象,并存入列表
            if test_excel.endswith('.xlsx'):
                excel_absolute_path = test_case_path + "\\" + test_excel
                work_book = load_workbook(filename=excel_absolute_path)
                excel_work_book_list.append(work_book)
    else:
        print("没有需要执行的测试用例(Excel)")
    # 返回所有测试数据
    total_test_list = ReadExcelData.get_total_test_data(excel_work_book_list)
    return total_test_list

if __name__ == "__main__":
    load_test_case_for_excel()
    # load_test_case()


