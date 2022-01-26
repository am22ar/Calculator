import  mysql.connector

con=mysql.connector.connect(host="localhost", user="root", password="", database="amar")

cur=con.cursor()

cur.callproc('sqlselect_emp')

print("..........employee details..........")

for results in cur.stored_results():
    rlist=results.fetchall()
    for row in rlist:
        cols=row
        for c in cols:
            print(c)
        print("--------------------")