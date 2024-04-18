from Interface.apis.base_api import BaseApi


class Token(BaseApi):

    def __init__(self, params1, papams2):
        self.access_token = self.get_access_token(params1, papams2)

    def get_access_token(self):
        #corpid = ""
        #corpsecret = ""
        url = ""
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }

        req = {
            "method": "GET",
            "url": url,
            "params": params
        }
        r = self.send_api(req)

        #r = requests.request(method="GET", url=url, params=params)
        access_token = r.json()["access_token"]
        return access_token