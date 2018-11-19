import json

import mysql.connector


def showDB():
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x[0])


def showTables():
    mycursor = mydb.cursor()
    mycursor.execute("SHOW tables")
    for x in mycursor:
        print(x[0])


def selectAll(tablename):
    mycursor = mydb.cursor()
    query = "SELECT * FROM " + tablename
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


if __name__ == '__main__':
    configsFile = open('./config.json', 'r')
    config = json.load(configsFile)

    mydb = mysql.connector.connect(
        host=config["host"],
        user=config["username"],
        passwd=config["password"],
        database=config["database"]
    )

    # showDB()
    # showTables()
    selectAll(config["tablename"])