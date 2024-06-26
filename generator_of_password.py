import random
import pyperclip
from tkinter import *
from tkinter.ttk import *import random
import pyperclip
from tkinter import *
from tkinter.ttk import *
import os
import datetime
import string

def generate_password():
    entry.delete(0, END)
    length = var_length.get()
    chars = {
        1: string.ascii_lowercase,
        0: string.ascii_uppercase,
        3: string.ascii_letters + string.digits + "!@#%§£$^ùéè*()"
    }
    
    char_pool = chars.get(var_strength.get())
    if not char_pool:
        return
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    entry.insert(0, password)

def copy_to_clipboard():
    random_pwd = entry.get()
    pyperclip.copy(random_pwd)
    
    with open("psd_generated.txt", "a") as file:
        date = datetime.datetime.now()
        file.write(f"Mot de passe: {random_pwd}\t{date}\n")

# Interface utilisateur
root = Tk()

var_strength = IntVar(value=1)
var_length = IntVar(value=8)

root.title("Automatic password generator")

Label(root, text="Mot de passe:").grid(row=0, column=0, padx=5, pady=5)
entry = Entry(root, width=30)
entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

Label(root, text="Taille:").grid(row=1, column=0, padx=5, pady=5)
combo = Combobox(root, textvariable=var_length, values=list(range(8, 33)))
combo.grid(row=1, column=1, padx=5, pady=5)

Button(root, text="Générer", command=generate_password).grid(row=0, column=3, padx=5, pady=5)
Button(root, text="Copier", command=copy_to_clipboard).grid(row=0, column=4, padx=5, pady=5)

Radiobutton(root, text="Faible", variable=var_strength, value=1).grid(row=1, column=2, padx=5, pady=5)
Radiobutton(root, text="Moyen", variable=var_strength, value=0).grid(row=1, column=3, padx=5, pady=5)
Radiobutton(root, text="Super_pro", variable=var_strength, value=3).grid(row=1, column=4, padx=5, pady=5)

root.mainloop()

import os
import datetime 


def faible():
    entry.delete(0, END)

    length = var1.get()
    miniscule = "abcdefghijklmnopqrstuvwxyz"
    majuscule = miniscule.upper()
    num = "0123456789"
    charac = "!@#%§£$^ùéè*()"
    min_maj_num_char = miniscule + majuscule + charac + num
    password  =""

    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(miniscule)
        return password
    elif var.get() == 0:
        for i  in range(0, length):
            password += random.choice(majuscule)
        return password
    elif var.get() == 3:
        for i  in range(0, length):
            password += random.choice(min_maj_num_char)
        return password
    else :
        print("S'il  vous plait! veuillez choisir une option")
    
def generateur():
        pwd1 = faible()
        entry.insert(10,pwd1)

def copier1():
        random_pwd = entry.get()
        pyperclip.copy(random_pwd)

        #mettre le mot de passe generer dans un fichier

        d = open("psd_generated.txt", "a")
        date = datetime.datetime.now()
        d.write("Mot de passe: "+random_pwd+"\t"+str(date)+"\n")
        d.close()


        
root = Tk()

var = IntVar(root)
var1 = IntVar(root)

root.title("Automatic password generator")

random_pwd = Label(root, text =" mot de passe")
random_pwd.grid(row = 0)
entry = Entry(root)
entry.grid(row = 0, column = 1)
c_label = Label(root, text= " Taille")
c_label.grid(row = 1)

copy_button = Button(root, text = "Copier", command=copier1)
copy_button.grid(row = 0, column=2)
generate_button = Button(root, text = "Générer", command=generateur)
generate_button.grid(row=0, column=3)

radio_faible = Radiobutton(root, text="Faible", variable= var ,value=1)
radio_faible.grid(row=1, column=2, sticky="E")
radio_moyen = Radiobutton(root, text = "Moyen", variable = var, value = 0)
radio_moyen.grid(row=1, column=3, sticky="E")
radio_dificile = Radiobutton(root, text = "Super_pro", variable=var,  value=3)
radio_dificile.grid(row = 1, column= 4, sticky="E")

combo = Combobox(root, textvariable= var1)
combo["values"] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind("<<ComboboxSelected>>2")
combo.grid(column=1, row=1)

root.mainloop()




