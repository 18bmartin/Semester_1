#importing the Tkinter library in order to create the GUI
from tkinter import *
#importing the hashlib library in order to hash the password
import hashlib
#importing the os library to connect to the internet website
import os

#creating the GUI
class PasswordTester:
#setting up the GUI
#this functions is creating the positions and objects within the GUI
    def __init__(self, master):
        self.master = master
#labelling the Title
        master.title("Password Tester")

#creating label for the first password input
        self.inputText1 = Label(master, text= "              Enter Password   ", )
#position of label on GUI
        self.inputText1.grid(row = 1, column = 0)

#creating entry for the first password
        self.pass1 = StringVar()
        self.enterPass1 = Entry(master, show="*", textvariable=self.pass1)
#position of entry space
        self.enterPass1.grid(row = 1, column = 1)

#creating label for the second password input
        self.inputText2 = Label(master, text="           Re-Enter Password      ")
#position of label on GUI
        self.inputText2.grid(row = 2, column = 0)

#creating entry for the second password input
        self.pass2 = StringVar()
        self.enterPass2 = Entry(master, show="*", textvariable=self.pass2)
#position of entry space
        self.enterPass2.grid(row = 2, column = 1)

#creating button for testing password
        self.TestButton = Button(master, text="Test", command=self.Test)
#position of button
        self.TestButton.grid(row=4, column=0)

#creating button for exiting code
        self.ExitButton = Button(master, text="Exit", command=master.quit)
#position of button
        self.ExitButton.grid(row=4, column=1)

#creating space within the GUI or the error messages and results
        self.spaceText = Label(master, text='''                          
        
        
        ''')
#position of created space
        self.spaceText.grid(row = 5, column = 0)

#the function which happens when the user presses the test button
    def Test(self):
#giving the first password input a variable
        p1 = self.pass1.get()
#giving the second password input a variable
        p2 = self.pass2.get()
#finding the length of the first password input
        length = len(p1)
#if the length is less than 8 characters it informs the user with an error message
        if length < 8:
#creating the error message
            self.errorText = Label(text= '''Your password must 
    be greater than or equal    
    to 8 characters in length    ''')
#positoin of error message
            self.errorText.grid(row=5)
#if the two entered passwords do not match it informs the user with an error message
        elif p1 != p2:
#creating the error message, extra space to properly cover any previous error messages
            self.errorText = Label(text='''The 2 passwords you
    have entered do not match
                                    ''')
#position of the error message
            self.errorText.grid(row=5)
#if the password input has no errors
        else:
#creating empty space to cover any previous error messages
            self.spaceText = Label(text='''                                                
      
      
                                 ''')
#position of error message removal
            self.spaceText.grid(row=5, column=0)
#turning the password into binary code
            p1 = str(p1).encode('utf-8')
#hashing the binary password into SHA-1 hash
            hashPassword = hashlib.sha1(p1)
            hashPassword = hashPassword.hexdigest()
#deleting the password variables now they are no longer necessary
            p1 = 0
            p2 = 0
#splitting the hash into affixes and making them all capitals
            hPrefix = hashPassword[0:5]
            hSuffix = hashPassword[6:]
            hPrefix = hPrefix.upper()
            hSuffix = hSuffix.upper()

#sending the hash prefix to the website and sending the results to a file
            os.system('curl https://api.pwnedpasswords.com/range/' + hPrefix + '>PPR.txt')

#opening the file the send the results from the Pwned passwords website
            PPR = open('PPR.txt', 'r')
#defining a variable for the while loop
            x = 0
#reading the file line by line
            fileRead = PPR.readline().strip()
#for each line within the file
            while fileRead:
#search for the hash suffix within the line
                fileSearch = fileRead.find(hSuffix)
#if the hash suffix is found within the line
                if fileSearch != -1:
                    result = fileRead[36:]
# creating the result message
                    self.resultText = Label(text='''this password 
      has been PWNED 
     ''' + result + " times     ")
# position of result message
                    self.resultText.grid(row=5, column=1)
#making x = 1 for if the suffix has been found
                    x = 1
#reading the next line and repeat process
                fileRead = PPR.readline().strip()
#if the suffix has not been found
            if x == 0:
# creating the result message
                self.resultText = Label(text='''  this password 
has not been 
      PWNED               ''')

# position of result message
                self.resultText.grid(row=5, column=1)

#deleting the file with all the possible hash suffixes
os.system('rm PPR.txt')

#Functions to make the GUI work
root = Tk()
gui = PasswordTester(root)
root.mainloop()