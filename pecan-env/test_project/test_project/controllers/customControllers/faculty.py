import pecan
from pecan import rest
from pecan import expose
from test_project.model import model
from test_project import db
from test_project.controllers.entites import faculty
class FacultyController(rest.RestController):
    _custom_actions = {
        'prof'     : ['PUT'],
        'pro_select' : ['GET']
        }

    @expose('json')
    def prof(self,fid,fname,email,age,sex,ofcroom,expr,course):
        #st=student.Student(name,email,age,sex)

        #session =  model.Session()
        #session.add(st)
        #session.commit()       
        #session.close()
        model.fac_register(fid,fname,email,age,sex,ofcroom,expr,course)
        return {'b':'c'}
    @expose('json')
    def pro_select(self,fid):
        print "Inside pro_select"
        return model.fac_select(fid)
        #return {'viks' : 'CS'}

