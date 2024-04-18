import json
import logging
import os

import yaml
from jsonpath import jsonpath


class GetData:

    @classmethod
    def get_data_yaml(cls, filename):
        # file_path = os.sep.join([GetData.get_frame_root_path(), filename])
        file_path = cls.gene_file_path(filename)
        logging.info(f"获取文件{file_path}数据")
        with open(file_path, encoding="utf-8") as f:
            datas = yaml.safe_load(f)
            return datas

    @classmethod
    def get_frame_root_path(cls):
        """
        获取测试框架项目的路径
        """
        return os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

    @classmethod
    def gene_file_path(cls, filename):
        file_path = os.sep.join([GetData.get_frame_root_path(), filename])
        return file_path

    @classmethod
    def get_data_json(cls, filename):
        logging.info(f"获取文件{filename}数据")
        # file_path = os.sep.join([GetData.get_frame_root_path(), filename])
        file_path = cls.gene_file_path(filename)
        with open(file_path, encoding="utf-8") as f:
            datas = json.load(f)
            return datas

    @classmethod
    def add_data_json(cls, filename, data):
        logging.info(f"对{filename}文件进行数据更新")
        old_data = cls.get_data_json(filename)
        logging.info(f"文件原有数据为：{old_data}")
        old_data.update(data)
        new_data = old_data
        logging.info(f"更新后数据为：{new_data}，重新写入文件")
        # file_path = os.sep.join([GetData.get_frame_root_path(), filename])
        file_path = cls.gene_file_path(filename)
        with open(file_path, 'w', encoding="utf-8") as new_f:
            json.dump(new_data, new_f, ensure_ascii=False)

    @classmethod
    def update_data_json(cls, filename, data):
        cls.add_data_json(filename, data)
        logging.info("获取更新后文件数据")
        return cls.get_data_json(filename)

    @classmethod
    def file_data_clear(cls, filename):
        # file_path = os.sep.join([GetData.get_frame_root_path(), filename])
        file_path = cls.gene_file_path(filename)
        logging.info(f"清除{filename}文件内容")
        with open(file_path, 'w', encoding="utf-8") as f:
            f.seek(0)
            f.truncate()

    @classmethod
    def file_data_init(cls, filename, filename_init):
        cls.file_data_clear(filename)
        data = cls.get_data_json(filename_init)
        # file_path = os.sep.join([GetData.get_frame_root_path(), filename])
        file_path = cls.gene_file_path(filename)
        logging.info(f"{filename}文件内容初始化")
        with open(file_path, 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

    @classmethod
    def get_key_json(cls, data, parse, key):
        # jsondata = json.dumps(data)
        # parse = f"$.data.records[?(@.name=='{value}')]"
        logging.info(f"对数据：{data}进行过滤，并获取{key}的值")
        try:
            result = jsonpath(data, parse)[0]
        except TypeError as e:
            print(e)
        else:
            logging.info(f"过滤后结果:  {result}")
            value = result[key]
            logging.info(f"{key}的值为: {value}")
            return value
