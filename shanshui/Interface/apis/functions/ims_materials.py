from Interface.apis.access_token import Token
from Interface.utils.read_data import GetData


class Materials(Token, GetData):

    def get_materials_group(self, group_name):
        # base_url = self.get_base_url()
        get_api = "/api/ims/material-groups/tree"
        params = {
            "access_token": self.access_token
        }
        req = {
            "method": "GET",
            "url": self.base_url + get_api,
            "params": params,
        }

        r = self.send_api(req)
        material_group_uuid = r.json()["uuid"]
        return material_group_uuid

    def get_material(self, type):
        # base_url = self.get_base_url()
        get_api = "/api/ims/materials"
        params = {
            "token": self.access_token,
            "group": self.get_materials_group(),
            "file_type": type
        }
        req = {
            "method": "GET",
            "url": self.base_url+get_api,
            "params": params
        }

        r = self.send_api(req)
        material_group_uuid = r.json()["data"]["children"][0]["uuid"]
        return material_group_uuid