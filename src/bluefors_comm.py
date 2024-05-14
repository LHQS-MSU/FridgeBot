'''
File: Fridge Communicator
Project: Telegram Bot LHQS Fridge Alert System
Developer: Abby Peterson (credit to Niyaz Beysengulov)
Purpose: 
'''
import time

def get_vars(cur_line):
    '''
    FILLER
    '''
    #Break up vars we care about
    cur_time = cur_line[10:18] #timestamp in line
    cur_temp = float(cur_line[19:]) #ch6 temp in line (ch6)
    return(cur_temp, cur_time)

def check_em(temp, ranges):
    '''
    FILLER
    '''
    if (temp < ranges[0] and temp > ranges[1]): #temp is w/in threshold yay!
        print(f"We're doin good! At {temp}")
    else:
        print(f"WEEEWOOOWEEWOO At {temp}") #telegram sends warning w/ch6_time timestamp and temp

def start_cont_check_logs():
    '''
    FILLER
    '''
    # Initial variables
    file_path = "lab_comp_files/CH6 T 23-12-05.log"
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
                check_em(temp, [n_high, n_low])

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
                check_em(temp, [n_high, n_low])
                