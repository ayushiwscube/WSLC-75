"""
insert_data

display_data
"""












# import tkinter as tk
# from PIL import Image, ImageTk
# import random
#
# window = tk.Tk()
# window.geometry("500x360")
# window.title("Dice Roll")
#
#
# dice = ["dice1.png","dice2.png","dice3.png","dice4.png","dice5.png","dice6.png"]
# image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
# image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
#
# label1 = tk.Label(window,image=image1)
# label2 = tk.Label(window,image=image2)
#
# label1.image = image1
# label2.image = image2
#
# label1.place(x = 40, y = 100)
# label2.place(x = 300, y = 100)
#
# def dice_roll():
#     image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
#     label1.configure(image = image1)
#     label1.image = image1
#
#     image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
#     label2.configure(image = image2)
#     label2.image = image2
# button = tk.Button(window,text="ROLL",bg = "green", fg = "white",font= "Times 20 bold",command=dice_roll)
# button.place(x = 200, y = 0)
# window.mainloop()


# from currency_converter import CurrencyConverter
#
# c = CurrencyConverter()
# print(c.convert(12,"USD","INR"))
# from tkinter import *
#
# window = Tk()
#
# window.geometry("600x400")
# window.title("Currency Converter")
#
# def clicked():
#     amount = int(e1.get())
#     cur1 = e2.get()
#     cur2 = e3.get()
#     data = (c.convert(amount,cur1,cur2))
#     label = Label(window,text=data,font="Times 20 bold").place(x = 250, y = 290)
#
#
# l1 = Label(window,text="enter amount: ",font="Times 20 bold").place(x = 30, y =40)
# e1 = Entry(window)
#
# l2 = Label(window,text="enter your currency: ",font="Times 20 bold").place(x = 30, y =100)
# e2 = Entry(window)
#
# l3 = Label(window,text="enter desried currency: ",font="Times 20 bold").place(x = 30, y =160)
# e3 = Entry(window)
#
# b1 = Button(window,text="click",command=clicked).place(x = 280, y = 230)
# e1.place(x = 250, y = 50)
# e2.place(x = 300, y = 110)
# e3.place(x = 330, y = 170)
# window.mainloop()













# from tkinter import *
#
#
# window = Tk()
#
# var = IntVar()
#
# def clicked():
#     l2 = Label(window, text="")
#     l2.pack()
#     if (var.get())==3:
#         l2.configure(text="correct answer")
#     else:
#         l2.configure(text="incorrect answer")
#
#
#
# l1 = Label(window,text="what is the capital of India? ").pack()
# r1 = Radiobutton(window, text= "Mumbai", variable=var, value=1,command=clicked)
# r2 = Radiobutton(window, text= "Jaipur", variable=var, value=2,command=clicked)
# r3 = Radiobutton(window, text= "New Delhi", variable=var, value=3,command=clicked)
# r4 = Radiobutton(window, text= "Bangalore", variable=var, value=4,command=clicked)
#
# r1.pack()
# r2.pack()
# r3.pack()
# r4.pack()
#
#
# window.mainloop()











# import tkinter as tk
# from tkinter import *
#
# window = tk.Tk()
#
# iv = IntVar(window, name = "int")
# sv = StringVar(window, name = "abc")
# bv = BooleanVar(window, name = "bool")
# dv = DoubleVar(window,name="float")
#
# #set function
# window.setvar(name="int",value=100)
# window.setvar(name="abc",value="hello")
# window.setvar(name="bool",value=True)
# window.setvar(name="float",value=1.23)
#
# a = iv.get()
# print(a)
