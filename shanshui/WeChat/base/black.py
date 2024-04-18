import logging
import os
import time
import traceback

import allure

from WeChat.base import base
from WeChat.base.base import BasePage


def get_time(self):
    t = time.localtime(time.time())
    cur_time = time.strftime("%Y-%m-%d_%H_%M_%S", t)
    return cur_time

def black_wrapper(fun):
    def run(*args, **kwargs):

        basepage:BasePage = args[0]
        try:
            logging.info("开始查找元素：{args[2]}")
            return  fun(*args, **kwargs)
        except Exception as e:
            logging.warning("未找到元素")
            curtime = basepage.get_time()
            tmp_name = curtime+".png"
            logging.info("当前图片路径 >>>" +(os.path.dirname(__file__)))
            tmp_path = os.path.join(os.path.dirname(__file__), "..", "images", tmp_name)
            basepage.screenshot(tmp_path)
            allure.attach.file(tmp_path, name="截图", attahment_type=allure.attachment_type.PNG)
            for black in base.black_list:
                logging.info(f"处理黑名单： {black}")
                eles = base.driver.find_elements(*black)
                if len(eles) > 0:
                    logging.info(f"点击黑名单弹框")
                    eles[0].click()
                    return fun(*args, **kwargs)
            logging.error(f"遍历黑名单，仍未找到元素，异常信息 ====> {e}")
            logging.error(f"traceback.format_exc() ====> {traceback.format_exc()}")
            raise e
    return run
