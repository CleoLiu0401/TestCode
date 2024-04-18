from Interface.apis.access_token import Token
from Interface.utils.read_data import GetData


class Courses(Token, GetData):

    def get_courses_group(self):
        # base_url = self.get_base_url()
        get_api = "/api/ims/educourse-groups/tree"
        headers = {
            "token": self.access_token
        }
        req = {
            "method": "GET",
            "url": self.base_url+get_api,
            "headers": headers
        }

        r = self.send_api(req)
        group_uuid = r.json()["data"]["uuid"]
        return group_uuid

    def course_create(self, data):
        # base_url = self.get_base_url()
        create_api = "/api/ims/educourses/create"
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

    def course_get(self):
        # base_url = self.get_base_url()
        get_api = "/api/ims/educourses"
        headers = {
            "token": self.access_token,
        }
        req = {
            "method": "GET",
            "url": self.base_url+get_api,
            "headers": headers
        }
        r = self.send_api(req)
        return r

    def get_course_uuid(self, course_name):
        data = self.course_get().json()
        parse = f"$.data.records[?(@.name=='{course_name}')]"
        key = "uuid"
        course_uuid = self.get_key_json(data, parse, key)
        return course_uuid

    def course_delete(self, course_uuid):
        # base_url = self.get_base_url()
        del_api = "/api/ims/educourses/delete/"
        headers = {
            "token": self.access_token,
        }

        req = {
            "method": "POST",
            "url": self.base_url+del_api+course_uuid,
            "headers": headers
        }
        r = self.send_api(req)
        return r
