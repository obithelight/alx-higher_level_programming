#!/usr/bin/python3
"""Module that lists all states from mySQL database"""
import sys
import MySQLdb

if __name__ == "__main__":

  db = MySQLdb.connect(user="obi", passwd="", db="hbtn_0e_0_usa")
  cursor = db.cursor()
  cursor.execute("SELECT * FROM states")
  states = cursor.fetchall()

  for state in states:
    print(state)

  cursor.close()
  db.close()
