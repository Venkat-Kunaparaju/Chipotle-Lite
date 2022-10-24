import mysql.connector
import SQLCommands as commands
import csv

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

    #Load inventory data
    csvFile = "Data/Inventory.csv"
    with open(csvFile, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            cursor.execute(commands.insertInventory, [row[0], int(row[1])])

            
        #Test inventory data
        cursor.execute("SELECT * FROM Inventory")
        for x in cursor:
            print(x)
        print("\n")
        
    #Load employee data
    csvFile = "Data/Employees.csv"
    with open(csvFile, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            cursor.execute(commands.insertEmployee, [int(row[0]), row[1], int(row[2]), row[3]])

            
        #Test employee data
        cursor.execute("SELECT * FROM Employees")
        for x in cursor:
            print(x)
        print("\n")
    

