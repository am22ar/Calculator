import mysql.connector
conn=mysql.connector.connect(host="localhost",username="root",password="", database="amar")

cur_obj=conn.cursor()

print("table contents:")

cur_obj.execute("SELECT * FROM EMPLOYEE")

print(cur_obj.fetchall())

sql_delete="DELETE FROM EMPLOYEE WHERE EMOB=231245"

try:
    cur_obj.execute(sql_delete)
    conn.commit()
    print("successfully Deleted.......")

except:
    conn.rollback()
print("contents of the table: ")
cur_obj.execute("SELECT * FROM EMPLOYEE")
print(cur_obj.fetchall())
conn.close()