import os
import tkinter as tk
import tkinter.font as tf
import tkinter.filedialog as tkf

import subprocess as sp



#--Variables--
folderNum = 0
folderPath = "Select a folder"
foldersName = "Please enter a name"



#--Functions--
def SelectDirectory():
    dire = tkf.askdirectory()

    dirField.config(state='normal')
    dirField.delete(0, 'end')
    dirField.insert(0, dire)
    dirField.config(state='readonly')

    return dire
    


def CreateFolders():
    global folderNum
    global folderPath
    global foldersName

    folderNum = windowVar.get()
    folderPath = dirField.get()
    foldersName = nameField.get()


    if folderPath == "Select a folder" : 
        InvokeError("SELECT DIRECTORY ERROR")
        
    
    if foldersName == "Please enter a name" : 
        InvokeError("NAME ERROR")
        

    if folderNum == "None" :
        InvokeError("NUMBER SELECT ERROR")
        


    loops = int(folderNum)
    fullPath = folderPath + '/' + foldersName

    

    if not os.path.exists(fullPath) : 
        while loops > 0 :
            os.makedirs(fullPath + f"{loops}", exist_ok=True)
            loops -= 1 
    else:
        InvokeError("NAME ERROR")
 

def InvokeError(errorType): 
    errWindow = tk.Canvas(window, height=5, width=5)

    if errorType == "SELECT DIRECTORY ERROR" : 
        errWindow.create_text(x=100, y=100, text="Select a folder")
        errWindow.place(x=100, y=100)
        errWindow.config(state='readonly')
        return
        #print("SELECT DIRECTORY ERROR")
    
    if errorType == "NAME ERROR" : 
        errWindow.create_text(x=100, y=100, text="Enter a name")
        errWindow.place(x=100, y=100)
        errWindow.config(state='readonly')
        return
        #print("NAME ERROR")

    if errorType == "NUMBER SELECT ERROR" :
        errWindow.create_text(x=100, y=100, text="Choose a number")
        errWindow.place(x=100, y=100)
        errWindow.config(state='readonly')
        return
        #print ("NUMBER SELECT ERROR")





#--Windows--
#Main Window
window = tk.Tk()
window.geometry("300x400")
window.title('Folder Creator')
window.maxsize(width=300, height=400)
window.minsize(width=300, height=400)
#Main Window____________________________________________________________________________________________________


#Choosing Directory 
dirField = tk.Entry(window, bd=2)
dirField.place(x=100, y=96)
dirField.insert(0, folderPath)
dirField.config(state='readonly')

dirBtn = tk.Button(window, text="Choose Folder", command = lambda : (folderPath := SelectDirectory()))
dirBtn.place(x=0, y=100)
#Choosing Directory______________________________________________________________________________________________ 


#Entering Name
nameLbl = tk.Label(window, text="Name : ")
nameLbl.place(x=0, y=200)

nameField = tk.Entry(window, width=26, bd=2)
nameField.place(x=50, y=198)
nameField.insert(0, foldersName)
nameField.bind("<FocusIn>", lambda a: nameField.delete(0, 'end'))
#Entering Name__________________________________________________________________________________________________


#Selecting Quanity 
quanLbl = tk.Label(window, text="Folder Quantity :")
quanLbl.place(x=0, y=250)

numList = list(range(1, 100))
windowVar = tk.StringVar(window)
windowVar.set(numList[0])

quanDrp = tk.OptionMenu(window, windowVar, *numList)
#quanDrp.config(fg="#191919", bg="#191919", font=("San Francisco",(10)))
quanDrp.place(x=125, y=250)
#Selecting Quanity______________________________________________________________________________________________ 


#Creating Folders 
submitBtn = tk.Button(window, text="Create Folders", command = lambda : windowVar.set(CreateFolders()))
#submitBtn.config(bg = "#191919")
submitBtn.place(x=98, y=300)

#Creating Folders_______________________________________________________________________________________________



#style 
deFont = tf.Font(family="San Francisco", size = 14, )
#Style_______________________________________________________________________________________________



window.mainloop()





   



