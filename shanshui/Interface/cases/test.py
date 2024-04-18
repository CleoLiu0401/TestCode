import json

from jsonpath import jsonpath

from Interface.apis.functions.ims_courses import Courses

course = Courses()
data = course.course_get().json()
#jsondata = json.load(data, ensure_ascii=False)
#print(jsondata)
value = '课程1'
parse = f"$.data.records[?(@.name=='{value}')]"
result = jsonpath(data, parse)[0]
# result = jsonpath(data, f"$.data.records[?(@.name=='{value}')]")
#result = jsonpath(data, "$.data.records[?(@.name=='课程1')]")
print(f"过滤后：{result}")
uuid = result["uuid"]
print(uuid)
#print(r)


"""def get_course_uuid(self, course_name):
    data = self.course_get().json()
    print(type(data))
    parse = f"$.data.records[?(@.name=='{course_name}')]"
    key = "uuid"
    course_uuid = self.get_key_json(data, parse, key)
    return course_uuid"""


"""def get_key_json(cls, data, parse, key):
    jsondata = json.dumps(data)
    # parse = f"$.data.records[?(@.name=='{value}')]"
    result = jsonpath(jsondata, parse)
    print(f"result:  {result}")
    value = result[key]
    return value"""