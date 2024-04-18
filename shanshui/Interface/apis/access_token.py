from Interface.apis.base_api import BaseApi
import logging


class Token(BaseApi):

    def __init__(self):
        self.base_url = super().get_base_url()
        self.access_token = self.get_access_token()
        self.ics_token = self.get_ics_token()

    def get_access_token(self):
        telephone = "13070182356"
        password = "+y2E84OoHTt2rh/R8hQ5UA=="
        # base_url = self.get_base_url()
        login_api = "/api/ims/employees/login"
        params = {
            "telephone": telephone,
            "password": password,
            "type": "password"
        }

        req = {
            "method": "POST",
            "url":  self.base_url+login_api,
            "json": params
        }

        logging.info("管理系统登录并获取token")
        r = self.send_api(req)
        # r = requests.request(method="POST", url=base_url+api_url, json=params)
        access_token = r.json()["data"]["token"]
        logging.info(f"获取到的token为：{access_token}")
        return access_token

    def get_ics_token(self):
        telephone = "18514532166"
        password = "3SjEnQkxqsmBcoAKm4ydXA=="
        # base_url = self.ics_base_url()
        login_api = "/api/ics/customers/login"
        params = {
            "telephone": telephone,
            "password": password,
            "type": "password"
        }

        req = {
            "method": "POST",
            "url": self.base_url+login_api,
            "json": params
        }

        logging.info("小程序登录并获取token")
        r = self.send_api(req)
        # r = requests.request(method="POST", url=base_url+api_url, json=params)
        ics_token = r.json()["data"]["token"]
        logging.info(f"获取到的token为：{ics_token}")
        return ics_token
