import mysql.connector
import SQLCommands as commands

mydb = mysql.connector.connect( # establish connection
    host="localhost",
    user="root",
    password='', #Edit password here to match user password
)


cursor = mydb.cursor(buffered=True)


#Check if database 'Chipotle-Lite' exists
cursor.execute("DROP DATABASE Chipotle_Lite")
cursor.execute("SHOW DATABASES") 

check = ""
for x in cursor:
    check += x[0];

#Create 'Chipotle' if it doesn't exist and load tables and data into it
if 'Chipotle_Lite' not in check:
    cursor.execute("Create DATABASE Chipotle_Lite")
    cursor.execute("USE Chipotle_Lite")
    