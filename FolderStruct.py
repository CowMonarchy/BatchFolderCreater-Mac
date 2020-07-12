import os
import tkinter as tk
import tkinter.font as tf
import tkinter.filedialog as tkf



#--Variables--
folderNum = 'None'
folderPath = "                        Select a folder                        "
foldersName = "             Please enter a name             "



#--Functions--
def SelectDirectory():
    dire = tkf.askdirectory()

    dirField.delete(0, 'end')
    dirField.config(fg="white")
    dirField.insert(0, dire)
    
    return dire



def EnterName(*kwargs):
    nameField.delete(0, 'end')
    nameField.config(fg='white')



def CreateFolders():
    global folderNum
    global folderPath
    global foldersName
    global windowVar
    global quanSpn
    
    folderNum = windowVar.get()
    folderPath = dirField.get()
    foldersName = nameField.get()

    if folderNum == 'None':
       windowVar.set('2')
       quanSpn.update()
       folderNum = windowVar.get()


    loops = int(folderNum)
    print(loops)
    fullPath = folderPath + '/' + foldersName


    if not os.path.exists(fullPath) : 
        while loops > 0 :
            os.makedirs(fullPath + f"{loops}", exist_ok=True)
            loops -= 1 
   



#--Windows--
#Main Window
window = tk.Tk()
window.geometry("300x400")
window.title('Folder Creator')
window.attributes('-alpha', 0.97)
window.attributes('-transparent', "true")
window.config(background="#2B2929")
window.maxsize(width=410, height=80)
window.minsize(width=410, height=80)
#Main Window__________________________________________



#Choosing Directory 
dirField = tk.Entry(window, width=32)
dirField.config(highlightthickness=0, font=('San Fransisco', 12), bd=0, bg="#747272", fg="#908E8E")
dirField.insert(0, folderPath)
dirField.place(x=109, y=13)

dirBtn = tk.Button(window, command = lambda : (folderPath := SelectDirectory()), text="Choose")
dirBtn.config(highlightthickness=0, font=('San Fransisco', 12), width=10, bd=100, bg="#737171")
dirBtn.place(x=15, y=13)
#Choosing Directory__________________________________________________________________



#Entering Name
nameField = tk.Entry(window, width=28)
nameField.config(highlightthickness=0, font=('San Fransisco', 12), bd=0, bg="#747272", fg="#908E8E")
nameField.insert(0, foldersName)
nameField.bind("<Button-1>", EnterName)
nameField.place(x=109, y=48)
#Entering Name_______________________________________________________________________________________________


#Selecting Quanity 
windowVar = tk.StringVar(window)

quanSpn = tk.Spinbox(window, textvariable=windowVar, increment=1, width=3, from_=2, to=100, bd=0)
quanSpn.place(x=348, y=45)
#Selecting Quanity_____________________________________________________________________________________________________________



#Creating Folders 
submitBtn = tk.Button(window, text="Create", command = lambda : windowVar.set(CreateFolders()))
submitBtn.config(highlightthickness=0, font=('San Fransisco', 12), width=10, bd=0)
submitBtn.place(x=15, y=48)
#Creating Folders____________________________________________________________________________________________________________________________




window.mainloop()





   



