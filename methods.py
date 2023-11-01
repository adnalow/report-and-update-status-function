import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def initialization():
    def createReportTable():
        # Create a table if it does not exist
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS report
                        (ReportID INTEGER PRIMARY KEY AUTOINCREMENT, 
                        title TEXT, 
                        checklist TEXT, 
                        image_path TEXT, 
                        details TEXT, 
                        urgency TEXT,
                        status TEXT)
                    ''')

    def createStatusUpdate():
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS statusUpdates
                        (ReportID INTEGER PRIMARY KEY AUTOINCREMENT, 
                        status TEXT 
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
    
    title = input("Title for your report:")
    choice = input("Choose from any of the following [1]Robbery [2]Fire [3]Accident:")
    checklist = pre_defined_reports[int(choice)]()
    image_path = input("Enter image path: ")
    details = input("Enter details: ")
    urgency = input("Enter urgency level (Low, Medium, High): ")
    status = "pending"
    
    # Insert user input into the database
    cursor.execute("INSERT INTO report (title, checklist, image_path, details, urgency, status) VALUES (?, ?, ?, ?, ?, ?)",
               (title, checklist, image_path, details, urgency, status))

    
    
    cursor.execute("SELECT * FROM report")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    




