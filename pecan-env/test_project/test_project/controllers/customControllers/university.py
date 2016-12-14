import pecan
import pdb
#import random
import uuid
from pecan import rest
from pecan import expose
from test_project.model import model
from test_project import db
from test_project.controllers.entites import student
#from test_project.db import database
#from controllers.customControllers import faculty

class UniversityController(rest.RestController):
    _custom_actions = {
        'register'     : ['PUT'],
	'give_details' : ['GET'],
        'update_details':['DELETE']
	}

    @expose('json')
    def register(self,sid,sname,email,age,sex,semister):
       # print "Inside register"
        model.db_register(sid,sname,email,int(age),sex,semister)
       # print "Back to register"
        text = "Student Details Registered Sucessfully"
        return text
    @expose('json')
    def give_details(self,sid):
        return model.db_select(sid)
       # return model.db_select(sid) 
    @expose('json')
    def update_details(self,sid):
        model.db_delete(sid)
        return {'up' : 'date'}
   # fac = faculty.FacultyController()
