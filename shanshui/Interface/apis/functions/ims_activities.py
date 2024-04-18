from Interface.apis.access_token import Token
from Interface.utils.read_data import GetData


class Activities(Token, GetData):

    def activity_discount_create(self, data):
        # base_url = self.get_base_url()
        create_api = "/api/ims/flash-sales/create"
        headers = {
            "token": self.access_token
        }

        req = {
            "method": "POST",
            "url": self.base_url+create_api,
            "headers": headers,
            "json": data
        }

        r = self.send_api(req)
        return r

    def activity_discount_get(self, activity_name):
        # base_url = self.get_base_url()
        get_api = "/api/ims/flash-sales"
        headers = {
            "token": self.access_token
        }

        params = {
            "like_key_value": activity_name
        }
        req = {
            "method": "GET",
            "url": self.base_url+get_api,
            "headers": headers,
            "params": params
        }
        r = self.send_api(req)
        return r

    def activity_discount_delete(self, activity_uuid):
        # base_url = self.get_base_url()
        del_api = "/api/ims/flash-sales/delete/"
        headers = {
            "token": self.access_token,
        }
        req = {
            "method": "POST",
            "url": self.base_url+del_api+activity_uuid,
            "headers": headers
        }
        r = self.send_api(req)
        return r
