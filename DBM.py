import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='mydatabase')
    
def addEmp(t):
    db=getConnection()
    sql='insert into mytable values(%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()



def selectAllEmp():
    db=getConnection()
    sql='select * from mytable'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

    
def deleteEmp(id):
    db=getConnection()
    sql='delete from  mytable where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    db.commit()
    db.close()

def selectEmpById(id):
    db=getConnection()
    sql='select * from mytable where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]

def updateEmp(t):
    db=getConnection()
    sql='update mytable set name=%s,contact=%s,email=%s,pwd=%s where id=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def name_pass():
    db=getConnection()
    cr=db.cursor()
    sql='select name,pwd from mytable'
    cr.execute(sql)
    dat=cr.fetchall()
    db.commit()
    db.close()
    return dat
