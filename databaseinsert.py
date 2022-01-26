import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="", database="amar")

cursor = db.cursor()

sqlinsert = "INSERT INTO EMPLOYEE(EID,ENAME,EADD,EMOB) VALUES(105,'rutuja','solapur',987065432)"

try:
    cursor.execute(sqlinsert)
    db.commit()
    print("record inserted....")

except:
    db.rollback()

db.close()