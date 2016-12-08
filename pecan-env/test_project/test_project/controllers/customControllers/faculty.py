import pecan
from pecan import rest
from pecan import expose
from test_project import model
from test_project.controllers.entites import faculty
class FacultyController(rest.RestController):
    _custom_actions = {
        'prof'     : ['PUT'],
        'pro' : ['GET']
        }

    @expose('json')
    def prof(self,name,email,age,sex,branch,experience):
        #st=student.Student(name,email,age,sex)

        #session =  model.Session()
        #session.add(st)
        #session.commit()       
        #session.close()
        return {'b':'c'}
    @expose('json')
    def pro(self):
        return {'viks' : 'CS'}

