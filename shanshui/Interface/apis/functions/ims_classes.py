from Interface.apis.access_token import Token
from Interface.utils.read_data import GetData


class Classes(Token, GetData):

    def class_create(self, data):
        # base_url = self.get_base_url()
        create_api = "/api/ims/educlasses/create"
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

    def class_get(self, class_name):
        # base_url = self.get_base_url()
        get_api = "/api/ims/educlasses"
        headers = {
            "token": self.access_token
        }
        params = {
            "like_key_value": class_name
        }
        req = {
            "method": "GET",
            "url": self.base_url+get_api,
            "headers": headers,
            "params": params
        }
        r = self.send_api(req)
        return r

    def class_delete(self, class_uuid):
        # base_url = self.get_base_url()
        # 只能删除未销售或已结束销售的班级
        del_api = "/api/ims/educlasses/delete/"
        headers = {
            "token": self.access_token,
        }

        req = {
            "method": "POST",
            "url": self.base_url+del_api+class_uuid,
            "headers": headers
        }
        r = self.send_api(req)
        return r
