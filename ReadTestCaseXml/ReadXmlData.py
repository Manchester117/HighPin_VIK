# -*- coding: utf-8 -*-

__author__ = 'Peng.Zhao'


from lxml import etree
import json


def get_total_test_data(xml_list):
    """
    :description: 获取所有的xml文件的测试数据
    :return: 返回所有数据
    """
    total_test_list = []
    for xml in xml_list:
        doc = etree.ElementTree(file=xml)
        xml_root = doc.getroot()
        single_test = get_single_test_data(xml_root)
        total_test_list.append(single_test)
    print(json.dumps(total_test_list, ensure_ascii=False))
    # print(total_test_list)
    return total_test_list


def get_single_test_data(xml_root):
    """
    :description: 从xml中获取TestSuite
    :return: 返回单条测试suite
    """
    test_suite_dict = dict()
    test_suite_dict[xml_root.get('name')] = list()
    for child in xml_root:
        if child.tag == 'TestCase':
            test_case = get_test_case_data(child)
            test_suite_dict[xml_root.get('name')].append(test_case)
    # print(json.dumps(test_suite_dict, ensure_ascii=False))
    # print(test_suite_dict)
    return test_suite_dict


def get_test_case_data(test_case):
    """
    :description: 从xml中获取数据拼凑成dict
    :return: 返回单条测试用例
    """
    test_case_dict = dict()
    for leaf in test_case:
        if leaf.tag == 'title':
            test_case_dict['title'] = leaf.text
        if leaf.tag == 'data':
            test_case_dict['data'] = get_request_data(leaf)
        if leaf.tag == 'corrParams':
            test_case_dict['corrParams'] = get_correlation_data(leaf)
        if leaf.tag == 'verify':
            test_case_dict['verify'] = get_verify_data(leaf)
    return test_case_dict


def get_request_data(leaf_request_data):
    """
    :description: 从xml中获取请求的数据
    :return: 返回请求数据的dict
    """
    request_data = dict()
    for item in leaf_request_data.iter():
        if item.tag == 'url' or item.tag == 'method' or item.tag == 'json':
            request_data[item.tag] = item.text.rstrip()
        if item.tag == 'getParams' or item.tag == 'postParams' or item.tag == 'headers' or item.tag == 'cookies':
            param_dict = dict()
            for param in item.iter():
                if param.text is not None and param.text.find('\n') == -1:
                    # 替换Xml中的'&amp;',并去掉两边的空白字符
                    param_content = param.text.replace('&amp;', '&')
                    param_dict[param.get('name')] = param_content.rstrip()
            if param_dict.__len__() == 0:
                param_dict = None
            request_data[item.tag] = param_dict
    return request_data


def get_correlation_data(leaf_corr_data):
    """
    :description: 从xml中获取需要关联的正则表达式
    :return: 返回关联的dict
    """
    corr_data = dict()
    for item in leaf_corr_data.iter():
        if item.text is not None and item.text.find('\n') == -1:
            corr_data[item.get('name')] = item.text.rstrip()
    if corr_data.__len__() == 0:
        corr_data = None
    return corr_data


def get_verify_data(leaf_verify_data):
    """
    :description: 从xml中获取需要验证的数据
    :return: 返回验证list
    """
    verify_data = list()
    for item in leaf_verify_data:
        if item in leaf_verify_data.iter():
            check_tuple = (item.get('name'), item.text.rstrip())
            verify_data.append(check_tuple)
    if verify_data.__len__() == 0:
        verify_data = None
    return verify_data


