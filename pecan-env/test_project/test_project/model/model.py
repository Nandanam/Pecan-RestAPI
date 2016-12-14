#!/usr/bin/python
import pdb
import MySQLdb as db
def db_register(sid,sname,email,age,sex,semister):
    print "I am in register"
    con = db.connect(db='uni300')
    cur = con.cursor()
    print "inside db register"
   # pdb.set_trace()
    cur.execute("insert into students VALUES('%s','%s','%s','%d','%s','%s')"%(sid,sname,email,int(age),sex,semister))
   # text1 = "Insert Sucessfull"
    print "Insert done"
    con.commit()
   # cur.close()
   # return text1
    
#Function for Get operation, returns select statement
def db_select(sid):
    print "I am in db_select"
    con = db.connect(db='uni300')
    cur = con.cursor()
    cur.execute("select * from students WHERE sid = '%s'"%(sid))
    data = cur.fetchone()
    con.commit()
    cur.close()
   # print data
    return data
def db_delete(sid):
    con = db.connect(db='uni300')
    cur = con.cursor()
    cur.execute("DELETE FROM students WHERE sid= '%s'"%(sid))
    text= "DELETE Sucessfull"
    con.commit()
    cur.close()
   # return text


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

 
def fac_select(fid):
   # pdb.set_trace()
    print "I am in fac_select"
    con = db.connect(db='uni300')
    cur = con.cursor()
    cur.execute("select * from faculty")
    data = cur.fetchone()
    con.commit()
    cur.close()
   # print data
    return data
#print db_delete('5436e')
#fac_register('4653e','Cenk','cenk@marist.edu',55,'m',2301,25,'cloudcomputing')
#print fac_select()
#print db_select('1245re')
#"db_register('346er','sandeep','sandeep@hotmail.com',29,'m','parallel')
