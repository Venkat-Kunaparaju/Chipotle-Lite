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
    cursor.execute(commands.createProtein)
    cursor.execute(commands.createIngredient)
    cursor.execute(commands.createOrder)
    cursor.execute(commands.createCustomer)
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
    
    #Load customer data
    csvFile = "Data/Customers.csv"
    with open(csvFile, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            cursor.execute(commands.insertCustomer, [int(row[0]), row[1], int(row[2]), None])

            
        #Test customer data
        cursor.execute("SELECT * FROM Customer")
        for x in cursor:
            print(x)
        print("\n")

    #Load Protein data
    csvFile = "Data/Protein.csv"
    with open(csvFile, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            cursor.execute(commands.insertProtein, [row[0], int(row[1]), int(row[2]), int(row[3]), float(row[4]), float(row[5])])

            
        #Test Protein data
        cursor.execute("SELECT * FROM Protein")
        for x in cursor:
            print(x)
        print("\n")

    #Load Ingredient data
    csvFile = "Data/Ingredient.csv"
    with open(csvFile, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            cursor.execute(commands.insertIngredient, [row[0], int(row[1]), int(row[2]), int(row[3]), float(row[4]), float(row[5])])

            
        #Test Ingredient data
        cursor.execute("SELECT * FROM Ingredient")
        for x in cursor:
            print(x)
        print("\n")
    
    cursor.execute(commands.insertEmployeeIndex);
    cursor.execute(commands.insertCustomerIndex);
    cursor.execute(commands.insertProteinIndex);
    cursor.execute(commands.insertProteinIndex2);
    cursor.execute(commands.insertIngredientIndex);
    cursor.execute(commands.insertIngredientIndex2);
    #Stored Procedures
    cursor.execute("""
    CREATE PROCEDURE createOrder(IN customerID INT, IN orderID INT, IN name varchar(10))
    BEGIN
    DECLARE i integer;
    DECLARE j VARCHAR(255);
    DECLARE test cursor for (
        SELECT Employee_ID, Job FROM Employees WHERE Job = 'Server_on_the_line'
    );

    open test;
    loop_label: LOOP
        FETCH test into i, j;

        select 'CHECK';

        INSERT INTO User_Order(Order_ID, Customer_ID, Employee_ID, Name) VALUES(orderID, customerID, i, name);
        leave loop_label;
    END LOOP;
    END;
    """)

    cursor.execute("""
    CREATE PROCEDURE UpdateItem (IN given_name varchar(10), vol INT)
    BEGIN
    
    START TRANSACTION;  
    SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;  
    UPDATE Inventory SET Count = vol WHERE Name = given_name;
    UPDATE Ingredient SET Volume = vol WHERE Name = given_name;
    UPDATE Protein SET Volume = vol WHERE Name = given_name;
    COMMIT;
    END;
    """)
    
    cursor.execute("""
    CREATE PROCEDURE aggregateTotals(IN orderID INT, OUT fat1 INT, OUT calories1 INT)
    BEGIN
    DECLARE done int default FALSE;

    DECLARE i integer;
    DECLARE j integer;
    DECLARE test cursor for (
        select fat, calories from Ingredient_list natural join Ingredient WHERE Order_ID = orderID
        UNION ALL
        select fat, calories from Protein_list natural join Protein WHERE Order_ID = orderID
    );
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

   

    open test;
    SET fat1 = 0;
    SET calories1 = 0;
    loop_label: LOOP
        FETCH test into i, j;
        
        IF done THEN LEAVE loop_label;
        END IF;

        SET fat1 = fat1 + i;
        SET calories1 = calories1 + j;
       
    END LOOP;
    END;
    """)


