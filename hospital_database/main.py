import os
from time import sleep
import datetime
from getpass import getpass

import user_pass_func
import database_func

def clear_terminal(prompt: str)-> None:
    os.system("clear")
    print(prompt)

get_clean_input = lambda prompt: input(prompt).lower().strip()

prompt_global = """
What is your role?
Press 1 for Manager
Press 2 for Doctor
enter 'q' to quit
>> """

prompt_manager = """
Press 1 to entry new paitent
Press 2 to update name or illness
Press 3 delete data with name or id
Press 4 to search a drug
Press 5 to add drug information
Press 6 to update drug price or quantity information
enter '0' to logout
>> """

prompt_doctor = """
Press 1 to check paitent info (name, illness etc)
Press 2 to add paitents prescription
enter '0' to go back
>> """

action = ""


while action != "q":
    clear_terminal("")
    print("="*60)
    print("🩺  Monta Health  🩺")
    print("Taking care of your health is our concern")
    print("="*60)

    action = input(prompt_global).lower().strip()

    if action == "1":   # managers action
        clear_terminal("")
        print("Enter username and password for manager")
        username = input("Username: ").strip()
        
        username_ls, password_ls = database_func.get_user_info("manager_list.csv")
        # print(username_ls, password_ls)
        
        if username in username_ls:
            password = getpass("Password: ")
            # print(password_ls)
            if password in password_ls:
                clear_terminal(f"logged in as {username}")

                inner_action = ""
                while inner_action != "0":

                    clear_terminal(f"Current user {username}\n")
                    inner_action = input(prompt_manager).lower().strip()

                    if inner_action == "1":
                        clear_terminal(f"{username} is writing paitent information")
                        database_func.write_paitent_info()

                    elif inner_action == "2":
                        clear_terminal(f"{username} is updating information")

                        mode = get_clean_input("Press 1 for name\nPress 2 for illness\n>> ")
                        
                        if mode == "1":
                            clear_terminal(f"{username} is updating information")
                            database_func.update_db("name")
                        elif mode == "2":
                            clear_terminal(f"{username} is updating information")
                            database_func.update_db("illness")
                    
                    elif inner_action == "3":
                        clear_terminal(f"{username} is deleting information")
                        mode = get_clean_input("Press 1 for id\nPress 2 for name\n>> ")
                        
                        if mode == "1":
                            clear_terminal(f"{username} is deleting information")
                            data = get_clean_input("Enter Id: ")
                            database_func.delete_data_db("id", data)
                        elif mode == "2":
                            clear_terminal(f"{username} is deleting information")
                            data = get_clean_input("Enter name: ")
                            database_func.delete_data_db("name", data)

                    elif inner_action == "4":
                        # Press 4 to search a drug
                        clear_terminal(f"{username} is searching for a drug")
                        database_func.search_drug()
                    
                    elif inner_action == "5":
                        # Press 5 to add drug information
                        clear_terminal(f"{username} is adding drug information")
                        database_func.add_drug_info()
                        
                    
                    elif inner_action == "6":
                        # Press 6 to update drug price or quantity information
                        clear_terminal(f"{username} is updating drug information")
                        mode = get_clean_input("Press 1 for id\nPress 2 for name\n>> ")
                        
                        if mode == "1":
                            clear_terminal(f"{username} is updating drug information")
                            data = get_clean_input("Enter Id: ")
                            database_func.update_drug_info("id", data)

                        elif mode == "2":
                            clear_terminal(f"{username} is updating drug information")
                            data = get_clean_input("Enter name: ")
                            database_func.update_drug_info("name", data)
                    
                    elif inner_action == "0":
                        break
                    else:
                        clear_terminal("")
                        
                    
            else:
                clear_terminal("")
                print("Password did not match!!")
                sleep(2)
                os.system("clear")
        else:
            clear_terminal("")
            print(f"{username} does not exists")
            sleep(2)
            os.system("clear")


    elif action == "2":     # doctors action
        clear_terminal("")
        print("Enter username and password for doctor")
        username = input("Username: ").strip()
        
        username_ls, password_ls = database_func.get_user_info("doctor_list.csv")
        # print(username_ls, password_ls)
        
        if username in username_ls:
            password = getpass("Password: ")
            # print(password_ls)
            if password in password_ls:
                clear_terminal(f"Logged in as {username}")
                
                inner_action = ""
                while inner_action != "0":

                    os.system("clear")
                    print(f"Current user {username}\n")
                    inner_action = input(prompt_doctor).lower().strip()

                    if inner_action == "1":
                        clear_terminal(f"{username} is writing searching paitent information")
                        database_func.view_paitent_info()

                    elif inner_action == "2":
                        clear_terminal(f"{username} is writing a pescription")
                        database_func.write_paitent_prescription()

                    elif inner_action == "0":
                        break
                    else:
                        clear_terminal("")
                        
            else:
                clear_terminal("")
                print("Password did not match!!")
                sleep(2)
                
        else:
            clear_terminal("")
            print(f"{username} does not exists")
            sleep(2)
   
os.system("clear")
print("\033[1mThank you for using Monta Health management system\033[0m", end="\n\n")