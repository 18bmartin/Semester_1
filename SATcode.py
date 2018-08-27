""" Author: Brent martin
Date:
Version: 1.0
This code will allow users to test their passwords against a database of stolen passwords in order to check
whether their passwords are secure. The database is in the form of the website 'PWNED passwords' which is
a database of all passwords which have already been broken into and so are insecure. For security reasons the code will
only send the first 5 digits of a Hashed version of their entered password and then search through the many corresponding hashes.

variables in order of appearance:
Binary Search:
    list = the list of possible hashes gotten from the website
    target = the hash which is being searched for in the list
    Pwned = a binary value definiing whether or not the target is within the list
    low = the lowest value within the search algorithm
    high = the highest value within the search algorithm
    mid = the midpoint between low and high
    val = the varible at the position of mid within the list
p1/self.pass1 = the first user input for their password
p2/self.pass2 = the second user input for their password
length = the length of the first password input
hashPassword = the first password input (after testing that p1 = p2) made into hash format
p1/p2 = zero values so they are forgotten
hPrefix = the first 5 digits of the hash
hSuffix = the last 35 digits of the hash
PPR = returned fil with all the Pwned passwords correlating to the hash prefix and the number of times they have been pwned
fileRead = a single line of the file, looping through the whole file
fileList = each of the hash suffixes returned placed into a list
pwnedList = the number of times each hash has been pwned placed into a list
position[0]/result = the position of the correct hash in the fileList
# position[1]/Pwned = the binary value of whether or not the hash suffix has been found in the list"""

# importing the Tkinter library in order to create the GUI
from tkinter import *
# importing the hashlib library in order to hash the password
import hashlib
# importing the os library to connect to the internet website
import os
# a binary search upon the list made
def BinarySearch(list, target):
# defining a binary result of whether or not the target is within the list
    Pwned = 0
# defining the size of the list
    low = 0
    high = len(list)
# while the lowest value is smaller than the highest value (when they are the same the value is not within the list)
    while low < high:
# finding the midpoint of the section being searching
        mid = (low + high) // 2
# getitng the value from the midpoint
        val = list[mid]
# making all the variables strings for consistent < > = comparisons
        target = str(target)
        val = str(val)
        mid = str(mid)
        low = str(low)
        high = str(high)
# if the target is found
        if target == val:
# making the binary 1 as a 'True' value to whether or not the hash Suffix is within the list
            Pwned = 1
# returning the position of the hash and whether or not it is within the list
            return (mid, Pwned)
# if the target is greater than the current value
        elif str(target) > str(val):
# if the lowest value is already equal to the middle value the target is not within the list
            if low == mid:
                break
# make the midpoint the lowest value, allowing the code to create a new midpoint in the next loop
            low = mid
# if target is less than the current value
        elif str(target) < str(val):
# make the midpoint the highest value, allowing the code to create a new midpoint in the next loop
            high = mid
# returning the high and low variable into integers to use in the earlier equation for the next loop
        low = int(low)
        high = int(high)
#returning the value of Pwned if the hash is not found
    return (0, Pwned)
# creating the GUI
class PasswordTester:
# setting up the GUI
# this functions is creating the positions and objects within the GUI
    def __init__(self, master):
        self.master = master
# labelling the Title
        master.title("Password Tester")
# creating label for the first password input
        self.inputText1 = Label(master, text= "              Enter Password   ", )
# position of label on GUI
        self.inputText1.grid(row = 1, column = 0)
# creating entry for the first password
        self.pass1 = StringVar()
        self.enterPass1 = Entry(master, show="*", textvariable=self.pass1)
# position of entry space
        self.enterPass1.grid(row = 1, column = 1)
# creating label for the second password input
        self.inputText2 = Label(master, text="           Re-Enter Password      ")
# position of label on GUI
        self.inputText2.grid(row = 2, column = 0)
# creating entry for the second password input
        self.pass2 = StringVar()
        self.enterPass2 = Entry(master, show="*", textvariable=self.pass2)
# position of entry space
        self.enterPass2.grid(row = 2, column = 1)
# creating button for testing password
        self.TestButton = Button(master, text="Test", command=self.Test)
# position of button
        self.TestButton.grid(row=4, column=0)
# creating button for exiting code
        self.ExitButton = Button(master, text="Exit", command=master.quit)
# position of button
        self.ExitButton.grid(row=4, column=1)
# creating space within the GUI or the error messages and results
        self.spaceText = Label(master, text='''                          
        
        
        ''')
# position of created space
        self.spaceText.grid(row = 5, column = 0)
# the function which happens when the user presses the test button
    def Test(self):
# giving the first password input a variable
        p1 = self.pass1.get()
# giving the second password input a variable
        p2 = self.pass2.get()
# finding the length of the first password input
        length = len(p1)
# if the length is less than 8 characters it informs the user with an error message
        if length < 8:
# creating the error message
            self.errorText = Label(text= '''Your password must 
    be greater than or equal    
    to 8 characters in length    ''')
# position of error message
            self.errorText.grid(row=5)
# if the two entered passwords do not match it informs the user with an error message
        elif p1 != p2:
# creating the error message, extra space to properly cover any previous error messages
            self.errorText = Label(text='''The 2 passwords you
    have entered do not match
                                    ''')
# position of the error message
            self.errorText.grid(row=5)
# if the password input has no errors
        else:
# creating empty space to cover any previous error messages
            self.spaceText = Label(text='''                                                
      
      
                                 ''')
# position of error message removal
            self.spaceText.grid(row=5, column=0)
# turning the password into binary code
            p1 = str(p1).encode('utf-8')
# hashing the binary password into SHA-1 hash
            hashPassword = hashlib.sha1(p1)
            hashPassword = hashPassword.hexdigest()
# deleting the password variables now they are no longer necessary
            p1 = 0
            p2 = 0
# splitting the hash into affixes and making them all capitals
            hPrefix = hashPassword[0:5]
            hSuffix = hashPassword[5:]
            hPrefix = hPrefix.upper()
            hSuffix = hSuffix.upper()
# sending the hash prefix to the website and sending the results to a file
            os.system('curl https://api.pwnedpasswords.com/range/' + hPrefix + '>PPR.txt')
# opening the file the send the results from the Pwned passwords website
            PPR = open('PPR.txt', 'r')
# reading the file line by line
            fileRead = PPR.readline().strip('\n')
# defining two lists which split the hash suffix and the number of times the password has been Pwned from the file
            fileList = []
            pwnedList = []
# for each line within the file
            while fileRead:
# add the hash prefix and number of times the password has been Pwned to their corresponding lists
                fileList.append(fileRead[:35])
                pwnedList.append(fileRead[36:])
# reading the next line for the loop
                fileRead = PPR.readline().strip('\n')
# using the binary search to get a return on whether or not the password has been Pwned
            position = BinarySearch(fileList, hSuffix)
# splitting the 2 values of position into their respective duties part 1
            Pwned = position[1]
# if the hash suffix has been found:
            if Pwned == 1:
# splitting the 2 values of position into their respective duties part 2
                result = pwnedList[int(position[0])]
# displays a message informing the user that the password they have input is not secure
                self.resultText = Label(text='''this password
      has been PWNED
     ''' + result + " times     ")
# position of result message
                self.resultText.grid(row=5, column=1)
# if the hash suffix has NOT been found:
            else:
# displays a message saying the password has not been Pwned
                self.resultText = Label(text='''  this password
has not been
      PWNED               ''')
# position of result message
                self.resultText.grid(row=5, column=1)
            Pwned = 0
# deleting the file with all the possible hash suffixes
os.system('rm PPR.txt')
# Functions to make the GUI work
root = Tk()
gui = PasswordTester(root)
root.mainloop()