# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import os
import datetime
import unittest
import HTMLTestRunner
from EngineModule.CreateTestCaseModule import create_test_case_class
from RunModeModule import LoadTestCase
from WebdriverOperation import ScreenCapture
from EmailNotice import SendEmail

if __name__ == '__main__':
    # 载入测试用例
    test_module_list = LoadTestCase.load_test_case()
    # 定义TestSuite
    test_all_suite = unittest.TestSuite()
    # 遍历测试用例对象
    for test_module in test_module_list:
        # 创建测试类
        test_class = create_test_case_class(test_module)
        # 创建TestSuite
        test_suite = unittest.TestSuite()
        # 将每个测试用例中加入到TestSuite当中
        for test_case in test_module.test_case_list:
            # 向测试类中添加测试方法
            test_suite.addTest(test_class(test_case['title']))
        # 将TestSuite加入到测试套件当中
        test_all_suite.addTests(test_suite)

    now_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    save_report_path = os.path.abspath('../ReportAndLog/Report')
    file_name = save_report_path + '/result_' + now_time + '.html'
    with open(file_name, 'wb') as file_open:
        runner = HTMLTestRunner.HTMLTestRunner(stream=file_open, title='测试结果', description='测试报告')
        # 运行测试
        runner.run(test_all_suite)
    # 进行浏览器截图
    ScreenCapture.web_driver_screen_capture()
    # 注意文件路径
    SendEmail.send_report('../configure.conf')
