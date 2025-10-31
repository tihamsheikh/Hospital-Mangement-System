from platform import system as psys
from os import system as osys
from time import sleep
import os
from csv import writer

# type = input("t: ")
# value = input("v: ")
# print(f"{type}({value})")
# a = f"{type}({value})"
# print(a)
# sleep(2)

print(psys())
# print(osys("clear"))

clear_terminal = lambda: osys("cls") if psys().lower().strip() == "windows" else osys("clear") 

def clear():
    if psys().lower().strip() == "windows":
        osys("cls")
    else: 
        osys("clear") 


def add_drug_info()-> None:
    """
        inputs drug data(id, name, price, quantity) into db 
    """
    checker = lambda id: id == ""
    base_dir = os.path.dirname(__file__)
    user_list_path = os.path.join(base_dir, "database", "drug_list.csv")

    clear()
    # id, name, price, quantity
    print("Enter durg information")

    id = input("Id: ").strip()
    name = input("Name: ").lower().strip()
    price = input("Price: ")
    quantity = input("Quantity: ")

    
    if "" in [id, name, price, quantity]:
        clear()
        print("Wront input")
        sleep(0.5)
        return 
    
    try: 
        price = float(price)
    except ValueError:
        clear()
        print("Put a number you mut")
        sleep(0.5)
        return
    try:
        quantity = int(quantity)
    except ValueError:
        clear()
        print("Put a number you mut")
        sleep(0.5)
        return
    

    with open(user_list_path, "a", newline="\n") as fp:

        data = writer(fp)
        data.writerow([id, name, abs(float(price)), abs(int(quantity))])
        print("Data recorded")
        sleep(2)

add_drug_info()