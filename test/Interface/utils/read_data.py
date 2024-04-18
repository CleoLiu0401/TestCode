import logging
import os

import yaml


class GetData:


    def get_data(self, filename):
        logging.info("获取数据")
        with open(filename, encoding="utf-8") as f:
            datas = yaml.safe_load(f)
            return  datas

    def get_fram_root_path(self):
        '''
        获取测试框架项目的路径
        '''
        return os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

