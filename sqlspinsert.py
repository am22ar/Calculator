import  mysql.connector

con=mysql.connector.connect(host="localhost", user="root", password="", database="amar")

cur_insert=con.cursor()

cur_insert.callproc('myinsert',[104,'vachana','asara road',1234554321])

con.commit()

print("contents of table:")
cur_insert.execute("select * from employee order by ename")
print(cur_insert.fetchall())
con.close()