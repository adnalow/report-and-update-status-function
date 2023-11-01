import sqlite3
from methods import initialization

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


initialization()