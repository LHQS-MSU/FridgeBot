'''
File: Database Communicator
Project: Telegram Bot LHQS Fridge Alert System
Developer: Abby Peterson
Purpose: Backend structure and methods to access our SQLite local databse
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
    '''PURPOSE: establish a read/write connection to our SQLite databse file
    RETURNS: a cursor object that will allow us to browse the database'''
    # Construct the full path to the database file
    db_path = os.path.join(os.path.dirname(__file__), filename + ".db")
    # Standard read/write connection
    conn = sqlite3.connect(db_path)
    this_curs = conn.cursor()  # can browse database using cursor methods
    return this_curs

def create_tables():
    '''PURPOSE: Creates 2 tables in telegram_info.db
    1. member_info: to track established LHQS users and alerts
    2. fridge_details: where the fridge errors/past alerts are stored'''
    curs = prep(FILENAME)

    #Create tables
    curs.execute(f"CREATE TABLE IF NOT EXISTS {TABLE1NAME} {KEYS1_INIT}") # makes user table
    curs.execute(f"CREATE TABLE IF NOT EXISTS {TABLE2NAME} {KEYS2_INIT}") # makes fridge table

def delete_table(table_name):
    '''PURPOSE: to wipe the table off of our database
    Not currently used anywhere, but can call if needed.'''
    # TODO: ideally add admin command to reset all users or clear fridge history
    curs = prep(FILENAME)
    curs.execute(f"DROP TABLE {table_name}")

def add_member(userid, fullname):
    '''GIVEN: userid - of telegram account signing up, fullname - of user too
    PURPOSE: adds telegram user (LHQS member) to our database so they get full access'''
    curs = prep(FILENAME)
    today = datetime.today()
    date_format = today.strftime("%Y %m %d") # as "YYYY MM DD"
    values_string = f"(\"{userid}\",\"{fullname}\",\"{date_format}\",1)" # default alert sign-up
    # TODO: add a check to see if the user is already in the table/fix multiple entries
    curs.execute(f"INSERT OR REPLACE INTO {TABLE1NAME}({KEYS1_STRING}) VALUES {values_string}") # SQLite
    curs.execute("COMMIT") # SQLite command to saved the newly updated database

def alert_choice(userid, status):
    '''GIVEN: userid - of telegram account changing their alert preference
        status - 1 means yes send alerts, 0 means turn their alerts off
    PURPOSE: called when telegram user sends /getalerts or /stopalerts'''
    curs = prep(FILENAME)
    curs.execute(f"UPDATE {TABLE1NAME} SET alerts = {status} WHERE userid = \"{userid}\"")
    curs.execute("COMMIT")

def is_member(userid):
    '''GIVEN: userid - of telegram account changing their alert preference
    PURPOSE: to check for qualifying accounts so that only LHQS telegram users can get access
    RETURNS: boolean T/F depending on if the telegram user is in our member table'''
    curs = prep(FILENAME)
    result = curs.execute(f"SELECT name FROM {TABLE1NAME} WHERE userid = \"{userid}\"").fetchall()
    if len(result) == 0:
        return False
    return True

def get_alert_list():
    '''PUPOSE: for our telegram bot to know who all to send fridge alerts to
    RETURNS: a list of all the userids that want to be alerted'''
    curs = prep(FILENAME)
    alert_ids = curs.execute(f"SELECT userid FROM {TABLE1NAME} WHERE alerts = 1").fetchall()
    format_ids = [] # alert_ids: [(id1,),(id2,)] <-- fixing tuple structure
    for cur_id in alert_ids:
        format_ids.append(cur_id[0])
    return format_ids
