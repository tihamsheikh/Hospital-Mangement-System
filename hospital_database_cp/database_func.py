import os
import hashlib
from csv import (reader, writer, DictReader, DictWriter)
from datetime import datetime
from time import sleep
from os import system as osys
from platform import system as psys


clear = lambda: osys("cls") if psys().lower().strip() == "windows" else osys("clear") 
get_clean_input = lambda prompt: input(prompt).lower().strip()

class DatabaseFunctions:


    def get_user_info(self, db: str)-> tuple:
        """
            gets the username and password from a csv file -> (list, list)
        """
        base_dir = os.path.dirname(__file__)
        user_list_path = os.path.join(base_dir, "database", db)

        with open(user_list_path) as fp:
            username, password = [], []
            info = reader(fp)
            next(info)

            for i in info:
                username.append(i[0])
                password.append(i[1])
        return username, password


    def get_id(self, name: str)-> int:
        """
            used to convert patient name into an id
        """
        name = f"{name}{datetime.now()}"
        hash_object = hashlib.md5(name.encode())  # encode string to bytes
        return int(hash_object.hexdigest(), 16) % (10 ** 8) # convert hex to integer (10** len of int)


    def write_patient_info(self)-> None:
        """
            takes patient info from user and stores it in db (patient_list.csv)
        """

        base_dir = os.path.dirname(__file__)
        user_list_path = os.path.join(base_dir, "database", "patient_list.csv")
        # print(user_list_path)

        with open(user_list_path, "a", newline="\n") as fp:
            file = writer(fp)
            
            patient_name = get_clean_input("patient Name: ")
            illness = get_clean_input("patient's Illness: ")

            # id, date, name, illness
            file.writerow([self.get_id(patient_name),datetime.now(),patient_name,illness])
        print("Information is recorded")
        sleep(2)



    def update_db(self, key: str)-> dict:
        """
            key(illness or name), old(illness or name), new(illness or name) is 
            inputed illness or name (key=title/heading, value=existing data, new_value=new data) is changed in csv
        """

        check = False
        base_dir = os.path.dirname(__file__)
        user_list_path = os.path.join(base_dir, "database", "patient_list.csv")


        old_data = get_clean_input(f"previous {key}: ")
        new_data = get_clean_input(f"new {key}: ")
        
        with open(user_list_path) as fp:
            dict_list = list(DictReader(fp))
            # print(content)
            for dictionary in dict_list:

                valid_keys = ["name", "illness"]
                if key not in valid_keys:
                    print(f"Invalid key '{key}'. Must be one of: {valid_keys}")
                    return
                if dictionary[key] == old_data:
                    # print(dictionary[key])
                    dictionary[key] = new_data
                    check = True
                
        if check:
            with open(user_list_path, "w", newline="\n") as fp:
                
                title = ["id", "date", "name", "illness"]
                writer = DictWriter(fp, fieldnames=title)
                writer.writeheader()
                writer.writerows(dict_list)
            print("Database is updated")
            sleep(2)
        else:
            print(f"{old_data} does not exist!!")


    def delete_data_db(self, key: str, value: str)-> dict:
        """
            key(id or name), value(id or name) is 
            inputed id or name (key=title/heading), value=existing data is deleted in csv
        """

        check = False
        base_dir = os.path.dirname(__file__)
        user_list_path = os.path.join(base_dir, "database", "patient_list.csv")

        with open(user_list_path) as fp:
            dict_list = list(DictReader(fp))
            # print(content)
            for index, dictionary in enumerate(dict_list):
                # print(index, dictionary)
                if dictionary[key] == value:
                    
                    # print(dictionary[key])
                    del dict_list[index]
                    check = True
                
        if check:
            with open(user_list_path, "w", newline="\n") as fp:
                
                title = ["id", "date", "name", "illness"]
                writer = DictWriter(fp, fieldnames=title)
                writer.writeheader()
                writer.writerows(dict_list)
            print(f"{value} is deleted from Database")
            sleep(2)
        else:
            print(f"{value} does not exist!!")


    def search_drug(self)-> None:
        """
            takes a drug name as input and displays all drug named like that
        """
        base_dir = os.path.dirname(__file__)
        user_list_path = os.path.join(base_dir, "database", "drug_list.csv")
        check = True
        search = get_clean_input("Drug name: ")
        
        
        with open(user_list_path, "r") as fp:
            data = reader(fp)
            next(fp)
            clear()
            for d in data:
                if search in d[1]:
                    print(f"Id: {d[0]}  Name: {d[1]}  Price: {d[2]}  Quantity: {d[3]}")
                    check = False
            
        if check:
            print(f"{search.capitalize()} not found")
        sleep(5)



    def add_drug_info(self)-> None:
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
            sleep(1)
            return 
        
        try: 
            price = float(price)
        except ValueError:
            clear()
            print("Put a number you mut")
            sleep(1)
            return
        try:
            quantity = int(quantity)
        except ValueError:
            clear()
            print("Put a number you mut")
            sleep(1)
            return

        with open(user_list_path, "a", newline="\n") as fp:

            data = writer(fp)
            data.writerow([id, name, abs(float(price)), abs(int(quantity))])
            print("Data recorded")
            sleep(2)


    def update_drug_info(self, key: str, key_value: str)-> None:
        """
            takes existing drug key=(id), key_value=(price,quantity, name)
        """

        base_dir = os.path.dirname(__file__)
        user_list_path = os.path.join(base_dir, "database", "drug_list.csv")
        check = False

        with open(user_list_path) as fp:
            dict_list = list(DictReader(fp))
            # print(dict_list)
            for dictionary in dict_list:
                # print("new: ",dictionary)
                if dictionary[key] == key_value:
                    action = input("Press 1 for price\nPress 2 for quantity\nPress 3 for name\n>> ").lower().strip()
                    if action == "1":
                        dictionary["price"] = input("New price: ").strip()
                    elif action == "2":
                        dictionary["quantity"] = input("New quantity: ").strip()
                    elif action == "3":
                        dictionary["name"] = input("New name: ").lower().strip()
                    else:
                        print("Good luck, starting from the start :)")
                    check = True
                # print("old: ",dictionary)
                
        if check:
            with open(user_list_path, "w", newline="\n") as fp:
                
                title = ["id", "name", "price", "quantity"]
                writer = DictWriter(fp, fieldnames=title)
                writer.writeheader()
                writer.writerows(dict_list)
            print("Database is updated")
            sleep(2)
        else:
            print(f"{key_value} does not exist!!")
        sleep(2)


    def view_patient_info(self)-> None:
        """
            inputing patients name, provides with indepth info  
        """

        base_dir = os.path.dirname(__file__)
        user_list_path = os.path.join(base_dir, "database", "patient_list.csv")
        check = True

        name = input("patient name: ").lower()

        with open(user_list_path) as fp:
            data = reader(fp)
            next(data)

            clear()
            for item in data:
                if name == item[2]:
                    # print(item)

                    print(f"Appointment data: {item[1]}\nid: {item[0]}\npatient name: {item[2]}\nIllness: {item[3]}", end="\n\n")
                    check = False
            if check:
                print(f"{name} does not exitst!!")
                sleep(4)
                return
        sleep(10)


    def get_list(self, type: str):
            """
                type=(illness, test or drug) return a list of (illness, test or drug) 
            """
            list = []
            variable = ""
            prompt = f"Enter the {type}: "
            clear()
            print("Enter 'q' to quit")
            while True:
                # os.system("clear")
                variable = input(prompt).lower().strip()
                if variable == "q":
                    break 
                list.append(variable)

            return list


    def write_patient_prescription(self):
        """
            takes patient info from user and stores it in db (patient_prescription.csv)
        """

        base_dir = os.path.dirname(__file__)
        user_list_path = os.path.join(base_dir, "database", "patient_prescription.csv")
        # print(user_list_path)

        with open(user_list_path, "a", newline="\n") as fp:
            file = writer(fp)
            
            clear()
            patient_name = input("patient Name: ").lower().strip()
            
            
            illness = self.get_list("Illness list: ")
            test = self.get_list("Tests list: ")
            drug = self.get_list("Drug list: ")


            # id, date, name, illness
            file.writerow([patient_name, illness, test, drug])
            clear()

        print("Information is recorded")
        sleep(2)


obj = DatabaseFunctions()


