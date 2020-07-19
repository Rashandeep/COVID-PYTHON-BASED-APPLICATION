#IMPORT FOR DATABASE CONNECTION
import sqlite3

# MAKING THE CONNECTION TO DATABASE
conn=sqlite3.connect('covid.sqlite')
cur=conn.cursor()
