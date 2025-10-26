import os
import hashlib
from csv import (reader, writer, DictReader, DictWriter)
from datetime import datetime
from time import sleep

# def get_clean_input(prompt):
#     return input(prompt).lower().strip()

get_clean_input = lambda prompt: input("previous name: ").lower().strip()

print(get_clean_input("this is inp: "))


import user_pass_func
import database_func

prompt_global = """
What is your role
Press 1 for Manager
Press 2 for Doctor
enter 'q' to quit
>> """
 # press 1-> if paitent already exists update the paitents data with same id 
prompt_manager = """
Press 1 to entry new paitent
Press 2 to update name or illness
Press 3 delete data with name or id
Press 4 to search a drug
Press 5 to add drug information
Press 6 to update drug price or quantity information
enter '0' to go back
>> """

# the doctor can only check a paitent if it goes through manager else it is not premisible
# press 1-> if paitent already exists show illness and prompt to add new illness else prompt to entry
# press 2-> add prescription based on id from paitent_list.csv
# the prescriptio should have three info (paitent basic info, medicine, test)
prompt_doctor = """
Press 1 to check paitent info (name, illness etc)
Press 2 to add paitents prescription
enter '0' to go back
>> """

# while action[0] != "q":
#     action = input(prompt_doctor).lower().strip()

# part 1 (login)
# take login info from a txt file like doctor or manager name and password 
# if the input matches the list of doctor or manager name then enter, after that prompt them password
# in the corresponding 

action = "1"

if action == "1":
    username = input("Username: ").strip()
    
    username_ls, password_ls = database_func.get_user_info("manager_list.csv")
    print(username_ls, password_ls)
    
    if username in username_ls:
        password = getpass("Password: ")
        print(password_ls)
        if password in password_ls:
            print("logged in as manager")
            inner_action = ""
            while inner_action != "0":
                print(f"Current user {username}\n")
                inner_action = input(prompt_manager).lower().strip()

                if inner_action == "1":
                    database_func.write_paitent_info("paitent_list.csv")
        else:
            print("Password did not match!!")
            # clear
    else:
        print(f"{username} does not exists")
        # clear


        


# part 2 manager (taking serial)
# manager taking serial means to take paitent information (id, date, name, illness, ) and store them in a file
# also add a back button


# with open("paitent_info.txt") as f:
#     pass





