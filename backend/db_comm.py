'''
File: Database Communicator
Project: Telegram Bot LHQS Fridge Alert System
Developer: Abby Peterson
Purpose: 
'''
import re
import sqlite3

filename = "telegram_info" # the database that will create a table we are saving values to
table1_name = "member_info" # for telegram users to sign up for fridge bot information
table2_name = "fridge_details"