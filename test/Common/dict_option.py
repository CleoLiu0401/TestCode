# coding=utf-8
import decimal
import json
import os
import re
import random
import datetime
import chardet
import gevent
from gevent import monkey
import time
from dateutil.relativedelta import relativedelta
from prettytable import PrettyTable
from Common.Log import MyLog
from math import sin, radians, cos, asin, sqrt
from multiprocessing import Pool


class DictOption:
    def __init__(self):
        self.log = MyLog

    def get_dict_key(self, you_dict):
        """
        该方法用于获取字典类型的所有key，包含子类中的key
        :param you_dict:
        :return tmp: 返回排序后的keylist
        """
        tmp = []
        if isinstance(you_dict, dict):
            for k, v in you_dict.items():
                tmp.append(k)
                # 判断数据类型是否字典，列表
                if isinstance(v, (dict, list)):
                    # 重复调用自己
                    ret = self.get_dict_key(v)
                    tmp += ret
        if isinstance(you_dict, list):
            for x in you_dict:
                if isinstance(x, (dict, list)):
                    ret = self.get_dict_key(x)
                    tmp += ret
        # 对list进行排序
        tmp.sort()
        return tmp

    def get_dict_value(self, you_dict):
        """
        该方法用于获取字典类型的所有value，包含子类中的value
        :param you_dict:
        :return tmp: 返回排序后的valuelist
        注：由于可能存在不同数据类型，排序时会报错，所以强制将所有数据转换为str类型返回
        """
        tmp = []
        if isinstance(you_dict, dict):
            for k, v in you_dict.items():
                # 判断数据类型是否字典，列表
                if isinstance(v, (dict, list)):
                    # 重复调用自己
                    ret = self.get_dict_value(v)
                    tmp += ret
                else:
                    tmp.append(str(v))
        if isinstance(you_dict, list):
            for x in you_dict:
                if isinstance(x, (dict, list)):
                    ret = self.get_dict_value(x)
                    tmp += ret
                else:
                    tmp.append(str(x))
        # 对list进行排序
        tmp.sort()
        return tmp

    def modify_dict_value(self, you_dict, key_list, value):
        """
        用于修改字典中的value值，实现不确定长度字典的修改
        :param you_dict: 要修改的字典
        :param key_list:
        :param value:
        :return:
        """
        if type(you_dict) is not dict:
            msg = '所需要的参数应该是dict格式，请确认你的传参；you_dict：{}'.format(you_dict)
            self.log.error(msg)
            raise TypeError(msg)
        if type(key_list) is not list:
            msg = '所需要的参数应该是list格式，请确认你的传参；key_list：{}'.format(you_dict)
            self.log.error(msg)
            raise TypeError(msg)
        yaml_data = you_dict

        # 首先将字典逐级读取出来，写入到data_list中
        tem = None
        data_list = []
        for n in range(len(key_list)):
            try:
                if n == 0:
                    tem = yaml_data[key_list[n]]
                else:
                    tem = tem[key_list[n]]
            except Exception as e:
                msg = '源数据没有key-{}！error:{}'.format(key_list[n], e)
                self.log.error(msg)
                raise TypeError(msg)
            data_list.insert(0, tem)

        # 修改需要修改的值后再封装字典
        new_dict = {}
        for m in range(len(key_list)):
            tem_dict = {}
            tem_list = []
            if m == 0:
                # 修改为需要修改的值
                tem_dict[key_list[-m - 1]] = value
            else:
                # 不修改的直接封装起来
                if isinstance(key_list[-m - 1], str):
                    tem_dict[key_list[-m - 1]] = new_dict
                elif isinstance(key_list[-m - 1], list):
                    tem_list = data_list[m + 1]
                    tem_list[key_list[-m - 1]] = new_dict
                else:
                    msg = '暂时不支持该数据格式！{}'.format(key_list[-m - 1])
                    self.log.error(msg)
                    raise TypeError(msg)
            new_dict = tem_dict

            if m == len(key_list) - 1:
                # 更新最外层的key
                yaml_data.update(new_dict)
                break
            else:
                # 逐层封装更新字典
                p = data_list[m + 1]
                if isinstance(p, dict):
                    p.update(new_dict)
                elif isinstance(p, list):
                    p = tem_list
                else:
                    msg = '暂时不支持该数据格式！{}'.format(p)
                    self.log.error(msg)
                    raise TypeError(msg)
                new_dict = p
        return yaml_data

    def dict_update_dict(self, source_dict, update_dict, action=None):
        """
        以字典传参方式更新字典值
        :param source_dict: 原字典（需要修改更新的字典）
        :param update_dict: 要更新为的目标字典值，如果字典元素为列表时，可用...代替对应位置不需要更新的列表元素
        :param action: True/False，不传或False时 只更新字典中存在的值，不新增；True时更新外还将把原来不存在的值加入字典；
        :return:
        """
        for key, value in update_dict.items():
            if key in source_dict:
                if isinstance(value, dict) and isinstance(source_dict[key], dict):
                    self.dict_update_dict(source_dict[key], value, action)
                elif isinstance(value, list) and isinstance(source_dict[key], list):
                    if action is True:
                        if len(value) > len(source_dict[key]):
                            source_dict[key][len(source_dict[key]):len(value)] = value[len(source_dict[key]):len(value)]
                    for d01, d02 in zip(source_dict[key], value):
                        if d02 is ...:
                            continue
                        if isinstance(d01, dict) and isinstance(d02, dict):
                            self.dict_update_dict(d01, d02, action)
                        else:
                            source_dict[key] = value
                else:
                    source_dict[key] = value
            else:
                if action is True:
                    source_dict[key] = value
                else:
                    self.log.warning('需要更新的值({})不在字典中！！'.format(key))
        return source_dict

    def dict_delete_dict(self, source_dict, del_dict):
        """
        以字典传参的方式删除字典值
        :param source_dict: 原字典（需要修改删除的字典）
        :param del_dict: 要被删除的字典值（目标字典），元素为列表时，可用...代替对应位置不需要删除的列表元素
        :return:
        """
        if not bool(del_dict):
            return {}
        for key, value in del_dict.items():
            if key in source_dict:
                if isinstance(value, dict) and isinstance(source_dict[key], dict):
                    source_dict[key] = self.dict_delete_dict(source_dict[key], value)
                elif isinstance(value, list) and isinstance(source_dict[key], list):
                    new_result = []
                    for d01, d02 in zip(source_dict[key], value):
                        if d02 is ...:
                            ...
                        elif isinstance(d01, dict) and isinstance(d02, dict):
                            d01 = self.dict_delete_dict(d01, d02)
                            if not bool(d01):
                                continue
                        else:
                            continue
                        new_result.append(d01)
                    if len(source_dict[key]) > len(value):
                        new_result.extend(source_dict[key][len(value):len(source_dict[key])])
                    source_dict[key] = new_result
                else:
                    source_dict.pop(key)
            else:
                self.log.warning('需要删除的值({})不在字典中！！'.format(key))
        return source_dict

    def get_file_last_modify_time(self, file_path):
        """
        查询文件（文件夹）的最后修改时间
        :param file_path: 文件（文件夹）的详细路径信息
        :return: 最后修改时间
        """
        try:
            last_time = os.path.getmtime(file_path)
        except Exception as e:
            self.log.error('查询文件（文件夹）的最后修改时间失败，ERROR:{}'.format(e))
            last_time = None
        self.log.info('文件（{}）的最后修改时间为：{}'.format(file_path, last_time))
        return last_time

    def remove_file(self, file_path):
        """
        删除文件--只支持删除文件，不支持删除文件夹
        :param file_path: 文件的详细路径信息
        :return:
        """
        try:
            os.remove(file_path)
        except Exception as e:
            self.log.error('删除文件失败，ERROR:{}'.format(e))
            return False
        self.log.info('文件（{}）删除完成'.format(file_path))
        return True
