from tkinter import *

class PasswordTester:

    def __init__(self, master):
        self.master = master
        master.title("Password Tester")

        self.titleText = Label(master, text="Password Tester")
        self.titleText.grid()

        self.inputText1 = Label(master, text="Enter Password")
        self.inputText1.grid(row = 1, column = 0)

        self.pass1 = DoubleVar()
        self.entrypass1 = Entry(master, textvariable=self.pass1)
        self.entrypass1.grid(row = 1, column = 1)

        self.inputText2 = Label(master, text="Re-Enter Password")
        self.inputText2.grid(row = 2, column = 0)

        self.pass2 = DoubleVar()
        self.entrypass2 = Entry(master, textvariable=self.pass2)
        self.entrypass2.grid(row = 2, column = 1)

        self.TestButton = Button(master, text="Test", command=self.Test)
        self.TestButton.grid(row=4, column=0)

        self.ExitButton = Button(master, text="Exit", command=master.quit)
        self.ExitButton.grid(row=4, column=1)

    def Test(self):
        x = 0

root = Tk()
gui = PasswordTester(root)
root.mainloop()