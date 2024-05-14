'''
File: Database Communicator
Project: Telegram Bot LHQS Fridge Alert System
Developer: Abby Peterson
Purpose: 
'''
import os
import sqlite3

FILENAME = "telegram_info" # the database that will create a table we are saving values to
TABLE1NAME = "member_info" # for telegram users to sign up for fridge bot information
TABLE2NAME = "fridge_details" # for telegram bot to access/store fridge log information

#Set up member and fridge table keys (columns)
# member: ID (int), username (str), name (str), date_assigned, alerts (0 or 1)
keys1_init = "(userid text, name text, date_assg text, alerts integer)"
keys1_string = "userid, name, date_assg, alerts"
# fridge: order (int), date, time , location (str), value (float), error (str)
keys2_init = "(ordering integer, date text, time text, loc text, val float, error string)"
keys2_string = "ordering, date, time, loc, val, error"

def prep(filename):
    # Construct the full path to the database file
    db_path = os.path.join(os.path.dirname(__file__), filename + ".db")
    # Standard read/write connection
    conn = sqlite3.connect(db_path)
    # Create a cursor object
    this_curs = conn.cursor()  # can browse database using cursor methods
    return this_curs

def create_tables():
    curs = prep(FILENAME)

    #Create tables
    curs.execute(f"CREATE TABLE IF NOT EXISTS {TABLE1NAME} {keys1_init}") # makes user table
    curs.execute(f"CREATE TABLE IF NOT EXISTS {TABLE2NAME} {keys2_init}") # makes fridge table

def delete_table(table_name):
    curs = prep(FILENAME)
    curs.execute(f"DROP TABLE {table_name}")

def add_member():
    curs = prep(FILENAME)
    #TEST - add my telegram account to the list
    values_string = "(\"boop1328\",\"Boop\",\"2024-02-20\",1)" #TODO: should come from param instead^
    curs.execute(f"INSERT INTO {TABLE1NAME}({keys1_string}) VALUES {values_string}") # SQLite command
    curs.execute("COMMIT") # SQLite command to saved the newly updated database

def alert_choice(member, status):
    member = "Abby"
    status = 1 # 1: on, get alerts - 0: off, no more alerts
    curs = prep(FILENAME)
    curs.execute(f"UPDATE {TABLE1NAME} SET alerts = {status} WHERE name = \"{member}\"") # for /alertson..off
    curs.execute("COMMIT")

def isMember(userid):
    return True