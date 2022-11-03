import matplotlib.pyplot as plt

x = ["part1","part2","part3","part4","part5"]
y = [95,80,75,95,80]
y1= [100,78,45,99,82]

plt.plot(x,y,label = "men",marker = "^")
plt.plot(x,y1, label = "women", marker = "D")
plt.legend(loc = 1)
plt.show()




# import matplotlib.pyplot as plt
#
# x = ["part1","part2","part3","part4","part5"]
# y = [95,80,75,95,80]
# c = ["red", "blue","pink","green","yellow"]
# plt.bar(x,y, color = c, edgecolor = "black",linewidth = 2,linestyle = "-.", alpha = 0.5)
# plt.xlabel("Parts",fontsize = 17)
# plt.ylabel("Popularity", fontsize = 17)
# plt.title("Popularity of different parts of Harry Potter")
# plt.legend("parts")
# plt.show()
















# import tkinter as tk
#
# window = tk.Tk()
#
# l = tk.Label(window,text='choose gender').pack()
#
# def clicked():
#     if (var1.get() == 1) & (var2.get()==0):
#         label = tk.Label(window,text="you have selected Male").pack()
#     elif (var1.get() == 0) & (var2.get()==1):
#         label = tk.Label(window, text="you have selected female").pack()
#     else:
#         label = tk.Label(window, text="you have selected both").pack()
#
# var1 = tk.IntVar()
# var2 = tk.IntVar()
#
# cb = tk.Checkbutton(window,text = "Male", variable=var1, onvalue=1, offvalue=0, command=clicked).pack()
# cb1 = tk.Checkbutton(window,text = "Female", variable=var2, onvalue=1, offvalue=0, command=clicked).pack()
# window.mainloop()






# import mysql.connector
# conn = mysql.connector.connect(host="localhost", username = "root", password = "12345", database = "library")
# cur = conn.cursor()
# l = []
# import tkinter as tk
#
# window = tk.Tk()
# window.geometry("600x400")
#
# def clicked():
#     l = []
#     roll = int(e1.get())
#     name = e2.get()
#     email = e3.get()
#     book = e4.get()
#     ph_no = int(e5.get())
#     t = (roll, name, book, email, ph_no)
#     l.append(t)
#     data = (""" insert into borrowed_books
#         (roll_no,name,book,email,ph_no)
#         values(%s,%s,%s,%s,%s)""")
#     cur.executemany(data, l)
#     conn.commit()
#
#
#
# e1 = tk.Entry(window)
# e2 = tk.Entry(window)
# e3 = tk.Entry(window)
# e4 = tk.Entry(window)
# e5 = tk.Entry(window)
# e1.pack()
# e2.pack()
# e3.pack()
# e4.pack()
# e5.pack()
# b1 = tk.Button(window,text = "click",command=clicked).pack()
#
# window.mainloop()
#
