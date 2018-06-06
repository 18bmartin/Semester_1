from tkinter import *
import hashlib

PPR = open('Pwnedpasswordresults.txt', 'a')

class PasswordTester:

    def __init__(self, master):
        self.master = master
        master.title("Password Tester")

        self.titleText = Label(master, text="Password Tester")
        self.titleText.grid()

        self.inputText1 = Label(master, text= "              Enter Password   ", )
        self.inputText1.grid(row = 1, column = 0)

        self.pass1 = StringVar()
        self.enterPass1 = Entry(master, show="*", textvariable=self.pass1)
        self.enterPass1.grid(row = 1, column = 1)

        self.inputText2 = Label(master, text="           Re-Enter Password      ")
        self.inputText2.grid(row = 2, column = 0)

        self.pass2 = StringVar()
        self.enterPass2 = Entry(master, show="*", textvariable=self.pass2)
        self.enterPass2.grid(row = 2, column = 1)

        self.TestButton = Button(master, text="Test", command=self.Test)
        self.TestButton.grid(row=4, column=0)

        self.ExitButton = Button(master, text="Exit", command=master.quit)
        self.ExitButton.grid(row=4, column=1)

        self.spaceText = Label(master, text='''                          
        
        
        ''')
        self.spaceText.grid(row = 5, column = 0)

    def Test(self):
        p1 = self.pass1.get()
        p2 = self.pass2.get()
        length = len(p1)

        if length < 8:
            self.errorText = Label(text= '''Your password must 
    be greater than or equal    
    to 8 characters in length    ''')
            self.errorText.grid(row=5)
        elif p1 != p2:
            self.errorText = Label(text='''The 2 passwords you
    have entered do not match
                                    ''')
            self.errorText.grid(row=5)
        else:
            self.spaceText = Label(text='''                                                
      
      
                                 ''')
            self.spaceText.grid(row=5, column=0)
            p1 = str(p1).encode('utf-8')
            hashPassword = hashlib.sha1(p1)
            hashPassword = hashPassword.hexdigest()
            hPrefix = hashPassword[0:5]
            hSuffix = hashPassword[5:]
PPR.close()

root = Tk()
gui = PasswordTester(root)
root.mainloop()