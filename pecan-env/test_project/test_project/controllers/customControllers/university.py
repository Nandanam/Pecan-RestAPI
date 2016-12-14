import pecan
from pecan import rest
from pecan import expose
from test_project.model import model
from test_project import db
from test_project.controllers.customControllers import faculty


class UniversityController(rest.RestController):
    _custom_actions = {
        'stud_register'     : ['PUT'],
	'stud_select' : ['GET'],
        'stud_delete':['DELETE']
	}
    
    #Function for PUT operation
    @expose('json')
    def stud_register(self,sid,sname,email,age,sex,semister):
       # print "Inside register"
        model.stud_register(sid,sname,email,int(age),sex,semister)
       # print "Back to register"
        text = "Student Details Registered Sucessfully"
        return text

    #Function for GET Operation
    @expose('json')
    def stud_select(self,sid):
        return model.stud_select(sid)
     
    #Function for DELETE function
    @expose('json')
    def stud_delete(self,sid):
        model.stud_delete(sid)
        text = "Student Details Deleted Sucessfully"
        return text

    fac = faculty.FacultyController()
