from Interface.apis.access_token import Token


class Courses(Token):

    def get_courses(self):
        get_api = "/api/ics/educlasses"
        headers = {
            "token": self.ics_token
        }
        req = {
            "method": "GET",
            "url": self.base_url + get_api,
            "headers": headers
        }
        r = self.send_api(req)
        course_uuid = r.json()["data"]["records"][0]["uuid"]
        return course_uuid
