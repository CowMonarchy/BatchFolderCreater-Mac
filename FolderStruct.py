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

    dirField.config(state='normal')
    dirField.delete(0, 'end')
    dirField.insert(0, dire)
    dirField.config(state='readonly')

    return dire



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
#Main Window____________________________________________________________________________________________________



#Choosing Directory 
dirField = tk.Entry(window, width=31)
dirField.place(x=109, y=10)
dirField.insert(0, folderPath)
dirField.config(state='readonly', bd=0, bg="red")

dirBtn = tk.Button(window, command = lambda : (folderPath := SelectDirectory()), text="Choose")
dirBtn.config(highlightthickness=0, font=('San Fransisco', 12), width=10, bd=100, bg="red")
dirBtn.place(x=15, y=13)
#Choosing Directory______________________________________________________________________________________________ 



#Entering Name
nameField = tk.Entry(window, width=25)
nameField.config(bd=0)
nameField.place(x=109, y=45)
nameField.insert(0, foldersName)
nameField.bind("<FocusIn>", lambda a: nameField.delete(0, 'end'))
#Entering Name__________________________________________________________________________________________________



#Selecting Quanity 
windowVar = tk.StringVar(window)

quanSpn = tk.Spinbox(window, textvariable=windowVar, increment=1, width=3, from_=2, to=100, bd=0)
quanSpn.place(x=348, y=45)
#Selecting Quanity______________________________________________________________________________________________ 



#Creating Folders 
submitBtn = tk.Button(window, text="Create", command = lambda : windowVar.set(CreateFolders()))
submitBtn.config(highlightthickness=0, font=('San Fransisco', 12), width=10, bd=0)
submitBtn.place(x=15, y=48)
#Creating Folders_______________________________________________________________________________________________




window.mainloop()





   



