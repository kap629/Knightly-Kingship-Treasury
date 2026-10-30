import getpass

import mysql.connector
import matplotlib.pyplot as plt
from tabulate import tabulate

try:
    import config
except ImportError:
    print("config.py not found.")
    print("Copy config.example.py to config.py and fill in your MySQL and admin passwords.")
    raise SystemExit(1)

'''
    -------------------------KNIGHTLY KINGSHIP TREASURY--------------------------
                                   Welcome To Indian Sports Treasury
     A project developed by Advait,Kapish & Yuvraj for CS Board Practical
    -----------------------------------------------------------------------------------------------        '''


# ==========================================
# Helper: one place for the database connection
# ==========================================
def get_connection(use_database=True):
    """Return a MySQL connection using the details in config.py."""
    settings = {
        "host": config.DB_HOST,
        "user": config.DB_USER,
        "password": config.DB_PASSWORD,
        "charset": "utf8",
    }
    if use_database:
        settings["database"] = config.DB_NAME
    return mysql.connector.connect(**settings)


# ==========================================
# Function to create a new database
# ==========================================
def create_database():
    print("Function to create a database is starting...")
    # try to connect with MySQL server
    try:
        mydb = get_connection(use_database=False)
        print("Connection successful!")
    except Exception:
        print("Connection failed! Please check MySQL service.")
        return
    mycursor = mydb.cursor()
    dbname = input("Enter name of the database you want to make: ")
    try:
        # SQL query to create new database
        query = "CREATE DATABASE " + dbname + ";"
        print("Running query:", query)
        mycursor.execute(query)
        print("Database created successfully.")
    except Exception as e:
        print("Error occurred while creating database:", e)
        print("Maybe it already exists or the name is wrong.")
    finally:
        print("Closing connection...")
        mydb.close()
        print("----------------------------------")


# ==========================================
# Function to show all databases
# ==========================================
def show_databases():
    print("Showing all databases present in your MySQL...")
    try:
        mydb = get_connection(use_database=False)
        print("Connected successfully.")
    except Exception:
        print("Error connecting to MySQL.")
        return
    mycursor = mydb.cursor()
    try:
        mycursor.execute("SHOW DATABASES;")
        print("Query executed successfully.")
    except Exception:
        print("Could not execute query.")
        return
    data = mycursor.fetchall()
    print("All Databases are listed below:")
    for one in data:
        print(one)
    print("That's all the databases we have!")
    mydb.close()
    print("----------------------------------")


# ==========================================
# Function to create a table inside a database
# ==========================================
def create_table():
    print("Creating table now... please wait.")
    try:
        mydb = get_connection()
        print("Connected to database", config.DB_NAME + ".")
    except Exception:
        print("Could not connect to database! Maybe it does not exist.")
        return
    mycursor = mydb.cursor()
    query = """
    CREATE TABLE sports_data(
        sport VARCHAR(50) PRIMARY KEY,
        viewership_millions FLOAT,
        revenue_crores FLOAT,
        govt_support_crores FLOAT
    );
    """
    try:
        mycursor.execute(query)
        print("Table created successfully.")
    except Exception as e:
        print("Error while creating table:", e)
    finally:
        mydb.commit()
        mydb.close()
        print("----------------------------------")


# ==========================================
# Function to add records in the sports table
# ==========================================
def add_record():
    print("Now adding a new record into the table.")
    try:
        mydb = get_connection()
        print("Connected to database successfully.")
    except Exception:
        print("Connection failed!")
        return
    mycursor = mydb.cursor()
    try:
        sport = input("Enter the name of the sport: ")
        viewership = float(input("Enter viewership in millions: "))
        revenue = float(input("Enter revenue in crores: "))
        support = float(input("Enter govt support in crores: "))
        # Query to insert data
        query = "INSERT INTO sports_data (sport, viewership_millions, revenue_crores, govt_support_crores) VALUES (%s, %s, %s, %s);"
        data = (sport, viewership, revenue, support)
        print("Running insert query now...")
        mycursor.execute(query, data)
        mydb.commit()
        print("Record inserted successfully!")
    except Exception as e:
        print("Error while inserting data:", e)
    finally:
        print("Closing connection now.")
        mydb.close()
        print("----------------------------------")


# ==========================================
# Function to add records in the awards table
# ==========================================
def add_awards():
    print("Now adding awards detail into the table.")
    try:
        mydb = get_connection()
        print("Connected to database successfully.")
    except Exception:
        print("Connection failed!")
        return
    mycursor = mydb.cursor()
    try:
        sport = input("Enter the name of the sport: ")
        playername = input("Enter player name:  ")
        year = input("Enter the year: ")
        award_name = input("Enter the name of the award given: ")
        # Query to insert data
        query = "INSERT INTO best_player (sport, player_name, year, award) VALUES (%s, %s, %s, %s);"
        data = (sport, playername, year, award_name)
        print("Running insert query now...")
        mycursor.execute(query, data)
        mydb.commit()
        print("Record inserted successfully!")
    except Exception as e:
        print("Error while inserting data:", e)
    finally:
        print("Closing connection now.")
        mydb.close()
        print("----------------------------------")


# ==========================================
# Function to view all data in sport table
# ==========================================
def view_all_data():
    print("Opening database to show all data from table.")
    try:
        mydb = get_connection()
    except Exception:
        print("Could not connect to the database.")
        return
    mycursor = mydb.cursor()
    try:
        mycursor.execute("SELECT * FROM sports_data;")
        print("Query executed successfully!")
    except Exception as e:
        print("Error:", e)
        return
    records = mycursor.fetchall()
    print("All Records Present in Table:")
    for row in records:
        print(row)
    print("End of data.")
    mydb.close()
    print("----------------------------------")


# ==========================================
# Function to view all data in Awards table
# ==========================================
def view_all_awards():
    print("---------------------------------------------------------------")
    print("Opening database to show all data from table.")
    try:
        mydb = get_connection()
    except Exception:
        print("Could not connect to the database.")
        return
    mycursor = mydb.cursor()
    try:
        mycursor.execute("SELECT * FROM best_player;")
        print("Query executed successfully!")
    except Exception as e:
        print("Error:", e)
        return
    records = mycursor.fetchall()
    print("All Records Present in  Awards Table:")
    for row in records:
        print(row)
    print("End of data.")
    mydb.close()
    print("----------------------------------")


# ==========================================
# Function to search for one record in Sports table
# ==========================================
def search_record():
    print("Searching for a record now...")
    try:
        mydb = get_connection()
    except Exception:
        print("Could not connect to the database.")
        return
    mycursor = mydb.cursor()
    sport_name = input("Enter sport name to search: ")
    try:
        query = "SELECT * FROM sports_data WHERE sport = %s;"
        mycursor.execute(query, (sport_name,))
        result = mycursor.fetchall()
        if result:
            print("Record found!!")
            for row in result:
                print(row)
        else:
            print("No record found for the given sport.")
    except Exception as e:
        print("Error during search:", e)
    finally:
        mydb.close()
        print("----------------------------------")


# ==========================================
# Function to delete a record in sports table
# ==========================================
def delete_record():
    print("Now deleting a record (if exists).")
    try:
        mydb = get_connection()
    except Exception:
        print("Could not connect.")
        return
    mycursor = mydb.cursor()
    sport_name = input("Enter sport name to delete: ")
    try:
        query = "DELETE FROM sports_data WHERE sport = %s;"
        mycursor.execute(query, (sport_name,))
        mydb.commit()
        if mycursor.rowcount > 0:
            print("Record deleted successfully.")
        else:
            print("No such record found.")
    except Exception as e:
        print("Error while deleting:", e)
    finally:
        mydb.close()
        print("----------------------------------")


# ==========================================
# Function to update a record in sports table
# ==========================================
def update_record():
    print("Updating existing record...")
    try:
        mydb = get_connection()
    except Exception:
        print("Cannot connect to database.")
        return
    mycursor = mydb.cursor()
    sport_name = input("Enter sport name to update: ")
    try:
        new_rev = float(input("Enter new revenue in crores: "))
        query = "UPDATE sports_data SET revenue_crores = %s WHERE sport = %s;"
        mycursor.execute(query, (new_rev, sport_name))
        mydb.commit()
        if mycursor.rowcount > 0:
            print("Record updated successfully!")
        else:
            print("No such sport found.")
    except Exception as e:
        print("Error while updating:", e)
    finally:
        mydb.close()
        print("----------------------------------")


# ===========================================
# GRAPH FUNCTIONS
# ============================================
def padma_shri():
    try:
        mydb = get_connection()
    except Exception:
        print("Cannot connect to database.")
        return
    mycursor = mydb.cursor()
    try:
        mycursor.execute("SELECT * FROM best_player where award like 'Padma Shri';")
        print("Query executed successfully!")
    except Exception as e:
        print("Error:", e)
        return
    records = mycursor.fetchall()
    print("List of players awarded Padma Shri")
    t = []
    for i in records:
        t.append([i[0], i[1], i[2]])
    headers = ["Sport name", "Name of the Player", "Year"]
    table = tabulate(t, headers, tablefmt="grid", maxcolwidths=[20, 30, None])
    print("Tabular Data")
    print(table)
    mydb.close()


# ===========================================
# GRAPH FUNCTIONS for Revenue
# ============================================
def plot_revenue():
    try:
        mydb = get_connection()
    except Exception:
        print("Cannot connect to database.")
        return
    mycursor = mydb.cursor()
    try:
        mycursor.execute("SELECT * FROM sports_data;")
        print("Query executed successfully!")
    except Exception as e:
        print("Error:", e)
        return
    records = mycursor.fetchall()
    sports = []
    revenue = []
    for row in records:
        sports.append(row[0])
        revenue.append(row[2])
    plt.bar(sports, revenue, color="skyblue")
    plt.xlabel("Sports")
    plt.ylabel("Revenue (in crores)")
    plt.title("Revenue Potential by Sport")
    plt.xticks(rotation=45)
    plt.show()
    mydb.close()
    print("----------------------------------")


# ===========================================
# GRAPH FUNCTIONS for Viewership Popularity
# ============================================
def plot_popularity():
    try:
        mydb = get_connection()
    except Exception:
        print("Cannot connect to database.")
        return
    mycursor = mydb.cursor()
    try:
        mycursor.execute("SELECT * FROM sports_data;")
        print("Query executed successfully!")
    except Exception as e:
        print("Error:", e)
        return
    records = mycursor.fetchall()
    sports = []
    viewers = []
    for row in records:
        sports.append(row[0])
        viewers.append(row[1])
    plt.plot(sports, viewers, marker="o", color="green")
    plt.xlabel("Sports")
    plt.ylabel("Viewership (in millions)")
    plt.title("Popularity of Sports")
    plt.xticks(rotation=45)
    plt.show()
    mydb.close()
    print("----------------------------------")


# ===========================================
# GRAPH FUNCTIONS for Govt Funds given to Sports
# ============================================
def plot_govt_support():
    try:
        mydb = get_connection()
    except Exception:
        print("Cannot connect to database.")
        return
    mycursor = mydb.cursor()
    try:
        mycursor.execute("SELECT * FROM sports_data;")
        print("Query executed successfully!")
    except Exception as e:
        print("Error:", e)
        return
    records = mycursor.fetchall()
    sports = []
    govt_aid = []
    for row in records:
        sports.append(row[0])
        govt_aid.append(row[3])
    plt.bar(sports, govt_aid, color="orange")
    plt.xlabel("Sports")
    plt.ylabel("Govt. Support Funds in crores")
    plt.title("Govt. Support Funds for Sports")
    plt.xticks(rotation=45)
    plt.show()
    mydb.close()
    print("----------------------------------")


# =================================================================
# GRAPH FUNCTIONS  to show comparion of revenue & govt. funds provided
# =================================================================
def plot_comparison():
    try:
        mydb = get_connection()
    except Exception:
        print("Cannot connect to database.")
        return
    mycursor = mydb.cursor()
    try:
        mycursor.execute("SELECT * FROM sports_data;")
        print("Query executed successfully!")
    except Exception as e:
        print("Error:", e)
        return
    records = mycursor.fetchall()
    sports = []
    popularity = []
    revenue = []
    govt_aid = []
    for row in records:
        sports.append(row[0])
        popularity.append(row[1])
        revenue.append(row[2])
        govt_aid.append(row[3])
    x = range(len(sports))
    plt.bar([i - 0.2 for i in x], revenue, width=0.2, label="Revenue")
    plt.bar([i + 0.2 for i in x], govt_aid, width=0.2, label="Govt. Support Funds")
    plt.xlabel("Sports")
    plt.ylabel("Values (in crores)")
    plt.title("Sports Potential Comparison")
    plt.xticks(x, sports, rotation=45)
    plt.legend()
    plt.show()
    mydb.close()


# ===========================================
# User Side Menu
# ============================================
def user_side():
    while True:
        print("\n----------------------------------")
        print("WELCOME TO USER")
        print("----------------------------------")
        print("1. Plot Revenue Graph ")
        print("2. Plot Popularity Graph ")
        print("3. Plot Govt. Support Funds Graph ")
        print("4. Comparision of Revenue & Govt. Support Funds   ")
        print("5. List of players awarded Padma Shri Award")
        print("6. Exit choice")
        choice = int(input("Enter your choice number: "))
        if choice == 1:
            plot_revenue()
        elif choice == 2:
            plot_popularity()
        elif choice == 3:
            plot_govt_support()
        elif choice == 4:
            plot_comparison()
        elif choice == 5:
            padma_shri()
        elif choice == 6:
            print("Thanks for using this option.")
            break
        else:
            print("Wrong choice! Please enter again.")


# ===========================================
# Admin Side Menu
# ============================================
def admin_side():
    while True:
        print("\n----------------------------------")
        print("WELCOME TO ADMIN")
        print("----------------------------------")
        # print("1. Create Database")
        # print("2. Show Databases")
        # print("3. Create Table")
        print("1. Add Record in Sports Data")
        print("2. Add Records about Awards")
        print("3. View All Data of Games")
        print("4. View All Data of Awards")
        print("5. Search Record")
        print("6. Delete Record")
        print("7. Update Record")
        print("8. Exit Program")
        print("----------------------------------")
        try:
            choice = int(input("Enter your choice number: "))
        except Exception:
            print("Invalid input! Please enter a number.")
            continue
        if choice == 1:
            add_record()
        elif choice == 2:
            add_awards()
        elif choice == 3:
            view_all_data()
        elif choice == 4:
            view_all_awards()
        elif choice == 5:
            search_record()
        elif choice == 6:
            delete_record()
        elif choice == 7:
            update_record()
        elif choice == 8:
            print("Thanks for using this option.")
            break
        else:
            print("Wrong choice! Please enter again.")


# ==========================================
# MAIN MENU SECTION
# ==========================================
def main_menu():
    while True:
        print("\n--------------------------KNIGHTLY KINGSHIP TREASURY----------------------")
        print("                                Welcome To Indian Sports Treasury                               ")
        print(" A project developed by Advait,Kapish & Yuvraj for CS Board Practical")
        print("---------------------------------------------------------------------------------------------")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        ch = int(input("enter your choice"))
        if ch == 1:
            # getpass hides the typed password (it shows nothing while typing)
            p = getpass.getpass("Enter the password")
            if p == config.ADMIN_PASSWORD:
                admin_side()
            else:
                print("Incorrect Password")
        elif ch == 2:
            user_side()
        elif ch == 3:
            print("Thanks for using this program. Bye!")
            break
        else:
            print("Wrong choice! Please enter again.")


main_menu()
