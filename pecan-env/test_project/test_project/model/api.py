"""import threading
import
_CONTEXT = threading.local()
def __session_for_read():
    return enginefacade.reader.using(_CONTEXT)
def __session_for_write():
    return enginefacade.writer.using(_CONTEXT)
def get_student_details():"""
import MySQLdb as db

def db_register(sid,name,email,age,sex,branch):
    con = db.connect(db='uni300')
    cur = con.cursor()
#cur.execute('CREATE TABLE IF NOT EXISTS users(login VARCHAR(8), uid INT)')
#login= "viks"
#uid= 10
    
    q=cur.execute("insert into students VALUES('%s','%s','%s','%d','%s','%s')"%(sid,name,email,age,sex,branch))
#cur.execute("INSERT INTO users(login,uid)""VALUES(%s,%d)",("viks",10))
#cur.execute(sql)
   # import pdb
   # pdb.set_trace()
   # con.commit()
#cur.execute("UPDATE users SET uid=45 WHERE uid=40")
#con.commit()
#cur.execute("INSERT INTO users(login,uid)""VALUES(%s,%s)",("viks","10"))
    cur.close()
