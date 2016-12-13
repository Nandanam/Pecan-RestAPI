#!/usr/bin/python

import MySQLdb as db

def createDataBase():
    
    con = db.connect(user="root", passwd="root")
    cur = con.cursor()
    #cur.execute('DROP DATABASE uni')
  #  cur.execute('CREATE DATABASE IF NOT EXISTS uni300;')
    cur.execute("GRANT ALL ON uni300.* to ''@'localhost'")
    #cur.commit()
   # cur.close()
    con = db.connect(db='uni300')
#import MySQLdb as db
#def db_register(sid,name,email,age,sex,branch):
   # con = db.connect(db='uni300')
   # cur = con.cursor()
#cur.execute('CREATE TABLE IF NOT EXISTS users(login VARCHAR(8), uid INT)')
#lo:gin= "viks"
#uid= 10

   # cur.execute("insert into students VALUES('%s','%s','%s','%d','%s','%s')"%(sid,name,email,age,sex,branch))
#cur.execute("INSERT INTO users(login,uid)""VALUES(%s,%d)",("viks",10))
#cur.execute(sql)
   # pdb.set_trace()
   # con.commit()

   # cur = con.cursor()
    #cur.execute('CREATE TABLE IF NOT EXISTS students(sid INT,sname VARCHAR(20),email VARCHAR(20),age INT,sex VARCHAR(3),semister VARCHAR(10))')
    #cur.execute('CREATE TABLE IF NOT EXISTS faculty(fid INT,fname VARCHAR(20),email VARCHAR(20),age INT,sex VARCHAR(3),ofcroom INT,expr INT, course VARCHAR(20))')
   # cur.execute('CREATE TABLE IF NOT EXISTS courses(cid INT,cname VARCHAR(20),semister VARCHAR(10))')

    #cur.execute("insert into students VALUES('%d','%s','%s','%d','%s','%s')"%(20,"vikas","nandana@gmail.com",23,"M","Fall"))

    #cur.execute("insert into faculty VALUES('%d','%s','%s','%d','%s','%d','%d','%s')"%(100,"ron","ron@gmail.com",50,"M",201,20,"networks"))

   # cur.execute("insert into courses VALUES('%d','%s','%s')"%(1006,"Parallel Comp","Fall"))
   # con.commit()


