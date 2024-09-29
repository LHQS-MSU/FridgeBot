'''
File: Fridge Communicator
Project: Telegram Bot LHQS Fridge Alert System
Developer: Abby Peterson (credit to Niyaz Beysengulov)
Purpose: Hosted on LHQS computer, tracking methods for BlueFors fridge
'''
import time
import os

def get_vars(cur_line):
    '''
    FILLER
    '''
    #Break up vars we care about
    cur_time = cur_line[10:18] #timestamp in line
    cur_temp = float(cur_line[19:]) #ch6 temp in line (ch6)
    return(cur_temp, cur_time)

async def check_em(temp, ranges, alert_func):
    '''
    Given a read value, check if it's w/in the asigned threshold
    If not, send alert to users via telegram bot
    '''
    #TODO: generalize to work with any of the 5 important values
        # Channel 6, Pressure 1, Pressure 3&4, Pressure 5, Variables cptempwi & cptempwo

    if (temp < ranges[0] and temp > ranges[1]): #temp is w/in threshold yay!
        print(f"We're doin good! At {temp}")
    else:
        print(f"WEEEWOOOWEEWOO At {temp}") #telegram sends warning w/ch6_time timestamp and temp
        await alert_func("Who knows rn")

def start_cont_check_logs(alert_func):
    '''
    TODO:
    Parse continuous log files for fridge data and alert when necessary
        Channel 6 - the mixing chamber, temperature <-- crucial
        Pressure 1 - the vacuum can, for a potential leak
        Pressure 3&4 - check points, to show any blocakge
        Variables cptempwi & cptempwo - if compressor is on/off
            Pressure 5 - if fridge turns off, to check on helium
    '''
    # Initial variables
    file_path = "lab_comp_files/CH6 T 23-12-05.log" #TODO: fix to appropiate local path
    exp_temp = 1 #varies based on experiment
    n = 0.02 #conditional threshold
    n_high = exp_temp + n
    n_low = exp_temp - n
    print(f"Stay w/in {n_high} and {n_low} please")

    # Open file
    with open(file_path, "r") as file:
        start = True
        # Read the entire file once initially
        for line in file:
            if start:
                print(f"Time {ch6_time}, temp {temp}") #TEST
                start = False
            else:
                temp, ch6_time = get_vars(line)
                check_em(temp, [n_high, n_low], alert_func)

        # Continuously read from the last position
        while True:
            where = file.tell()  # Get the current position in the file
            line = file.readline()
            if not line:
                print("Starting SLEEP")
                time.sleep(300)  # Sleep for 5 minutes (300 seconds)
                print("Ending SLEEP")
                file.seek(where)  # Move the cursor back to the last position
            else:
                temp, ch6_time = get_vars(line)
                check_em(temp, [n_high, n_low], alert_func)
          
async def fake_cont_check_logs(alert_funct):
    '''
    Tester function for reading/parsing static version of files
    '''
    # Initial variables
    filename = "CH6 T 23-12-05.log"
    file_path = os.path.join(os.path.dirname(__file__), filename)
    exp_temp = 1 #varies based on experiment
    n = 0.2 #conditional threshold
    n_high = exp_temp + n
    n_low = exp_temp - n
    print(f"Stay w/in {n_high} and {n_low} please")

    # Open file
    with open(file_path, "r") as file:
        start = True
        # Read the entire file once initially
        for line in file:
            if start:
                #print(f"Time {ch6_time}, temp {temp}") #TEST
                start = False
            else:
                temp, ch6_time = get_vars(line)
                await check_em(temp, [n_high, n_low], alert_funct)
