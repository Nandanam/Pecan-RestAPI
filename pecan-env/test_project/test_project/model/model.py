#import sqlite
import sqlalchemy
from sqlalchemy import Boolean, Column
from sqlalchemy import ForeignKey, Integer
from sqlalchemy import schema, String, Text
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb as db
def db_register(sid,name,email,age,sex,branch):
    con = db.connect(db='uni300')
    cur = con.cursor()
#cur.execute('CREATE TABLE IF NOT EXISTS users(login VARCHAR(8), uid INT)')
#lo:gin= "viks"
#uid= 10
    
    q=cur.execute("insert into students VALUES('%s','%s','%s','%d','%s','%s')"%(sid,name,email,age,sex,branch))
#cur.execute("INSERT INTO users(login,uid)""VALUES(%s,%d)",("viks",10))
#cur.execute(sql)
   # pdb.set_trace()
    con.commit(q)
    
#cur.execute("UPDATE users SET uid=45 WHERE uid=40")
#con.commit()
"""Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
   ## __table_args__ = (
      ##schema.UniqueConstraint('id',name='uniq_student0id'),
      ##table_args()
    sid = Column(Integer, autoincrement=True, primary_key=True)
    name=Column(String(64))
    email=Column(String(64))
    age=Column(Integer)
    sex=Column(String(64))

class Faculty(Base):
    __tablename__ = 'faculty'
    fid = Column(Integer, autoincrement=True, primary_key=True)
    name=Column(String(64))
    email=Column(String(64))
    age=Column(Integer)
    sex=Column(String(64))
    exper=Column(Integer)

class Course(Base):
    __tablename__ = 'course'
    cid = Column(Integer, autoincrement=True, primary_key=True)
    cname = Column(String(64))
    sem = Column(String(64))
"""
