import requests

from Interface.apis.access_token import Token


class Function(Token):

    def create(self,data):
        create_url = ""
        params = {
            "asscee_token": self.access_token
        }

        r = requests.request("POST", create_url, json=data, params=params)
        return r