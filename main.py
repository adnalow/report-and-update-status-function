import sqlite3
from methods import initialization
from methods import userReport
from methods import printReport
from methods import statusUpdate


conn = sqlite3.connect('database.db')
cursor = conn.cursor()


initialization()
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


choice = input("Do you want to report something?y/n")

while choice == 'y':
    userReport()
    choice = input("\nDo you want to report something?y/n")


printReport()
printAllReport()
