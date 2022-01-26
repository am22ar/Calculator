import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="amar")

curupdate = conn.cursor()

try:
    sqlupdate="UPDATE EMPLOYEE SET EMOB=100000002 WHERE EMOB=1000000000 "

    curupdate.execute(sqlupdate)
    print("updated successfully.......")
    conn.commit()

except:
    conn.rollback()

conn.close()