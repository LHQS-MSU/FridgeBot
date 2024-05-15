'''
File: Database Communicator
Project: Telegram Bot LHQS Fridge Alert System
Developer: Abby Peterson
Purpose: 
'''
import os
import sqlite3
from datetime import datetime

FILENAME = "telegram_info" # the database that will create a table we are saving values to
TABLE1NAME = "member_info" # for telegram users to sign up for fridge bot information
TABLE2NAME = "fridge_details" # for telegram bot to access/store fridge log information

#Set up member and fridge table keys (columns)
# member: ID (int), username (str), name (str), date_assigned, alerts (0 or 1)
KEYS1_INIT = "(userid text, name text, date_assg text, alerts integer)"
KEYS1_STRING = "userid, name, date_assg, alerts"
# fridge: order (int), date, time , location (str), value (float), error (str)
KEYS2_INIT = "(ordering integer, date text, time text, loc text, val float, error string)"
KEYS2_STRING = "ordering, date, time, loc, val, error"

def prep(filename):
    '''FILLER'''
    # Construct the full path to the database file
    db_path = os.path.join(os.path.dirname(__file__), filename + ".db")
    # Standard read/write connection
    conn = sqlite3.connect(db_path)
    # Create a cursor object
    this_curs = conn.cursor()  # can browse database using cursor methods
    return this_curs

def create_tables():
    '''FILLER'''
    curs = prep(FILENAME)

    #Create tables
    curs.execute(f"CREATE TABLE IF NOT EXISTS {TABLE1NAME} {KEYS1_INIT}") # makes user table
    curs.execute(f"CREATE TABLE IF NOT EXISTS {TABLE2NAME} {KEYS2_INIT}") # makes fridge table

def delete_table(table_name):
    '''FILLER'''
    curs = prep(FILENAME)
    curs.execute(f"DROP TABLE {table_name}")

def add_member(userid, fullname):
    '''FILLER'''
    curs = prep(FILENAME)
    today = datetime.today()
    date_format = today.strftime("%Y %m %d") # as "YYYY MM DD"
    values_string = f"(\"{userid}\",\"{fullname}\",\"{date_format}\",1)" # default alert sign-up
    curs.execute(f"INSERT INTO {TABLE1NAME}({KEYS1_STRING}) VALUES {values_string}") # SQLite
    curs.execute("COMMIT") # SQLite command to saved the newly updated database

def alert_choice(userid, status):
    '''FILLER'''
    curs = prep(FILENAME)
    curs.execute(f"UPDATE {TABLE1NAME} SET alerts = {status} WHERE userid = \"{userid}\"")
    curs.execute("COMMIT")

def is_member(userid):
    '''FILLER'''
    # TODO: For bot to see if current user is on the LHQS member list
    #curs.execute(f"SELECT name FROM {table_name} WHERE username = {tele_user}").fetchall()

    #Ex. sgY = curs.execute(f"SELECT Y FROM {table_name}").fetchall()
    return True

def get_alert_list():
    '''FILLER'''
    # TODO: return userid list
