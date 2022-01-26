import  mysql.connector

con=mysql.connector.connect(host="localhost", user="root", password="", database="amar")

cur_delete=con.cursor()

cur_delete.callproc('mydelete',[104])

con.commit()

print("contents of table:")
cur_delete.execute("select * from employee order by ename")
print(cur_delete.fetchall())
con.close()