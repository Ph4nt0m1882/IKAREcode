import sqlite3, os
dir=os.path.dirname(os.path.abspath(__file__))

conn=sqlite3.connect('https://github.com/Ph4nt0m1882/IKAREcode/blob/main/AsDBCoIn.db')
cur=conn.cursor()
conn.close()
