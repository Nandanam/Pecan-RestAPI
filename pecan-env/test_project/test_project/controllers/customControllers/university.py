import pecan
import pdb
#import random
import uuid
from pecan import rest
from pecan import expose
from test_project import model
from test_project.controllers.entites import student
#from test_project.db import database
#from controllers.customControllers import faculty

class UniversityController(rest.RestController):
    _custom_actions = {
        'register'     : ['PUT'],
	'uni' : ['GET']
	}

    @expose('json')
    def register(self,stud_name,email,age,sex,branch):
       # st=student.Student(stud_name,email,age,sex,branch)
        sid = uuid.uuid4()
       # random.shuffle(sid)
        #session =  model.Session()
        #session.add(st)
        #session.commit()	
        #session.close()
	pdb.set_trace()
	model.model.db_register(sid,stud_name,email,int(age),sex,branch)
        return {'a' :'b'}
    @expose('json')
    def uni(self):
        return {'univ' : 'Marist'}
   
   # fac = faculty.FacultyController()
