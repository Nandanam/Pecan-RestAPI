import pecan
from pecan import rest
from pecan import expose
from test_project.model import model
from test_project import db


class CourseController(rest.RestController):
    _custom_actions = {
        'course_register'     : ['PUT'],
        'course_select' : ['GET'],
        'course_delete' : ['DELETE']
        }
    
    #Function for PUT operation
    @expose('json')
    def course_register(self,cid,cname,semister):
        model.course_register(cid,cname,semister)
        text = "Course Updated Sucessfully"
        return text
    #Function for GET Operation
    @expose('json')
    def course_select(self,cid):
        return model.course_select(cid)

    #Function for DELETE operation
    @expose('json')
    def course_delete(self,cid):
        model.course_delete(cid)
        text = "Course deleted Sucessfully"
        return text
       
