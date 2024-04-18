from Interface.apis.access_token import Token
from Interface.apis.base_api import BaseApi


class Order(Token, BaseApi):

    def cart_add(self, data):

        add_api = "/api/ics/cart-goods/add"
        headers = {
            "token": self.ics_token
        }
        req = {
            "method": "POST",
            "url": self.base_url+add_api,
            "headers": headers,
            "json": data
        }

        r = self.send_api(req)
        # goods_uuid = r.json()["data"]["uuid"]
        return r

    def order_settle(self, goods):
        settle_api = "/api/ics/order-sheets/settle"
        headers = {
            "token": self.ics_token
        }
        data = {
            "order_type": "educourse",
            "cart_goods": goods
        }
        req = {
            "method": "POST",
            "url": self.base_url+settle_api,
            "headers": headers,
            "json": data
        }

        r = self.send_api(req)
        return r

    def order_pay(self, data):
        pay_api = "/api/ics/order-sheets/pay"
        headers = {
            "token": self.ics_token
        }
        req = {
            "method": "POST",
            "url": self.base_url+pay_api,
            "headers": headers,
            "json": data
        }

        r = self.send_api(req)
        return r
