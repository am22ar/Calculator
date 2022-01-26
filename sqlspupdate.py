import  mysql.connector

con=mysql.connector.connect(host="localhost", user="root", password="", database="amar")

cur_update=con.cursor()

cur_update.callproc('myupdate',[1001001001,'rutuja'])

con.commit()

print("contents of table:")
cur_update.execute("select * from employee order by ename")
print(cur_update.fetchall())
con.close()