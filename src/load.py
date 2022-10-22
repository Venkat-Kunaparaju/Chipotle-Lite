import mysql.connector
import SQLCommands as commands

mydb = mysql.connector.connect( # establish connection
    host="localhost",
    user="root",
    password='', #Edit password here to match user password
)


cursor = mydb.cursor(buffered=True)
cursor.execute("DROP DATABASE Chipotle_Lite") #Remove once done with initializing database

#Check if database 'Chipotle_Lite' exists
cursor.execute("SHOW DATABASES") 

check = ""
for x in cursor:
    check += x[0];

#Create 'Chipotle_Lite' if it doesn't exist and load tables and data into it
if 'Chipotle_Lite' not in check:
    cursor.execute("Create DATABASE Chipotle_Lite")
    cursor.execute("USE Chipotle_Lite")
    cursor.execute(commands.createInventory)
    cursor.execute(commands.createEmployees)
    cursor.execute(commands.createCustomer)
    cursor.execute(commands.createProtein)
    cursor.execute(commands.createIngredient)
    cursor.execute(commands.createOrder)
    cursor.execute(commands.createMenu)
    cursor.execute(commands.createProteinList)
    cursor.execute(commands.createIngredientList);