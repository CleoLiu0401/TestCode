#! -*- coding:utf-8 -*-
# 统一封装YAML文件读写方法
from Common.Log import MyLog

import yaml
from decimal import Decimal  # 如果yaml文件中有Decimal数据格式时需要有这个import

from Common.dict_option import DictOption


class Config:
    def __init__(self):
        self.log = MyLog

    def read(self, file_path: str):
        """
            读取YAML文件数据
            @:param file_path yaml文件的完整路径
            @:return config文件所有数据
        """

        try:
            with open(file_path, 'rb') as f:
                return yaml.load(f, Loader=yaml.FullLoader)
        except FileNotFoundError as e:
            msg = '没有找到该配置文件：{}，请确认你的文件名是否正确！！'.format(file_path)
            self.log.error(msg + "ERROR:" + str(e))
            raise FileNotFoundError(msg)
        except Exception as e:
            msg = '配置文件读取异常，请确认文件格式是否正确！！'
            self.log.error(msg + "ERROR:" + str(e))
            raise ValueError(msg)

    # 修改YAML文件数据--yaml配置文件需要是有两级数据
    def modify(self, file_path: str, key_list: list, value: any):
        """
        修改配置文件
        :param file_path yaml文件的完整路径
        :param key_list: 修改的配置文件的层级目录，以list方式传入,[一级目录，二级目录，...]
        :param value: 需要修改的新值
        :return:
        """
        data = self.read(file_path)
        # 保留一份旧文件，用于报错时恢复
        old_data = data
        with open(file_path, 'w', encoding="utf-8") as f:
            try:
                new_data = DictOption().modify_dict_value(data, key_list, value)
                yaml.dump(new_data, f, sort_keys=False, allow_unicode=True)
            except Exception as e:
                # 如果发生报错时，恢复初始文件
                yaml.dump(old_data, f, sort_keys=False, allow_unicode=True)
                msg = 'modify data error:{}'.format(e)
                self.log.error(msg)
                raise RuntimeError(msg)
        return self.read(file_path)
