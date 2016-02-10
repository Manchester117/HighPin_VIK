# -*- coding: utf-8 -*-
__author__ = 'Administrator'


def packing_test_case(test_case_list):
    """
    :description: 将测试用例的四个数据项分散到四个列表当中
    :param test_case_list: 测试用例
    :return: 返回4个测试用例的item列表
    """
    title_list = []
    req_data_list = []
    corr_list = []
    verify_list = []
    for item in test_case_list:
        title_list.append(item['title'])
        req_data_list.append(item['data'])
        corr_list.append(item['corr_params'])
        verify_list.append(item['verify'])

    return title_list, req_data_list, corr_list, verify_list
