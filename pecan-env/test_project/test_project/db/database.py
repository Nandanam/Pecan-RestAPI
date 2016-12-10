
"""def db_register(self,sid,name,email,age,sex,branch):
    con = db.connect(db='same200')
    cur = con.cursor()
#cur.execute('CREATE TABLE IF NOT EXISTS users(login VARCHAR(8), uid INT)')
#login= "viks"
#uid= 10
    cur.execute("insert into students VALUES('%d','%s','%s','%d','%s','%s')"%(sid,name,email,age,sex,branch))
#cur.execute("INSERT INTO users(login,uid)""VALUES(%s,%d)",("viks",10))
#cur.execute(sql)
    con.commit()
#cur.execute("UPDATE users SET uid=45 WHERE uid=40")
#con.commit()
#cur.execute("INSERT INTO users(login,uid)""VALUES(%s,%s)",("viks","10"))
    cur.close()"""


    
