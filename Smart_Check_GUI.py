#########################################################################################################
#GROUP: 1
#GROUP MEMEBERS: Ariel Lee, Devon Fears
#DATE: 4/21/2021
#DESCRIPTION: Smart Check is an RFID based invnetory that allows users to send
# and recieve inventory list through email. The application allows end users to
# read tags to view its embbed information and write new id names to tags.
# Additonally, users can compare their currently scanned inventory to a recieved
# list. Importing a list saves it to text file in the same folder as the program.
# User can also clear their text windows and inventory at any time. Their current
# inventory can be displayed on the screen. The can select how many items to scan
# at any given time or scan 10 in rapid succession. Tag information is stored within
# a dicitonary. Once the dicitonary keys are stored in a list, they can be compared
# to a recieved list and common items are removed and remaining items are displayed for the user.
# Sounds and lights were used to add visual and auditory cues for users to know
# when succesfful scan take place.
##################################################################################################

# A number of different libraries were imported to functionalities like adding sound,
# delays between operations, image manipulation, and the library for the RFID reader
# and emailing system.

import tkinter
from tkinter import *
from PIL import Image, ImageTk
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import pygame
import mailing as m

    
# Allows the Rpi to recognise the RFID reader
reader = SimpleMFRC522()
#Initializes pygame so that sounds can be played
pygame.init()

# This function runs to first allow the reader to settle and only permit authorized
# users access.
def start_up():
    #Sets the pin for the red led
    red_Led = 36
    GPIO.setup(red_Led, GPIO.OUT)

    #Sets the pin for the green led
    green_Led = 16
    GPIO.setup(green_Led, GPIO.OUT)
    
    # Authurized users
    admin = ["Ariel Lee", "Devon Fears"]
    opening = pygame.mixer.Sound('three.wav') # Sets a sound file to a variable

    # Plays to alert users that the programing is running and requests an authorized tag
    for i in range(3):
        GPIO.output(red_Led, GPIO.HIGH)
        opening.play()
        time.sleep(.5)
        GPIO.output(red_Led,GPIO.LOW)
        time.sleep(.5)
    GPIO.output(red_Led, GPIO.HIGH)
    print("Please scan key card to open this application.")
    id, text = reader.read() # Tuple that stores information scanned from the tag
    a = text.split()# The reader adds extra spaces to tag names. Names are saved in a list
    a.append("extra")# Some names have one or two words in them and this makes comparison eaiser
    t = str(a[0] + " " + a[1]) # Combines names 
    if t == admin[0] or t == admin[1]: # if combined names equal the first or second index of the admin list. Entrance is permitted
        GPIO.output(red_Led,GPIO.LOW)
        correct = pygame.mixer.Sound('two.wav')
        correct.play()
        GPIO.output(green_Led, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(green_Led,GPIO.LOW)
        time.sleep(.5)
        print("Welcome to Smart Check {} {}".format(a[0],a[1]))
        LoadScreen()

    else:
        start_up() # If names do not match the start_up() function goes again

# Initializes the start up window
class LoadScreen:
    def __init__(self):
        root = Tk()
        root.title("Smart Check")
        self.Widgets(root)

    def Widgets(self,root):
        frame0 = Frame(root, width=500, height=295)
        frame0.pack()
        frame4 = Frame(root)
        frame4.pack()
        Begin = Button(frame4, text ="Begin", command = root.destroy) #Once being is selected the root frame is destroyed and the next GUI is created
        Begin.grid(row=1, column=2,sticky = W + E, columnspan = 2)

        image1 = Image.open("New Smart Check.png") #pulls the Smart Check logo
        test = ImageTk.PhotoImage(image1)

        label1 = tkinter.Label(image=test)
        label1.image = test

        label1.place(x=250, y=120, anchor="center")

        root.mainloop()

class SmartCheck:
    def __init__(self):
        window = Tk()
        window.title("Smart Check")
        self.createWidgets(window)

    def createWidgets(self, window):
        # Sets the frame for the radiobuttons
        frame1 = Frame(window)
        frame1.pack()

        self.inventory = {}

        self.v1 = IntVar()

        Add_Item = Radiobutton(frame1, text="Process a Single Tag", bg="white", fg = "black", variable=self.v1, value=1, command=self.processRadiobutton)
        Read_Item = Radiobutton(frame1, text = "Process Multiple Tags", bg="white", fg = "black",  variable=self.v1, value=2, command=self.unlim) 

        Add_Item.grid(row=1, column=1)
        Read_Item.grid(row=1, column=2) 

        # Sets the frame for the labels
        frame2 = Frame(window)
        frame2.pack()

        # Sets the frame for the buttons
        frame3 = Frame(window)
        frame3.pack()

        self.name = StringVar()
        self.scans = IntVar()
        self.itemInfo = StringVar()
        

        label = Label(frame2, text = "New item name")
        self.item_name = Entry(frame2, textvariable=self.name, width = 20)

        label2 =Label(frame2, text = "Enter the number of items to be added")
        item_num = Entry(frame2, textvariable = self.scans, width = 10)

        # All the buttons the user can interact which are all tied to functions
        Read_Items = Button(frame3, text ="Read", command = self.readTag)
        Write_Items = Button(frame3, text="Scan", command=self.writeTag)
        Display_Items = Button(frame3, text="Display Inventory", command=self.showInventory)
        Del_Inventory = Button(frame3, text="Clear", command=self.clear)
        Search_Inventory = Button(frame3, text="Compare Inventory", command=self.scan_Tag)
        Import_List = Button(frame3, text ="Import List", command = self.pull_list)
        Send_List = Button(frame3, text = "Send List", command = self.send_list)

        label.grid(row=2, column=2)
        self.item_name.grid(row=2, column=3)
        
        label2.grid(row=2, column=4)
        item_num.grid(row=2, column=5)

        Read_Items.grid(row=1, column=2, sticky = W + E)
        Write_Items.grid(row=1, column=1, sticky = W + E)
        Display_Items.grid(row=1, column=3,sticky = W + E)
        Del_Inventory.grid(row=1, column=7, sticky = W + E)
        Search_Inventory.grid(row=1, column=5, sticky = W + E)
        Import_List.grid(row=1, column=6, sticky = W + E)
        Send_List.grid(row=1, column=4, sticky = W + E) 

        # Creates the text window to display inventory items
        self.text = Text(window)  
        self.text.pack(fill = X)
        self.text.insert(END, "Welcome to Smart Check. Inventory Items will appear below.")

        # Set the red led to on until the user does an action
        self.red_led()
        window.mainloop()
        
    #Instructions for the user on how to proceed based on the option selected
    def processRadiobutton(self):
        if self.v1.get() == 1:
            self.text.insert(END,"\nEnter item name scan count above and press 'Scan' or 'Read'.\n")

        else:
            self.text.insert(END,"\nPlace your item near the scanner and press 'Read'.\n")
            self.unlim()
            
    # Compares items in scnanned inventory to those downloaded from an email
    def scan_Tag(self):
        gear_fh = open('downloaded_list.txt', 'r')
        l1 = gear_fh.read()
        b = (l1.split("\n"))
        l2 = (list(self.inventory.keys()))
        res = set(b) - set(l2)# Names that are the same removed
        self.text.insert(END,"\nRemaining inventory items.\n{}".format(res))# Displays the result from comparing the two sets
  

    def readTag(self):
        if self.scans.get() == 0:
            id, text = reader.read()
            a = text.split()
            a.append("extra") # items names can be one or two words. Bases on the lenght of the split text list, this if-else determined which indexes to add to the inventory.
            self.text.insert(END,"\nItem name {}\nItem ID {}\n".format(text, id))# Displays the inventory informaition

            if len(a) == (2):
                self.inventory[a[0]] = id #Items with a single word as its name
                
            else:
                self.inventory[a[0] + " " + a[1]] = id#Items with two words as its name


        else:
            for i in range(self.scans.get()):#Fixed number of scans selected
                id, text = reader.read()
                a = text.split()
                a.append("extra")
                self.text.insert(END,"\nItem name {}\nItem ID {}\n".format(text, id))

                if len(a) == (2):
                    self.inventory[a[0]] = id# Adds the scanned item to the dicitonary

                else:
                    self.inventory[a[0] + " " + a[1]] = id # Adds the scanned item to the dicitonary
                time.sleep(2)
                
        self.sound()
        self.redOff()
        self.green_led()
        
    def writeTag(self):
        id, text = reader.read()# Reads the tag to dislay the previous name
        self.text.insert(END,"\nOld Item")
        self.text.insert(END,"\nItem name {}\nItem ID {}\n".format(text, id))
        reader.write(self.name.get())                
        self.sound()
        self.redOff()
        self.green_led()                 
        self.text.insert(END,"\nNew Item\n") 
        self.text.insert(END,"\nItem name {}\nItem ID {}\n".format(self.name.get(), id)) 
        self.inventory.clear()# Prevents duplicate items with different names but different SN from being added to the dictionary
        self.item_name.delete(0, 'end')# Clears the entry box to prevent read tags from adopting unintedned names

    def showInventory(self):
        self.text.insert(END,"\n") #prevent inventory from appearing on the same line as a previous entry
        self.sound()
        self.redOff()
        self.green_led()
        self.text.insert(END,"Your current Inventory\n")
        gear_fh = open('return_attachment.txt', 'w+')
        gear_fh.write(str(self.inventory)) #Writes scanned items to an attachment that can be sent
        gear_fh.close()
        for k in self.inventory.keys():
            self.text.insert(END, "Item Name: {} ".format(k) + "\nSN: {} \n".format(self.inventory[k]) + " \n")
            
    #Calls the return attachment function. Takes an email and an inventory as an arguement.
    def send_list(self):
        m.return_attachment("ariel.j.lee@outlook.com", self.inventory)
        self.text.insert(END, "\nYour list has been sent!\n")
        self.showInventory()
    
    # Allows tags to be scanned in rapid succession and displays items scanned at the end. Only adds unique items to the dictionary.
    def unlim(self):
        for i in range (10):
            self.readTag()
        self.showInventory()

    def clear(self):
        self.red_flash()# Alerts user that the list is being cleared
        self.inventory.clear()# Clears the inventory
        self.text.delete("1.0", "end")# Clears the text window
        self.text.insert(END,"Inventory is clear.\n")
        
    # Imports the list from an email and displays its contents in the text window
    def pull_list(self):
        m.download_attachment()
        gear_fh = open('downloaded_list.txt', 'r')
        uncompleted_items = gear_fh.read()
        uncompleted_items  = uncompleted_items.replace("\n", " ")
        self.text.insert(END,"\nAssigned list: {}\n".format(uncompleted_items))
        
    # The remaining functions are auditory and visuals cues for the user
    def sound(self):
        correct = pygame.mixer.Sound('two.wav')
        correct.play()
        print("Sound played")

    def red_led(self):
        red_Led = 36
        GPIO.setup(red_Led, GPIO.OUT)
        GPIO.output(red_Led, GPIO.HIGH)

    def red_flash(self):
        correct = pygame.mixer.Sound('three.wav')
        red_Led = 36
        GPIO.setup(red_Led, GPIO.OUT)
        for i in range (3):
            correct.play() 
            GPIO.output(red_Led, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(red_Led,GPIO.LOW)
            time.sleep(.5)

    def redOff(self):
        red_Led = 36
        GPIO.setup(red_Led, GPIO.OUT)
        GPIO.output(red_Led, GPIO.LOW)

    def green_led(self):
        green_Led = 16
        GPIO.setup(green_Led, GPIO.OUT)
        GPIO.output(green_Led, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(green_Led,GPIO.LOW)
        time.sleep(.5)        
                                    
#main code
################################
start_up()
SmartCheck()

    
    



