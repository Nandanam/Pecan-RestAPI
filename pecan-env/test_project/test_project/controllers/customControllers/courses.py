import pecan
from pecan import rest
from pecan import expose
from test_project import model
from test_project.controllers.entites import course
class CourseController(rest.RestController):
    _custom_actions = {
        'course'     : ['PUT'],
        'cours' : ['GET']
        }

    @expose('json')
    def course(self,cname,sem,credits):
        #st=student.Student(name,email,age,sex)

        #session =  model.Session()
        #session.add(st)
        #session.commit()       
        #session.close()
        return {'courses':'offered'}
    @expose('json')
    def cours(self):
        return {'course' : 'network'}
