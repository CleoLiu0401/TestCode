from Interface.apis.access_token import Token
from Interface.utils.read_data import GetData


class Students(Token, GetData):

    def get_student(self):
        get_api = "/api/ics/students/list"
        headers = {
            "token": self.get_ics_token()
        }
        req = {
            "method": "GET",
            "url": self.base_url+get_api,
            "headers": headers
        }

        r = self.send_api(req)

        if not r.json()["data"]:
            return self.add_student()

        student_uuid = r.json()["data"][0]["uuid"]

        return student_uuid

    def add_student(self):
        add_api = "/api/ics/students/add"
        headers = {
            "token": self.get_ics_token()
        }
        data = self.get_data_json("datas/student.json")

        req = {
            "method": "POST",
            "url": self.base_url + add_api,
            "headers": headers,
            "json": data
        }

        r = self.send_api(req)
        student_uuid = r.json()["data"]["uuid"]

        return student_uuid
