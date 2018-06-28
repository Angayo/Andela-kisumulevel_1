'''This is the place where user name is stored in the database and the status 
 if he is log in
'''
users = {}
status = ""

def displayMenu():# checks if the user is registered or not
    status = input("Are you registered user? y/n? ")
    if status == "y":                                     
        currentUser()
    elif status == "n":
        newUser()
 
def newUser(): #creates  new user and sees if user already exit
    createLogin = input("Create username: ")
    if createLogin in users:
        print("\n Username already exist!\n")
    else:
        createPassword = input("Create password: ")
        users[createLogin] = createPassword
        print("\n newUser created\n")
 
def currentUser():#It prompts the user to enter username an password
    login = input("Enter login name: ")
    password = input("Enter password: ")
 
    if login in users and users[login] == password:
        print("\nLogin successful!\n")
    else:
        print("\n User doesn't exist or wrong password!\n ")
 
while status != "q":
    displayMenu()



