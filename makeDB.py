import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root", #your username here,
    passwd="asirwad@123",# your passowrd here
)


# create a curser obj
curserObject = database.cursor()

# create the db
curserObject.execute("CREATE DATABASE crm_app_db")

print("Database created!")