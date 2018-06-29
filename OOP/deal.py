'''This is the place where user name is stored in the database and the status 
 if he is log in
'''
'''This is the place where user name is stored in the database and the status 
 if he is log in
'''
from user import Users
from db import cred_User


class Details():
    def check_data():
        command = ("Are you registered user? y/n? ")
        while command != 'q':
            command = input("Enter your login Details: ")
            if command == 'y':
                self.login()
                print("You are logged in")
            elif command == "n":
                self.register()
                print("Welcome to Andela")

    def log_in(self):
"""if the user is not registered it should 
request the user to register. If the user."""
        logged_in = False
        email = str(input("Please enter your email: "))
        password = str(input("Please enter your password: "))

        fh = open("my_database", 'r')#opens a file called my_database with read priviledges
        my_database = json.load(fh)#read a dictionary from the file

    if email in my_database:
        database_identies = my_database[email]
        database_password = database_identies[0]
        if database_password == password:
            logged_in = True
            print("You are now logged in.")
        return logged_in
        else:
        print("Wrong email or password used.")
    else:
        print("You have not registered yet. Please register first.")

    def log_out(self):
        """Allows the user to log out of the application"""
        if logged_in == True:
            logged_in ==False
            return logged_in    

def make_comment(self):
    if logged_in == True:
    print("You can now post a comment.")
    print("please log in first.")

def reply_comment(self):
    if logged_in == True:
    print("You can now reply to a comment.")
print("please log in first.")
