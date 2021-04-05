from tkinter import *
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

inventory = {}
reader = SimpleMFRC522()

class SmartCheck:
    def __init__(self):
        window = Tk()
        window.title("Smart Check")
        self.createWidgets(window)
        

    def createWidgets(self, window):
        frame1 = Frame(window)
        frame1.pack()

        self.inventory = {}

        self.v1 = IntVar()

        Add_Item = Radiobutton(frame1, text="Process a Single Tag", bg="white", fg = "black", variable=self.v1, value=1, command=self.processRadiobutton)
        Read_Item = Radiobutton(frame1, text = "Process Fixed Amount of Tags", bg="white", fg = "black",  variable=self.v1, value=2, command=self.unlim) 

        Add_Item.grid(row=1, column=1)
        Read_Item.grid(row=1, column=2) 

        frame2 = Frame(window)
        frame2.pack()

        self.name = StringVar()
        self.scans = IntVar()
        self.itemInfo = StringVar()
        

        label = Label(frame2, text = "Enter name of the item: ")
        self.item_name = Entry(frame2, textvariable=self.name, width = 10)

        label2 =Label(frame2, text = "Enter the number of items to be added: ")
        item_num = Entry(frame2, textvariable = self.scans, width = 10)


        Read_Items = Button(frame2, text ="Read", command = self.readTag)
        Write_Items = Button(frame2, text="Scan", command=self.writeTag)
        Display_Items = Button(frame2, text="Display Inventory", command=self.showInventory)
        Del_Inventory = Button(frame2, text="Clear", command=self.clear)


        label.grid(row=2, column=1)
        self.item_name.grid(row=2, column=2)
        
        label2.grid(row=2, column=3)
        item_num.grid(row=2, column=4)

        Read_Items.grid(row=4, column=2, sticky = W + E)
        Write_Items.grid(row=4, column=1, sticky = W + E)
        Display_Items.grid(row=4, column=3,sticky = W + E)
        Del_Inventory.grid(row=4, column=4, sticky = W + E)

        self.text = Text(window)  
        self.text.pack(fill = X)
        self.text.insert(END, "Welcome to Smart Check. Inventory Items will appear below.")

        window.mainloop() 

    def processRadiobutton(self):
        if self.v1.get() == 1:
            self.text.insert(END,"\nEnter item name, scan count, or Item above and press 'Scan' or 'Read'.\n")

        else:
            self.text.insert(END,"\nPlace your item near the scanner and press 'Read'.\n")
            self.unlim()

                          

    def readTag(self):
        if self.scans.get() == 0:
            id, text = reader.read()
            self.text.insert(END,"\nItem name {}\nItem ID {}\n".format(text, id))
            self.inventory[text] = id

        else:
            for i in range(self.scans.get()):
                id, text = reader.read()
                self.text.insert(END,"\nItem name {}\nItem ID {}\n".format(text, id))
                self.inventory[text] = id
                time.sleep(1)
        

    def writeTag(self):
        self.text.insert(END,"\nPlace tag to written near the scanner\n")
        id, text = reader.read()
        del self.inventory[text]
        text = self.item_name.get()
        reader.write(text)
        id, text = reader.read()
        self.text.insert(END,"\nItem name {}\nItem ID {}\n".format(text, id))
        self.inventory[text] = id

    def showInventory(self):
        self.text.insert(END,"\n")
        for k in self.inventory.keys():
            self.text.insert(END, k, ":\n", self.inventory[k], "\n")
            self.text.insert(END,"\n", self.inventory[k], "\n")
            
        for k in self.inventory.keys():
            print(k, ":", self.inventory[k])

    def unlim(self):
        for i in range (25):
            id, text = reader.read()
            print(id)
            print(text)
            self.inventory[text] = id
        self.showInventory()

    def clear(self):
        self.inventory.clear()
        self.text.insert(END,"\nInventory is clear\n")

                
          

                        
#main code
################################
SmartCheck()
    
    



