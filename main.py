import sqlite3
from methods import initialization
from methods import userReport

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


initialization()
userReport()


