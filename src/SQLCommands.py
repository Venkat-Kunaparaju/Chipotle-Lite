createInventory = """
    CREATE TABLE Inventory (
        Name VARCHAR(255), Count INT,
        PRIMARY KEY (Name)
    )
    """
insertInventory = """
    INSERT INTO INVENTORY(Name, Count) VALUES(%s, %s)
    """
createEmployees = """
    CREATE TABLE Employees (
        Employee_ID INT, Name VARCHAR(255), Salary INT,
        Job VARCHAR(255),
        PRIMARY KEY (Employee_ID)
    )
    """
insertEmployee = """
    INSERT INTO Employees(Employee_ID, Name, Salary, Job) VALUES(%s, %s, %s, %s)
    """
createCustomer = """
    CREATE TABLE Customer (
        Customer_ID INT, Name VARCHAR(255),
        Place_in_line INT, Order_ID INT,
        PRIMARY KEY (Customer_ID)
    ) 
    """
insertCustomer = """
    INSERT INTO Customer(Customer_ID, Name, Place_in_line, Order_ID) VALUES(%s, %s, %s, %s)
    """
createProtein = """
    CREATE TABLE Protein (
        Name VARCHAR(255), Volume INT, Calories INT,
        Fat INT, Price DOUBLE, Extra_price DOUBLE,
        PRIMARY KEY (Name)
    )   
    """
insertProtein = """
    INSERT INTO Protein(Name, Volume, Calories, Fat, Price, Extra_price) VALUES(%s, %s, %s, %s, %s, %s)
    """
createIngredient = """
    CREATE TABLE Ingredient (
        Name VARCHAR(255), Volume INT, Calories INT,
        Fat INT, Price DOUBLE, Extra_price DOUBLE,
        PRIMARY KEY (Name)
    )
    """
insertIngredient = """
    INSERT INTO Ingredient(Name, Volume, Calories, Fat, Price, Extra_price) VALUES(%s, %s, %s, %s, %s, %s)
    """
createOrder = """
    CREATE TABLE User_order (
        Order_ID INT, Customer_ID INT, Employee_ID INT,
        Name VARCHAR(255), Protein_list_ID INT, Ingredient_list_ID INT,
        PRIMARY KEY (Order_ID)
    )
    """
createProteinList = """
    CREATE TABLE Protein_list (
        Protein_list_ID INT, Name VARCHAR(255)
    )
    """
createIngredientList = """
    CREATE TABLE Ingredient_list (
        Ingredient_list_ID INT, Name VARCHAR(255)
    )
    """

