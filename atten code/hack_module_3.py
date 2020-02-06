from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import main_using_csv
import sys
import pyttsx3
import cv2
engine = pyttsx3.init()
#import AAdd
import atten_trail_trail


root = Tk()
img = ImageTk.PhotoImage(Image.open("for_button.jpeg"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

heading = Label(root, text="Enter Your ID", font='arial 18 bold', bg = '#495757', fg = '#46e012').place(x=450,y=400)
#heading1 = Label(root, text="Attendance System", font='arial 15 bold').place(x=650,y=390)
#heading2 = Label(root, text="Powered by Python", font='arial 15 bold',fg='#03fcad').place(x=650,y=430)

root.geometry("1055x600+150+150")
root.title("ATTENDANCE")
root.iconbitmap(r'icon.ico')
#button = Button(root, text="START",width = 20,height = 2, font = 'arial 12 bold', 
  #              command=Show).place(x=120,y=100)
####################database opening#############
def dev ():
    os.system('cmd /c main.html ')

def myCmd ():
     
     mtext = ment.get()
     os.system('cmd /c '+mtext+'.csv ')


def myCmd1 ():
    os.system('cmd /c atten.bat ')

def myCmd2 ():
    os.system('cmd /c kill.bat ')
    #os.system("start C:Users/hp/Desktop/GUI/click.wav")
    
def Add_st():
    top = Tk()
    top.geometry("700x600+150+150")
    top.title("ATTENDANCE")
    heading = Label(top, text="Enter Your name", font='arial 18 bold', bg = '#495757', fg = '#46e012').place(x=250,y=200)
    entry  = Entry(top,textvariable=ment, width = 40,font='Calibri 13').place(x=170,y=250)
    entry_button = Button(top,text = "Capture",command = capt(ment.get()), fg = '#030f21',bg = '#184b96',font = 'arial 13 bold',width = 30,height=2).place(x=200,y=300)

    
    top.mainloop()
    

    



########################################################

    
    
######################

    

    
'''def mhello1():#for database
    mtext = ment.get()
    mLable2 = Label(root, text = "You'r database is ready : " + mtext).pack()
    read_from_db(mtext)
    return'''
################################################################
    
ment = StringVar()
def start():
    
    if ment.get() == "aparna" or ment.get() == "ashwin": 
        atten_trail_trail.main(ment.get())
        root = Tk()
        img = ImageTk.PhotoImage(Image.open("for_button1.jpeg"),master=root)
        panel = Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        
       # heading = Label(root, text="Enter Your ID", font='arial 15 bold', bg = 'white', fg = '#ebb434').place(x=450,y=400)
        #heading1 = Label(root, text="Attendance System", font='arial 15 bold').place(x=650,y=390)
        #heading2 = Label(root, text="Powered by Python", font='arial 15 bold',fg='#03fcad').place(x=650,y=430)
        
        root.geometry("1055x500+150+150")
        root.title("ATTENDANCE")
        root.iconbitmap(r'icon.ico')
           ############################33
       # button2 = Button(root, text="DEVELOPERS",width = 20,height = 2, font = 'arial 12 bold',command = dev).place(x=120,y=200)
        button3 = Button(root, text="DATABASE",width = 20,height = 2, font = 'arial 12 bold',command = myCmd).place(x=120,y=200)
        button4 = Button(root, text="QUIT",width = 20,height = 2, font = 'arial 12 bold',command=myCmd2).place(x=120,y=300)
        
        
       
        
    
        
      
        root.mainloop()

    
    
   
    

    
    '''f1 = Frame(root, width=100,height=500,bg='#03fcad')
    f1.pack(side=LEFT)
    f2 = Frame(root, width=150,height=500,bg='#9403fc')
    f2.pack(side=RIGHT) '''


def mhello():
    mtext = ment.get()
    print(mtext)
    
    if mtext =="aparna" or mtext =="ashwin":
        engine.say("You are logged in")
        engine.runAndWait()
        mLable2 = Label(root, text = "You are logged in",font='arial 15 bold').place(x=460,y=30)
        mLable3 = Label(root, text = "Click on start attendance",font='arial 15 bold').place(x=440,y=60)
        main_using_csv.call('Date : ',mtext)
        #messagebox.showinfo("Title","a Tk messsage yozz")

    
    else:
        
        
        messagebox.showinfo("Error","invalid USER ID")
        
         
         #messagebox.showinfo("Title","a Tk messsage yozz")
        
        

    return

button1 = Button(root, text="START ATTENDANCE",width = 50,height = 2, font = 'arial 12 bold',bg='#ebb434',command = start).place(x=530,y=530)

#button2 = Button(root, text="Add Student",width = 20,height = 2, font = 'arial 9 bold',bg='#ebb434',command = Add_st).place(x=900,y=20)


entry  = Entry(root,show="*",textvariable=ment, width = 70,font='Calibri 15').place(x=170,y=450)
entry_button = Button(root,text = "LOG IN",command = mhello, fg = '#030f21',bg = '#184b96',font = 'arial 13 bold',width = 50,height=2).place(x=10,y=530)

#canvas = Canvas(root,width = 400, height =250,bg='blue').pack()

'''f1 = Frame(root, width=100,height=500,bg='#03fcad')
f1.pack(side=LEFT)
f2 = Frame(root, width=150,height=500,bg='#9403fc')
f2.pack(side=RIGHT)'''
root.mainloop()
