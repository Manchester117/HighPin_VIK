# -*- coding: utf-8 -*-
__author__ = 'Peng.Zhao'

import os
import json
import datetime
import unittest
import HTMLTestRunner
from EngineModule.CreateTestCaseModule import create_test_case_class
from EngineModule.CreateTestCaseModule import create_test_case_class_for_file
from RunModeModule import LoadTestCase
from WebdriverOperation import ScreenCapture
from EmailNotice import SendEmail

#
#                       _oo0oo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      O\  =  /O
#                    ___/`---'\___
#                  .' \\|     |#  '.
#                 / \\|||  :  |||#  \
#                / _||||| -:- |||||- \
#               |   | \\\  -  #/ |    |
#               | \_|  ''\---/''  |_/ |
#               \  .-\__  '-'  ___/-. /
#             ___'. .'  /--.--\  `. .'___
#          ."" '<  `.___\_<|>_/___.' >'  "".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `_.   \_ __\ /__ _/   .-` /  /
#     =====`-.____`.___ \_____/___.-`___.-'=====
#                       `=---='
#
#
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#               佛祖保佑         永无BUG
#


# if __name__ == '__main__':
#     """
#     :description: 使用Python数据结构运行测试
#     """
#     # 载入测试用例
#     test_module_list = LoadTestCase.load_test_case()
#     # 定义TestSuite
#     test_all_suite = unittest.TestSuite()
#     # 遍历测试用例对象
#     for test_module in test_module_list:
#         # 创建测试类
#         test_class = create_test_case_class(test_module)
#         # 创建TestSuite
#         test_suite = unittest.TestSuite()
#         # 将每个测试用例中加入到TestSuite当中
#         for test_case in test_module.test_case_list:
#             # 向测试类中添加测试方法
#             test_suite.addTest(test_class(test_case['title']))
#         # 将TestSuite加入到测试套件当中
#         test_all_suite.addTests(test_suite)
#
#     now_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#     save_report_path = os.path.abspath('ReportAndLog/Report')
#     file_name = save_report_path + '/result_' + now_time + '.html'
#     with open(file_name, 'wb') as file_open:
#         runner = HTMLTestRunner.HTMLTestRunner(stream=file_open, title='测试结果', description='测试报告')
#         # 运行测试
#         runner.run(test_all_suite)
#     # 进行浏览器截图
#     ScreenCapture.web_driver_screen_capture()
#     # 注意文件路径
#     # SendEmail.send_report('configure.conf')


# if __name__ == "__main__":
#     """
#     :description: 使用Excel运行测试
#     """
#     # 载入测试用例
#     total_test_list = LoadTestCase.load_test_case_for_excel()
#     print(json.dumps(total_test_list, ensure_ascii=False))
#     # 定义所有Excel的TestSuite
#     test_suite_for_all_excel = unittest.TestSuite()
#     for test_workbook_dict in total_test_list:
#         # 定义单个Excel的TestSuite
#         test_suite_for_single_excel = unittest.TestSuite()
#         # 遍历每个Excel的Sheet页(以Sheet页名称为key,以Sheet页中的测试步骤生成list为value)
#         for test_key, test_value in test_workbook_dict.items():
#             # 定义每一个Sheet页的的TestSuite
#             test_suite_for_sheet = unittest.TestSuite()
#             # 根据Sheet页生成测试用例类(以Sheet页为类名,以Sheet页生成list为类的内容)
#             test_sheet_class = create_test_case_class_for_file((test_key, test_value))
#             # 遍历每个类的测试步骤
#             for test_sheet_case in test_value:
#                 # 取步骤的title当做测试方法名,并将这个测试方法加入到Test_Suite当中
#                 test_suite_for_sheet.addTest(test_sheet_class(test_sheet_case['title']))
#             # 将每个Sheet页的TestSuite加入到单个Excel的TestSuite当中
#             test_suite_for_single_excel.addTests(test_suite_for_sheet)
#         # 将每个Excel的TestSuite加入整个TestSuite当中
#         test_suite_for_all_excel.addTests(test_suite_for_single_excel)
#
#     now_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#     save_report_path = os.path.abspath('ReportAndLog/Report')
#     file_name = save_report_path + '/result_' + now_time + '.html'
#     with open(file_name, 'wb') as file_open:
#         runner = HTMLTestRunner.HTMLTestRunner(stream=file_open, title='测试结果', description='测试报告')
#         # 运行测试
#         runner.run(test_suite_for_all_excel)
#     # 进行浏览器截图
#     ScreenCapture.web_driver_screen_capture()
#     # 注意文件路径
#     # SendEmail.send_report('D:/CI_Program/Python_Program/HighPin_VIK/configure.conf')


if __name__ == "__main__":
    """
    :description: 使用xml运行测试
    """
    # 载入测试用例
    total_test_list = LoadTestCase.load_test_case_for_xml()
    # print(json.dumps(total_test_list, ensure_ascii=False))
    # 定义所有文件的TestSuite
    test_suite_for_all_file = unittest.TestSuite()
    for test_file_dict in total_test_list:
        # 定义单个文件的TestSuite
        test_suite_for_single_file = unittest.TestSuite()
        # 遍历每个文件
        for test_key, test_value in test_file_dict.items():
            # 定义每一个文件的的TestSuite
            test_suite_for_file = unittest.TestSuite()
            # 根据文件生成测试用例类
            test_file_class = create_test_case_class_for_file((test_key, test_value))
            # 遍历每个类的测试步骤
            for test_file_case in test_value:
                # 取步骤的title当做测试方法名,并将这个测试方法加入到Test_Suite当中
                test_suite_for_file.addTest(test_file_class(test_file_case['title']))
            # 将每个文件的TestSuite加入到单个文化部的TestSuite当中
            test_suite_for_single_file.addTests(test_suite_for_file)
        # 将每个文件的TestSuite加入整个TestSuite当中
        test_suite_for_all_file.addTests(test_suite_for_single_file)

    now_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    save_report_path = os.path.abspath('ReportAndLog/Report')
    file_name = save_report_path + '/result_' + now_time + '.html'
    with open(file_name, 'wb') as file_open:
        runner = HTMLTestRunner.HTMLTestRunner(stream=file_open, title='测试结果', description='测试报告')
        # 运行测试
        result = runner.run(test_suite_for_all_file)
        error_count = result.error_count
        failure_count = result.failure_count
    # 进行浏览器截图
    ScreenCapture.web_driver_screen_capture()
    # 注意文件路径
    SendEmail.send_report('configure.conf', error_count, failure_count)

