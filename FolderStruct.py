import os
import tkinter as tk
import subprocess as sp
import tkinter.ttk as ttk
import tkinter.font as tf
import tkinter.filedialog as tkf



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
window.attributes('-alpha', 0.97)
window.attributes('-topmost', "true")
window.attributes('-transparent', "true")
window.config(background="#25272A")
window.maxsize(width=300, height=400)
window.minsize(width=300, height=400)
#Main Window____________________________________________________________________________________________________



#style 
style = ttk.Style()
style.theme_use("aqua")

style.configure('TEntry', foreground='white', background='#818284', bd=9)
style.configure('TButton', foreground='black', font=('San Fransisco', 12), bd=0)
#Style_______________________________________________________________________________________________



#Choosing Directory 
dirField = tk.Entry(window)
dirField.place(x=105, y=10)
dirField.insert(0, folderPath)
dirField.config(state='readonly')

dirBtn = tk.Button(window, text="Choose", command = lambda : (folderPath := SelectDirectory()))
dirBtn.config(width=10, bd=0, highlightthickness=0, font=('San Fransisco', 12))
dirBtn.place(x=8, y=15)
#Choosing Directory______________________________________________________________________________________________ 



#Entering Name
nameLbl = tk.Label(window, text="Name : ")
nameLbl.place(x=0, y=200)

nameField = tk.Entry(window, width=26)
nameField.config(bd=0)
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
quanDrp.place(x=125, y=250)
#Selecting Quanity______________________________________________________________________________________________ 



#Creating Folders 
submitBtn = tk.Button(window, text="Create Folders", command = lambda : windowVar.set(CreateFolders()))
submitBtn.place(x=98, y=300)
#Creating Folders_______________________________________________________________________________________________




window.mainloop()





   



