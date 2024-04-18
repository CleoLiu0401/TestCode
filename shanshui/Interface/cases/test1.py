from Interface.apis.functions.ics_courses import Courses
from Interface.apis.functions.ics_order import Order
from Interface.apis.functions.ics_students import Students
from Interface.utils.read_data import GetData

order = Order()
student = Students()
course = Courses()
getdata = GetData()


# student_uuid = student.get_student()
course_uuid = course.get_courses()
print(course_uuid)

