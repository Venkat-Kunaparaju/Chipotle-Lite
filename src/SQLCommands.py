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
createCustomer = """
    CREATE TABLE Customer (
        Customer_ID INT, Name VARCHAR(255),
        Place_in_line INT, Order_ID INT,
        PRIMARY KEY (Customer_ID)
    ) 
    """
createProtein = """
    CREATE TABLE Protein (
        Name VARCHAR(255), Volume INT, Calories INT,
        Fat INT, Price INT, Extra_price INT,
        PRIMARY KEY (Name)
    )
    """
createIngredient = """
    CREATE TABLE Ingredient (
        Name VARCHAR(255), Volume INT, Calories INT,
        Fat INT, Price INT, Extra_price INT,
        PRIMARY KEY (Name)
    )
    """
createOrder = """
    CREATE TABLE User_order (
        Order_ID INT, Customer_ID INT, Employee_ID INT,
        Name VARCHAR(255), Protein_list_ID INT, Ingredient_list_ID INT,
        PRIMARY KEY (Order_ID)
    )
    """
createMenu = """
    CREATE TABLE Menu (
        Name VARCHAR(255), Protein_list_ID INT, Ingredient_list_ID INT,
        PRIMARY KEY (NAME)
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

