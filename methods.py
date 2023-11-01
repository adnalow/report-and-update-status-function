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





