from tkinter import *
from tkinter import ttk


window = Tk()
window.title('Data Entry Form')
window.geometry("470x340")

#title
title = Label(window, text="Data Entry Form",font="Calibre 20 bold")
title.grid(row=0, column=0, pady=10, columnspan=4)

#first last name
fname_label = Label(window, text="First Name")
fname_label.grid(row=1, column=0, padx=10, sticky="w")

fname_entry=Entry(window, width=20)
fname_entry.grid(row=1, column=1)

Lname_label = Label(window, text="Last Name")
Lname_label.grid(row=1, column=2, padx=10)

Lname_entry=Entry(window, width=20)
Lname_entry.grid(row=1, column=3, pady=5)

#dateofbirth
birth_label = Label(window, text="Birth Date")
birth_label.grid(row=2, column=0, padx=10, sticky="w")

birth_entry=Entry(window, width=20)
birth_entry.grid(row=2, column=1, pady=5, columnspan=3, sticky="we")

#gender
Gender = Label(window, text="Gender")
birth_label.grid(row=2, column=0, padx=10, sticky="w")
gender = StringVar()
gender.set("none")
male = Radiobutton(window , text="Male", variable=gender,value="Male")
male.grid(row=3, column=1, pady=5, sticky="w")

female = Radiobutton(window , text="Female", variable=gender, value="Female")
female.grid(row=3, column=2, pady=5, sticky="w")
#Contry
country_label = Label(window, text="Country")
country_label.grid(row=2, column=0, padx=10, sticky="w")

country_choices=ttk.Combobox(window, width=20, values=["Mauritania","Algeria","Senegal","Morroco","Mali"])
country_choices.grid(row=4, column=1, pady=5, columnspan=3, sticky="we")

#Address
text_label = Label(window, text="Address")
text_label.grid(row=5, column=0, padx=10, sticky="nw")

text_entry= Text(window, width=20, height=5)
text_entry.grid(row=5, column=1, pady=5, columnspan=3, sticky="we")
#Buttons
def record():
    firstname= fname_entry.get()
    lastname= Lname_entry.get()
    gender= Gender.get()
    birthdate= birth_entry.get()
    country= country_choices.get()
    address= text_entry.get("1.0","end-1c")
    text= firstname + "," + lastname + "," + gender + "," + birthdate + "," + country + "," + address + "\n"
    with open(r"C:\Users\PC\Desktop\file.csv", "a") as file :
        file.write(text)
        clear_all()
def clear_all():
    fname_entry.delete(0, "end")
    Lname_entry.delete(0, "end")
    gender.set("none")
    birth_entry.delete(0, "end")
    country_choices.delete(0, "end")
    text_entry.delete("1.0", "end")
    fname_entry.focus_set()
save = Button(window, text="save", command=record)
save.grid(row=6, column=1, padx=10, sticky="e", ipadx=10)

clear = Button(window, text="Clear", command=clear_all)
clear.grid(row=6, column=2, padx=10, sticky="w", ipadx=10)











window.mainloop()