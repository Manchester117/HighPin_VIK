# -*- coding: utf-8 -*-

__author__ = 'Peng.Zhao'

import json


def get_total_test_data(work_book_list):
    """
    :description: 返回所有测试用例步骤
    :param work_book_list: Excel的对象列表
    :return: 测试用例数据内容
    """
    # 所有测试用例数据将存放在列表当中
    total_test_list = []
    for work_book in work_book_list:
        # 获取每个sheet的名称
        sheet_name_list = work_book.get_sheet_names()
        # 每个Excel的测试数据蚁Sheet为单位,存储在字典当中
        test_case_dict = {}
        # 遍历每个sheet页
        for sheet_name in sheet_name_list:
            work_sheet = work_book[sheet_name]
            step_list = get_read_index(work_sheet)
            # 用字典来确定测试类
            test_case_dict[sheet_name] = step_list
        total_test_list.append(test_case_dict)
    # print(json.dumps(total_test_list, ensure_ascii=False))
    return total_test_list


def get_read_index(work_sheet):
    """
    :description: 查找单个Sheet当中的行号索引,并且创建存放测试数据的字典
    :param work_sheet: 单个Sheet页对象
    :return: 单个Sheet页的测试数据
    """
    # 行号索引
    row_index_list = []
    # 当前sheet中的所有测试步骤以列表形式存放
    sheet_step_list = []

    # 将所有不为None的title列的行号放入list
    for row_num in range(2, len(work_sheet.rows)):
        title_col_value = work_sheet.cell(row=row_num, column=1).value
        if title_col_value is not None:
            row_index_list.append(row_num)
            step_dict = {'title': None, 'data': None, 'corrParams': None, 'verify': None}
            sheet_step_list.append(step_dict)

    # 这里获得的行数必须+1,因为要做单元格遍历,所以行号必须是最后一行+1
    row_index_list.append(len(work_sheet.rows) + 1)

    begin_end_index_list = []
    # 根据list中的行号边界,取得行号区间
    for index in range(0, len(row_index_list)):
        if index + 1 < len(row_index_list):
            begin_col = row_index_list[index]
            end_col = row_index_list[index + 1]
            # 将步骤的上下边界放置到元组中,并将元组放置到列表里
            begin_end_index_list.append((begin_col, end_col))

    index = 0
    for begin_end in begin_end_index_list:
        read_cell(work_sheet, sheet_step_list[index], begin_end[0], begin_end[1])
        index += 1
    # print(json.dumps(sheet_step_list, ensure_ascii=False))
    return sheet_step_list


def read_cell(work_sheet, step_dict, begin, end):
    """
    :description: 遍历Sheet页中的所有单元格获取数据
    :param work_sheet:  单个Sheet页对象
    :param step_dict:   每个操作步骤的字典
    :param begin:       步骤行号的开始索引
    :param end:         步骤行号的结束索引
    :return:            无返回值
    """
    data = {}
    get_params_dict = {}
    post_params_dict = {}
    headers_dict = {}
    cookies_dict = {}
    corr_params_dict = {}
    verify_list = []

    for row_index in range(begin, end):
        # 填充title字段
        if work_sheet.cell(row=row_index, column=1).value is not None:
            step_dict['title'] = work_sheet.cell(row=row_index, column=1).value
        # 填充data字段
        if work_sheet.cell(row=row_index, column=2).value is not None:
            data['url'] = work_sheet.cell(row=row_index, column=2).value
        if work_sheet.cell(row=row_index, column=3).value is not None:
            data['method'] = work_sheet.cell(row=row_index, column=3).value
        if work_sheet.cell(row=row_index, column=4).value is not None:
            get_key = work_sheet.cell(row=row_index, column=4).value
            if work_sheet.cell(row=row_index, column=5).value is None:
                get_params_dict[get_key] = ''
            else:
                # 将get方法的参数放入到get_params_dict中
                get_params_dict[get_key] = work_sheet.cell(row=row_index, column=5).value
        if work_sheet.cell(row=row_index, column=6).value is not None:
            post_key = work_sheet.cell(row=row_index, column=6).value
            if work_sheet.cell(row=row_index, column=7).value is None:
                post_params_dict[post_key] = ''
            else:
                # 将post方法的参数放入到post_params_dict中
                post_params_dict[post_key] = work_sheet.cell(row=row_index, column=7).value
        # 填充json字段
        if work_sheet.cell(row=row_index, column=8).value is not None:
            data['json'] = work_sheet.cell(row=row_index, column=8).value
        else:
            data['json'] = None
        # 填充headers字段
        if work_sheet.cell(row=row_index, column=9).value is not None:
            headers_key = work_sheet.cell(row=row_index, column=9).value
            headers_dict[headers_key] = work_sheet.cell(row=row_index, column=10).value
        # 填充cookie字段
        if work_sheet.cell(row=row_index, column=11).value is not None:
            cookie_key = work_sheet.cell(row=row_index, column=11).value
            cookies_dict[cookie_key] = work_sheet.cell(row=row_index, column=12).value
        # 填充关联参数字段
        if work_sheet.cell(row=row_index, column=13).value is not None:
            corr_key = work_sheet.cell(row=row_index, column=13).value
            corr_params_dict[corr_key] = work_sheet.cell(row=row_index, column=14).value
        # 填充验证字段
        if work_sheet.cell(row=row_index, column=15).value is not None:
            verify_key = work_sheet.cell(row=row_index, column=15).value
            verify_value = work_sheet.cell(row=row_index, column=16).value
            verify_list.append((verify_key, verify_value))

    # 将所有填充好的数据结构放置到step_dict中
    if not get_params_dict:
        data['getParams'] = None
    else:
        data['getParams'] = get_params_dict

    if not post_params_dict:
        data['postParams'] = None
    else:
        data['postParams'] = post_params_dict

    if not headers_dict:
        data['headers'] = None
    else:
        data['headers'] = headers_dict

    if not cookies_dict:
        data['cookies'] = None
    else:
        data['cookies'] = cookies_dict

    if not corr_params_dict:
        step_dict['corrParams'] = None
    else:
        step_dict['corrParams'] = corr_params_dict

    if not verify_list:
        step_dict['verify'] = None
    else:
        step_dict['verify'] = verify_list

    # 将data放置到step_dict
    step_dict['data'] = data




