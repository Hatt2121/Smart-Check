import tkinter
from tkinter import *
from PIL import Image, ImageTk
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import pygame

    
inventory = {}
reader = SimpleMFRC522()
pygame.init()

def start_up():                           
    red_Led = 36
    GPIO.setup(red_Led, GPIO.OUT)

    green_Led = 16
    GPIO.setup(green_Led, GPIO.OUT)
    
    admin = ["Ariel Lee", "Devon Fears"]
    opening = pygame.mixer.Sound('three.wav')
    for i in range(3):
        GPIO.output(red_Led, GPIO.HIGH)
        opening.play()
        time.sleep(.5)
        GPIO.output(red_Led,GPIO.LOW)
        time.sleep(.5)
    GPIO.output(red_Led, GPIO.HIGH)
    print("Please scan key card to open this application.")
    id, text = reader.read()
    a = text.split()
    a.append("extra")
    t = str(a[0] + " " + a[1])
    if t == admin[0] or t == admin[1]:
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
        start_up()

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
        Begin = Button(frame4, text ="Begin", command = root.destroy)
        Begin.grid(row=1, column=2,sticky = W + E, columnspan = 2)

        image1 = Image.open("New Smart Check.png")
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
        

    def createWidgets(self, window): 
        frame1 = Frame(window)
        frame1.pack()

        self.inventory = {}

        self.v1 = IntVar()

        Add_Item = Radiobutton(frame1, text="Process a Single Tag", bg="white", fg = "black", variable=self.v1, value=1, command=self.processRadiobutton)
        Read_Item = Radiobutton(frame1, text = "Process Multiple Tags", bg="white", fg = "black",  variable=self.v1, value=2, command=self.unlim) 

        Add_Item.grid(row=1, column=1)
        Read_Item.grid(row=1, column=2) 

        frame2 = Frame(window)
        frame2.pack()

        self.name = StringVar()
        self.scans = IntVar()
        self.itemInfo = StringVar()
        

        label = Label(frame2, text = "Enter name of the item")
        self.item_name = Entry(frame2, textvariable=self.name, width = 20)

        label2 =Label(frame2, text = "Enter the number of items to be added")
        item_num = Entry(frame2, textvariable = self.scans, width = 10)


        Read_Items = Button(frame2, text ="Read", command = self.readTag)
        Write_Items = Button(frame2, text="Scan", command=self.writeTag)
        Display_Items = Button(frame2, text="Display Inventory", command=self.showInventory)
        Del_Inventory = Button(frame2, text="Clear", command=self.clear)
        Search_Inventory = Button(frame2, text="Compare Inventory", command=self.scan_Tag)


        label.grid(row=2, column=1)
        self.item_name.grid(row=2, column=2)
        
        label2.grid(row=2, column=4)
        item_num.grid(row=2, column=5)

        Read_Items.grid(row=4, column=2, sticky = W + E)
        Write_Items.grid(row=4, column=1, sticky = W + E)
        Display_Items.grid(row=4, column=3,sticky = W + E)
        Del_Inventory.grid(row=4, column=5, sticky = W + E)
        Search_Inventory.grid(row=4, column=4, sticky = W + E)

        self.text = Text(window)  
        self.text.pack(fill = X)
        self.text.insert(END, "Welcome to Smart Check. Inventory Items will appear below.")
        
        self.red_led()
        window.mainloop() 

    def processRadiobutton(self):
        if self.v1.get() == 1:
            self.text.insert(END,"\nEnter item name, scan count, or Item above and press 'Scan' or 'Read'.\n")

        else:
            self.text.insert(END,"\nPlace your item near the scanner and press 'Read'.\n")
            self.unlim()

    def scan_Tag(self):
        gear_fh = open('gear_list.txt', 'r')
        l1 = gear_fh.read()
        b = (l1.split())
        l2 = (list(self.inventory.keys()))
        res = set(b) - set(l2)
        self.text.insert(END,"\nRemaining inventory items.\n{}".format(res))
  

    def readTag(self):
        if self.scans.get() == 0:
            id, text = reader.read()
            a = text.split()
            a.append("extra")
            self.text.insert(END,"\nItem name {}\nItem ID {}\n".format(text, id))

            if len(a) == (2):
                self.inventory[a[0]] = id
                
            else:
                self.inventory[a[0] + " " + a[1]] = id


        else:
            for i in range(self.scans.get()):
                id, text = reader.read()
                a = text.split()
                a.append("extra")
                self.text.insert(END,"\nItem name {}\nItem ID {}\n".format(text, id))

                if len(a) == (2):
                    self.inventory[a[0]] = id

                else:
                    self.inventory[a[0] + " " + a[1]] = id
                time.sleep(2)
                
        self.sound()
        self.redOff()
        self.green_led()
        

    def writeTag(self):
        id, text = reader.read()
        self.text.insert(END,"\nOld Item")
        self.text.insert(END,"\nItem name {}\nItem ID {}\n".format(text, id))
        reader.write(self.name.get())                
        self.sound()
        self.redOff()
        self.green_led()                 
        self.text.insert(END,"\nNew Item\n") 
        self.text.insert(END,"\nItem name {}\nItem ID {}\n".format(self.name.get(), id)) 
        self.inventory.clear()
        self.item_name.delete(0, 'end')


    def showInventory(self):
        self.text.insert(END,"\n")
        self.sound()
        self.redOff()
        self.green_led()
        self.text.insert(END,"Your current Inventory\n")
        gear_fh = open('Your_List.txt', 'w+')
        gear_fh.write(str(self.inventory))
        gear_fh.close()
        for k in self.inventory.keys():
            self.text.insert(END, "Item Name: {} ".format(k) + "\nSN: {} \n".format(self.inventory[k]) + " \n")
            
        for k in self.inventory.keys():
            print(k, ":", self.inventory[k])

    def unlim(self):
        for i in range (10):
            self.readTag()
        self.showInventory()

    def clear(self):
        self.red_flash()
        self.inventory.clear()
        self.text.delete("1.0", "end")
        self.text.insert(END,"Inventory is clear.\n")

                            
#main code
################################
start_up()
SmartCheck()

    
    



