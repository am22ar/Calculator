import mysql.connector

mydb = mysql.connector.connect(host="localhost", username="root", password="")

mycursor = mydb.cursor()

mycursor.execute("drop database if exists amar")
print("database deleted")

mycursor.execute("create database amar")
print("database created")