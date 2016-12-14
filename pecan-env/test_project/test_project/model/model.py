#!/usr/bin/python
#import pdb
import MySQLdb as db

#Function for student registration(inserts values into student table)
def stud_register(sid,sname,email,age,sex,semister):
    con = db.connect(db='uni300')
    cur = con.cursor()
    cur.execute("insert into students VALUES('%s','%s','%s','%d','%s','%s')"%(sid,sname,email,int(age),sex,semister))
    con.commit()
   
    
#Function for Get operation, returns select statement from student table
def stud_select(sid):
   # print "I am in db_select"
    con = db.connect(db='uni300')
    cur = con.cursor()
    cur.execute("select * from students WHERE sid = '%s'"%(sid))
    data = cur.fetchone()
    con.commit()
    cur.close()
   # print data
    return data

#Function for DELETE Operation, Deletes entry from student table
def stud_delete(sid):
    con = db.connect(db='uni300')
    cur = con.cursor()
    cur.execute("DELETE FROM students WHERE sid= '%s'"%(sid))
    text= "DELETE Sucessfull"
    con.commit()
    cur.close()
   # return text

#Function for PUT operation, inserts value into faculty table
def fac_register(fid,fname,email,age,sex,ofcroom,expr,course):
    print "I am in register"
    con = db.connect(db='uni300')
    cur = con.cursor()
    print "inside db register"
   # pdb.set_trace()
    cur.execute("insert into faculty VALUES('%s','%s','%s','%d','%s','%d','%d','%s')"%(fid,fname,email,int(age),sex,int(ofcroom),int(expr),course))
    print "Insert Sucessfull"
    con.commit()
    cur.close()

#Function for GET operation for faculty table
def fac_select(fid):
   # pdb.set_trace()
    print "I am in fac_select"
    con = db.connect(db='uni300')
    cur = con.cursor()
    cur.execute("select * from faculty WHERE fid= '%s'"%(fid))
    data = cur.fetchone()
    con.commit()
    cur.close()
   # print data
    return data

#Function for DELETE operation for faculty table
def fac_delete(fid):
    con = db.connect(db='uni300')
    cur = con.cursor()
    cur.execute("DELETE FROM faculty WHERE fid= '%s'"%(fid))
    text= "DELETE Sucessfull"
    con.commit()
    cur.close()

#Function for PUT operation for course table
def course_register(cid,cname,semister):
    con = db.connect(db='uni300')
    cur = con.cursor()
    cur.execute("insert into courses VALUES('%s','%s','%s')"%(cid,cname,semister))
    con.commit()

#Function for GET operation for course table
def course_select(cid):
   # pdb.set_trace()
    print "I am in fac_select"
    con = db.connect(db='uni300')
    cur = con.cursor()
    cur.execute("select * from courses WHERE cid= '%s'"%(cid))
    data = cur.fetchone()
    con.commit()
    cur.close()
   # print data
    return data

#Function for DELTE operation for course table
def course_delete(cid):
    con = db.connect(db='uni300')
    cur = con.cursor()
    cur.execute("DELETE FROM courses WHERE cid= '%s'"%(cid))
    text= "DELETE Sucessfull"
    con.commit()
    cur.close()
#print db_delete('5436e')
#fac_register('345','Cenk','cenk@marist.edu',55,'m',2301,25,'cloudcomputing')
#print fac_select()
#print db_select('1245re')
#"db_register('346er','sandeep','sandeep@hotmail.com',29,'m','parallel')
