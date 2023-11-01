import sqlite3
import random

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def initialization():
    def createReportTable():
        # Create a table if it does not exist
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS report (
                    ReportID INTEGER PRIMARY KEY,
                    title TEXT,
                    checklist TEXT,
                    image_path TEXT,
                    details TEXT,
                    urgency TEXT,
                    status TEXT)
                    ''')

    def createStatusUpdate():
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS statusUpdate (
                ReportID INTEGER,
                title TEXT,
                status TEXT,
                FOREIGN KEY (ReportID) REFERENCES report(ReportID)
            )
        ''')

    
    createReportTable()
    createStatusUpdate()




def userReport():
    def report1():
        return "Robbery"
    
    def report2():
        return "Fire"
    
    def report3():
        return "Accident"
    
    
    pre_defined_reports ={
        1: report1,
        2: report2,
        3: report3,
    }
    
    reportID = random.randint(10, 999)
    title = input("Title for your report:")
    choice = input("Choose from any of the following [1]Robbery [2]Fire [3]Accident:")
    checklist = pre_defined_reports[int(choice)]()
    image_path = input("Enter image path: ")
    details = input("Enter details: ")
    urgency = input("Enter urgency level (Low, Medium, High): ")
    status = "pending"
    
    # Insert user input into the database
    cursor.execute("INSERT INTO report (reportID, title, checklist, image_path, details, urgency, status) VALUES (?, ?, ?, ?, ?, ?, ?)",
               (reportID, title, checklist, image_path, details, urgency, status))
    
    cursor.execute("INSERT INTO statusUpdate (reportID, title, status) VALUES (?, ?, ?)",
               (reportID, title, status))

    
    def printReport():
        cursor.execute("SELECT * FROM report")
        rows = cursor.fetchall()
        
        for row in rows:
            print(row)
            
    def printStatusUpdate():
        cursor.execute("SELECT * FROM statusUpdate")
        rows = cursor.fetchall()
        
        for row in rows:
            print(row)
    
    printReport()
    printStatusUpdate()




