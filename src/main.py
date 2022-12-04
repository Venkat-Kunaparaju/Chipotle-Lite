
from load import *
from setup import *
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk

welcome = Tk()

place_in_line = 4
customer_id = 4
order_id = 1

order_name = ""
items = [] #List of items chosen by user


def update():
    sql1 =  "select name from inventory where name = %s"
    cursor.execute(sql1, [x1.get()])
    result = cursor.fetchall()
    if result:
        temp = "UPDATE inventory SET Count = %s WHERE name = %s"
        cursor.execute(temp, [x2.get(), x1.get()])
        cursor.execute("SELECT * FROM inventory")
        result = cursor.fetchall()

        


def createOrder():
    #z1 is list of all the ingredients and proteins that the user selected
    #z2 is the type of order (bowl, tacos, etc.)
    return



def C_Inven():
    inven = Tk()
    inven.geometry("400x300")

    Label(inven, text="Name of Inventory").place(x=10, y=50)

    global x1
    x1 = Entry(inven)
    x1.place(x=140, y=50)

    global x2
    Label(inven, text="No. of Units").place(x=10, y=100)
    x2 = Entry(inven)
    x2.place(x=140, y=100)

    Button(inven, text="Confirm", height=3, width=13, command=update).place(x=140, y=150)


def Employee_Login():
    # variables for name and employee_id
    global e1
    global e2

    # create login page
    root = Tk()
    root.geometry("400x300")
    root.title("Employee Login Page")

    Label(root, text="Username").place(x=10, y=50)

    e1 = Entry(root)
    e1.place(x=140, y=50)

    Label(root, text="Employee ID").place(x=10, y=100)
    e2 = Entry(root)
    e2.place(x=140, y=100)
    e2.config(show="*")

    Button(root, text="Login", command=E_Main, height=3, width=13).place(x=140, y=150)

def Customer_Login():
    
    global cname

    # create login page
    root = Tk()
    root.geometry("400x300")
    root.title("Customer Login Page")

    Label(root, text="Username").place(x=10, y=50)

    cname = Entry(root)
    cname.place(x=140, y=50)

    Button(root, text="Enter", command=C_Main, height=3, width=13).place(x=140, y=150)

def getOrderType():
    global order_name
    order_name = clicked.get()
    
def updateItemList():
    global items
    temp_items = clicked2.get()
    items.append(temp_items)
    temp_items += ","
    hold.config(state='normal')
    hold.insert('end', temp_items)
    hold.config(state='disabled')

def C_Main():
    global customer_id
    global place_in_line

    name = cname.get()
    temp = "INSERT INTO Customer (Customer_ID, Name, Place_in_line, Order_ID) Values (%s, %s, %s, %s)"
    cursor.execute(temp, [customer_id, name, place_in_line, None])
    customer_id += 1
    place_in_line += 1

    #CREATE create order page 
    toplevel1 = tk.Tk()
    toplevel1.configure(height=450, width=600)

    #hold = Text of the stuff user has selected
    global hold
    hold = Text(toplevel1, width = 100, height = 50)
    hold.place(x=0, y=350)
    hold.config(state='disabled')

    #Text for item lsit
    label5 = ttk.Label(toplevel1)
    label5.configure(background="light green", text="Item List", anchor='c')
    label5.place(height=30, width=400, x=75, y=300)

    #List of items with price
    trv = ttk.Treeview(toplevel1, selectmode='browse')
    trv.place(x=10, y=50)
    # number of columns
    trv["columns"] = ("1", "2")

    # Defining heading
    trv['show'] = 'headings'

    # width of columns and alignment
    trv.column("1", width=100, anchor='c')
    trv.column("2", width=50, anchor='c')

    # Headings
    # respective columns
    trv.heading("1", text="Name")
    trv.heading("2", text="Price")

    # getting data from MySQL student table
    cursor.execute("SELECT Name, Price FROM Protein")
    row = cursor.fetchall()
    for y in row:
        trv.insert('', 'end', values=y)
    
    # getting data from MySQL student table
    cursor.execute("SELECT Name, Price FROM Ingredient")
    row = cursor.fetchall()
    for y in row:
        trv.insert('', 'end', values=y)

    #Button for confirming
    button3 = ttk.Button(toplevel1)
    button3.configure(text='Place Order' , command=displayOrder)
    button3.place(
        height=75,
        relwidth=0.0,
        relx=0.0,
        rely=0.0,
        width=75,
        x=500,
        y=400)

    #Dropdown for order type
    global clicked
    clicked = StringVar(toplevel1)
    clicked.set("Bowl")
    
    drop = OptionMenu( toplevel1 , clicked , "Bowl", "Burrito", "Tacos")
    drop.place(x= 250, y = 50)

    button = Button(toplevel1, text="Confirm Choice", command=getOrderType)
    button.place(x=225, y=100)

    global clicked2
    options = []
    cursor.execute("select name from Protein")
    for x in cursor:
        options.append(x[0])
    cursor.execute("select name from Ingredient")
    for x in cursor:
        options.append(x[0])
    
    clicked2 = StringVar(toplevel1)
    clicked2.set(options[0])

    drop = OptionMenu(toplevel1, clicked2, *options)
    drop.place(x=250, y=150)

    button = Button(toplevel1, text="Confirm Ingredient", command=updateItemList)
    button.place(x=225, y=200)

def displayOrder():

    #Create a stored procedure for creating a order from the customer, employee, and the two ingredient list and protein list tables created
    #Returns the created order id

    #Create ingredient_list and protein list
    global order_id
    global order_name
    global items
    global hold
    all_ingredients = []
    all_proteins = []
    cursor.execute("Select Name from Ingredient")
    for x in cursor:
        all_ingredients.append(x[0])
    
    cursor.execute("Select Name from Protein")
    for x in cursor:
        all_proteins.append(x[0])

    for x in items:
        if x in all_proteins:
            cursor.execute("INSERT INTO Protein_LIST(Order_ID, Name) Values (%s, %s)", [order_id, x])
        if x in all_ingredients:
            cursor.execute("INSERT INTO Ingredient_LIST(Order_ID, Name) Values (%s, %s)", [order_id, x])

    #Call sotred procedures
    #create order
    cursor.callproc("createOrder", [customer_id-1, order_id, order_name])

    #get fat and calorie totals
    args = [order_id, 0, 0]
    result_args = cursor.callproc("aggregateTotals", args)

    fat_total = result_args[1]
    calorie_total = result_args[2]

    #get total price
    name_price = {}
    count = []
    cursor.execute("""
    select name, price, extra_price from Ingredient_list natural join Ingredient WHERE Order_ID = %s
        UNION ALL
    select name, price, extra_price from Protein_list natural join Protein WHERE Order_ID = %s
    """, [order_id, order_id])
   
    for x in cursor:
        if x[0] not in name_price:
            name_price[x[0]] = [x[1], x[2], 1]
        else:
            name_price[x[0]][2] += 1
    total_price = 0
    for x in name_price:
        total_price += (name_price[x][2]-1) * name_price[x][1] + name_price[x][0]


    
    #CREATE create order page 
    toplevel1 = tk.Tk()
    toplevel1.configure(height=200, width=400)

    #hold = Text of the stuff user has selected
    temp = ""
    order = "Server: "
    cursor.execute("SELECT e.Name, u.name, u.Order_id FROM User_Order u Join Employees e ON e.Employee_Id = u.Employee_ID WHERE u.Order_id = %s", [order_id])
    for x in cursor:
        order += x[0]
        temp = x[1]
        break
    order += "\n"
    order += "Order Type: " + temp + "\n"

    order += "Ingredients: "
    count = 0
    for x in range(len(items)):
        order += items[x]
        if x != len(items) - 1:
            order += ", "
        count += 1
        if count == 4:
            order += "\n"

    order += "\n"
    order += "Price: " + str(total_price) + "\n"
    order += "Fat: " + str(fat_total) + "\n"
    order += "Calories: " + str(calorie_total) + "\n"
    
    
    hold2 = Text(toplevel1, width = 100, height = 50)
    hold2.place(x=0, y=100)
    hold2.insert('end', order)
    hold2.config(state='disabled')

 
    # Create label
    l = Label(toplevel1, text = "Thank You For Your Order!\n Here Is Your Summary!")
    l.config(font =("Courier", 14))
    l.place(x=50, y=20)

    items.clear()
    order_name = ""
    order_id += 1
    hold.config(state='normal')
    hold.delete(1.0, END)

def E_Main():
    name = e1.get()
    Employee_ID = e2.get()

    sql = "select * from employees where name = %s and Employee_id = %s"
    cursor.execute(sql, [name, Employee_ID])
    result = cursor.fetchall()
    if result:

        toplevel1 = tk.Tk()
        toplevel1.configure(height=1000, width=1000)

        label3 = ttk.Label(toplevel1)
        label3.configure(background="light green", text=Employee_ID, anchor='c')
        label3.place(height=60, relx=0.0, rely=0.0, width=250, x=600, y=115)
        label4 = ttk.Label(toplevel1)
        label4.configure(background="light green", text=name, anchor='c')
        label4.place(height=100, width=400, x=75, y=75)
        message2 = tk.Message(toplevel1)
        message2.configure(background="yellow", text='E.ID', anchor='c')
        message2.place(height=20, width=250, x=600, y=75)
        button3 = ttk.Button(toplevel1)
        button3.configure(text='Exit')
        button3.place(
            height=75,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=150,
            x=700,
            y=850)
        separator1 = ttk.Separator(toplevel1)
        separator1.configure(orient="horizontal")
        separator1.place(anchor="nw", height=5, width=1000, x=0, y=800)
        separator2 = ttk.Separator(toplevel1)
        separator2.configure(orient="horizontal")
        separator2.place(height=5, width=1000, x=0, y=200)
        button2 = ttk.Button(toplevel1)
        button2.configure(text="Change Inventory", command= C_Inven)
        button2.place(
            height=75,
            relwidth=0.0,
            relx=0.0,
            rely=0.0,
            width=150,
            x=75,
            y=850)

        trv = ttk.Treeview(toplevel1, selectmode='browse')
        label5 = ttk.Label(toplevel1)
        label5.configure(background="light green", text="Inventroy List", anchor='c')
        label5.place(height=100, width=400, x=75, y=250)
        trv.place(x=75, y=350)
        # number of columns
        trv["columns"] = ("1", "2")

        # Defining heading
        trv['show'] = 'headings'

        # width of columns and alignment
        trv.column("1", width=199, anchor='c')
        trv.column("2", width=199, anchor='c')

        # Headings
        # respective columns
        trv.heading("1", text="Name")
        trv.heading("2", text="Count")

        # getting data from MySQL student table
        cursor.execute("SELECT Name, Count FROM inventory")
        row = cursor.fetchall()
        for y in row:
            trv.insert('', 'end', values=y)


    else:

        return False


welcome.geometry("400x300")
welcome.title("Welcome to ChipChip")
cbutton = tk.Button(welcome, text="Customer Login", command=Customer_Login, height=3, width=13).place(x=75, y=50)
button = tk.Button(welcome, text="Employee Login", command=Employee_Login, height=3, width=13).place(x=75, y=150)

welcome.mainloop()

