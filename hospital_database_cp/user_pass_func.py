from os import system
from time import sleep
from getpass import getpass


class Credentials:

    def removing_repeatation(self, password: str)-> bool:
        """
            it blocks user from using same char and setting it as a password
            at least three different char is needed
            return -> bool
        """
        dict = {}        
        for char in password:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
        most_used_char = max([value for value in dict.values()])

        return most_used_char < len(password)-2 

    def strong_pass_check(self, username: str)-> str:
        """
            gets input from user and checks
            if the inputed password is larger than 10 char 
            and uses number, digit and special char
            returns -> str
        """
        check: bool = True

        while check:
            system("clear")
            print(f"Password for this username '{username}'")
            password: str = getpass("Choose a password: ") 
            # hw
            if password.isdigit() or password.isalpha() or len(password) < 10 or password.isalnum():
                review = "password too short" if len(password) < 10 else "use different character"  
                print(review)
                sleep(.5)
                system("clear")
                continue

            if not password.isalnum() and self.removing_repeatation(password):
                print("Account created")
                check = False
                break

        return password


    def get_username_password(self)-> tuple:
        """
            Gets username and password 
            and returns username and password
            -> username, password
        """
        username: str = input("Username: ").strip()
        password: str = self.strong_pass_check(username)

        return username, password



