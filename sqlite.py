import sqlite3

def createDatabase():
    conn = sqlite3.connect('database_name.db')
    cursor = conn.cursor()

    # Create a table if it does not exist
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS reports
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    title TEXT, 
                    checklist TEXT, 
                    image_path TEXT, 
                    details TEXT, 
                    urgency TEXT)
                ''')

    # Insert data into the table
    reports_data = [
        ("Report Title 1", "Robbery", "robbery.jpg", "Additional details about the incident.", "High"),
        ("Report Title 2", "Fire", "fire.jpg", "Additional details about the incident.", "High")
    ]

    cursor.executemany("INSERT INTO reports (title, checklist, image_path, details, urgency) VALUES (?, ?, ?, ?, ?)",
                    reports_data)

    # Commit the changes
    conn.commit()

    # Query to retrieve reports with a specific checklist item
    cursor.execute("SELECT * FROM reports WHERE checklist=?", ("Fire",))
    rows = cursor.fetchall()
    
    return rows

def main():
    rows = createDatabase()
    for row in rows:
        print(row)

# Call the main function to execute your code
main()

import sqlite3

# Connect to the database
conn = sqlite3.connect('database_name.db')
cursor = conn.cursor()

# Get user input
title = input("Enter report title: ")
checklist = input("Enter checklist item: ")
image_path = input("Enter image path: ")
details = input("Enter details: ")
urgency = input("Enter urgency level (Low, Medium, High): ")

# Insert user input into the database
cursor.execute("INSERT INTO reports (title, checklist, image_path, details, urgency) VALUES (?, ?, ?, ?, ?, ?)",
               (title, checklist, image_path, details, urgency, status))

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Data inserted successfully.")
