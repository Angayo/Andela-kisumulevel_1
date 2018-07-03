class Sign(object):
    dictis={}
    def __init__(self):
        self.post_comment=[]
        self.reply_comment=[]
        status=""

    def main(self):
    	command=input("Are you registered ? y/n: ")
    	if command == 'y':
            print('Login exist') 
    	elif command == 'n':
    		print("Fill the registration form:")
    	else:
    		print("incorrect username or password")

    def registration(self):
        sur_Name = input ("Enter SurName: ")
        first_Name = input ("Enter FirstName: ")
        last_Name  = input("Enter SeconName:")
        email_Addr = input ("Enter Your Email: ")
        username = input ("Enter Username: ")
        password = input ("Enter Password: ")
        password2 = input ("Confirm Password: ")

        self.dictis.update({username:[password, sur_Name, first_Name,  last_Name, email_Addr]})
        print ("successfully Registered " + username)

    def login(self):
        username = input ("Enter Username: ")
        password = input("Enter Password: ")
        if password == self.dictis[username]:
            print("welcome")
        else:
            print("invalid username or password try again: ")

    def post_comments(self):
    	comment= self.post_comment.append(input("Place your comments here please: "))
    	self.post_comment.append(comment)
    	print(self.post_comment)

    def reply(self):
    	comment = self.reply_comment.append(input("place your reply comment here: "))
    	self.reply_comment.append(comment)
    	print(self.reply)

    def logout(self):
    	user = input("Do you want to logout: click y/n  ")
    	if user == 'y':
    		return 'You have logout'
    	else:
    		return  'login'

Test = Sign()
print(Test.main(), Test.registration(), Test.login(), Test.post_comments(), Test.reply(), Test.logout())