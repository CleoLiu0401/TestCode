import requests

from Interface.utils.log_util import logger


class BaseApi:

    def send_api(self, req):

        logger.info(f"请求数据为 ====> {req}")
        # **req 等同于 request.request(method="get"....)
        r = requests.request(**req)
        logger.info(f"响应数据为 ====> {r.text}")
        return r