import pecan
from pecan import rest
from pecan import expose
from test_project.model import model
from test_project import db
#from test_project.controllers.entites import faculty
from test_project.controllers.customControllers import courses

class FacultyController(rest.RestController):
    _custom_actions = {
        'fac_register'     : ['PUT'],
        'fac_select' : ['GET'],
        'fac_delete' : ['DELETE']
        }
    #Function for PUT operation 
    @expose('json')
    def fac_register(self,fid,fname,email,age,sex,ofcroom,expr,course):
        model.fac_register(fid,fname,email,age,sex,ofcroom,expr,course)
        text = "Faculty details updated Sucessfully"
        return text

    #Function for GET operation
    @expose('json')
    def fac_select(self,fid):
        return model.fac_select(fid)
    
    #Function for DELETE Operation
    @expose('json')   
    def fac_delete(self,fid):
        model.fac_delete(fid)
        text = "Deleted Sucessfully"
        return text

    cor=courses.CourseController()
