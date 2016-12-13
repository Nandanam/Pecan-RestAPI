#!/usr/bin/python
import pdb
import MySQLdb as db
def db_register(sid,sname,email,age,sex,branch):
    print "I am in register"
    con = db.connect(db='uni300')
    cur = con.cursor()
    print "inside db register"
   # pdb.set_trace()
    cur.execute("insert into students VALUES('%s','%s','%s','%d','%s','%s')"%(sid,sname,email,int(age),sex,branch))
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
    cur.execute("DELETE FROM students WHERE sid= '%s'")
    text= "DELETE Sucessfull"
    con.commit()
    cur.close()
    return text
 
#print db_select('1245re')
#db_register('346er','sandeep','sandeep@hotmail.com',29,'m','parallel')
