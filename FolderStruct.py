#!/usr/bin/env python3
import os
import sys
import tkinter as tk
import tkinter.font as tf
import tkinter.filedialog as tkf



#--Variables--
folderNum = 'None'
foldersName = "             Please enter a name             "
folderPath = sys.argv[1]



#--Functions--
def EnterName(*kwargs):
    nameField.delete(0, 'end')
    nameField.config(fg='white')
    submitBtn.config(state='disabled')



def ChooseQuan(*kwargs):
    quanSpn.config(fg='white')



def ConditionCheck(*kwargs):
    global folderNum
    global folderPath
    global foldersName
    global windowVar
    global quanSpn
    
    folderNum = windowVar.get()
    foldersName = nameField.get()

    if folderNum.isdigit() == False:
        submitBtn.config(state='disabled')
        return
    if  len(foldersName) == 0 or foldersName.isspace() or foldersName == "             Please enter a name             " :
        submitBtn.config(state='disabled')
        return
    

    submitBtn.config(state='normal')



def CreateFolders():
    global folderNum
    global folderPath
    global foldersName
    global windowVar
    global quanSpn
    
    folderNum = windowVar.get()
    foldersName = nameField.get()


    loops = int(folderNum)
    fullPath = folderPath + '/' + foldersName


    if not os.path.exists(fullPath) : 
        while loops > 0 :
            os.makedirs(fullPath + f"{loops}", exist_ok=True)
            loops -= 1 


    window.destroy()
   



#--Windows--
#Main Window
window = tk.Tk()
window.geometry("300x400")
window.title('Folder Creator')
window.attributes('-alpha', 0.97)
window.attributes('-transparent', 'true')
window.config(background="#2B2929")
window.maxsize(width=410, height=35)
window.minsize(width=410, height=35)
#Main Window__________________________________________



#Entering Name
nameField = tk.Entry(window, width=28)
nameField.config(highlightthickness=0, font=('San Fransisco', 12), bd=0, bg='#747272', fg='#908E8E')
nameField.insert(0, foldersName)
nameField.bind("<Button-1>", EnterName)
nameField.bind("<Leave>", ConditionCheck)
nameField.place(x=109, y=9)
#Entering Name_______________________________________________________________________________________________



#Selecting Quanity 
windowVar = tk.StringVar(window)

quanSpn = tk.Spinbox(window, textvariable=windowVar, highlightthickness=0)
quanSpn.config(increment=1, width=3, from_=2, to=100, bg='#747272', fg='#908E8E', bd=0)
quanSpn.bind("<Button-1>", ChooseQuan)
quanSpn.bind("<Leave>", ConditionCheck)
quanSpn.place(x=348, y=8)
#Selecting Quanity_____________________________________________________________________________________________________________



#Creating Folders 
submitBtn = tk.Button(window, text='Create', command = lambda : windowVar.set(CreateFolders()))
submitBtn.config(highlightthickness=0, state='disabled', font=('San Fransisco', 12), width=10, bd=0)
submitBtn.place(x=15, y=8)
#Creating Folders____________________________________________________________________________________________________________________________




window.mainloop()





   



