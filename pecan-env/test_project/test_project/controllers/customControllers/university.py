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
    def register(self,stud_name,email,age,sex,branch):
        st=student.Student(stud_name,email,age,sex,branch)
        sid = uuid.uuid4()
       # import model
       # random.shuffle(sid)
        #session =  model.Session()
        #session.add(st)
        #session.commit()	
        #session.close()
	#pdb.set_trace()
	model.db_register(sid,stud_name,email,age,sex,branch)
       # db.db_register(sid,stud_name,email,age,sex,branch)
        return {'a' :'b'}
    @expose('json')
    def give_details(self,sid):
        model.db_select(sid)
        return {'univ' : 'Marist'}
    @expose('json')
    def update_details(self):
        model.db_delete(sid)
        return {'up' : 'date'}
   # fac = faculty.FacultyController()
