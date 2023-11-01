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

    conn.commit()
    
    
def printReport():
    # Define the reportId you want to retrieve
        inquireReportID = input("Insert The ReportId that you want to see: ")

        # Fetch the row with reportId equal to user input using a WHERE clause
        cursor.execute("SELECT * FROM report WHERE reportId=?", (inquireReportID,))
        row = cursor.fetchone()

        # Check if a row was found
        if row:
            print("ReportId:", row[0])  
            print("Title:", row[1])  
            print("Checklist:", row[2])
            print("image_path:", row[3])
            print("details:", row[4])
            print("urgency:", row[5])
            print("status:", row[6])
            
        else:
            print("No row found with ReportId =", inquireReportID)
            
def statusUpdate():
    def status1():
        return "Preparing to deploy"
    
    def status2():
        return "On the Process"
    
    def status3():
        return "Resolved"
    
    
    pre_defined_status ={
        1: status1,
        2: status2,
        3: status3,
    }
    
    choice = input("Enter the new status: [1]Preparing to deploy [2]On the Process [3]Resolved: ")
    newStatus = pre_defined_status[int(choice)]()
    whereReportID = input("Enter the reportID of the incident:")

    # Update the status for the specific reportId using a WHERE clause
    cursor.execute("UPDATE report SET status=? WHERE reportId=?", (newStatus, whereReportID))

    # Commit the changes to the database
    conn.commit()

    
    




