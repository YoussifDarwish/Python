from customtkinter import *
from tkinter import messagebox


master = CTk()
master.title("Weather Converter")
master.geometry("500x500")
master.resizable(width= False, height= True)


def  fahrenheit_to_celsius():
    
    global degree
    degree = inputbutton.get()

    result = (int(degree)-32) * 5/9
    degreelabel.configure(text = f"{result} F")

inputbutton = CTkEntry(master, placeholder_text = "enter a number", width= 350)
inputbutton.pack(padx = 50, pady = 40)

convertbutton = CTkButton(master, text = "convert to celsius", command = fahrenheit_to_celsius)
convertbutton.pack(padx = 50, pady = 150)

degreelabel = CTkLabel(master, text= "")
degreelabel.pack(padx = 50, pady = 20)




master.mainloop()