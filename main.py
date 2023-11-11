import mysql.connector
from methods import initialization, userReport, printReport, statusUpdate

host = "112.198.173.169"
user = "root"
password = "incidentreportingapp"
database = "reportingApp"

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "incidentreportingapp",
    database = "reportingApp"
    )

cursor = db.cursor()


initialization()
choice = input("Do you want to report something?y/n")

while choice == 'y':
    userReport()
    choice = input("\nDo you want to report something?y/n")

def printAllReport():
    cursor.execute("SELECT * FROM report")
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]

    for row in rows:
        for i in range(len(column_names)):
            print(f"{column_names[i]}: {row[i]}")
        print("---")

choice = input("Do you want to update the status of a report?[y/n]:")

while choice == 'y':
    statusUpdate()
    choice = input("\nDo you want to update the status of a report?[y/n]:")

printReport()

choice = input("Do you want to see all the report[y/n]:")

while choice == 'y':
    printAllReport()
    choice = input("\nDo you want to see all the report[y/n]:")
