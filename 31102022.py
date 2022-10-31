import tkinter as tk

window = tk.Tk()
window.geometry("500x360")
window.title("hello world")

l = tk.Label(window,text="enter your name here: ", font="Times 18 italic").place(x = 30, y = 50)
e = tk.Entry(window).place(x = 300, y = 50)
window.mainloop()






# import mysql.connector
# conn = mysql.connector.connect(host="localhost", username = "root", password = "12345", database = "college")
# cur = conn.cursor()
#
# get_data = """select * from students
# where age between 19 and 22"""
#
# cur.execute(get_data)
# data = cur.fetchall()
#
# for i in data:
#     print(i)





# import mysql.connector
# conn = mysql.connector.connect(host="localhost", username = "root", password = "12345", database = "college")
# cur = conn.cursor()
#
# get_data = """select name,branch,city from students
# where branch not in ("eee","mech")"""
#
# cur.execute(get_data)
# data = cur.fetchall()
#
# for i in data:
#     print(i)





# import mysql.connector
# conn = mysql.connector.connect(host="localhost", username = "root", password = "12345", database = "college")
# cur = conn.cursor()
# #sum avg
# get_data = """select count(fees) from fee_deposit"""
#
# cur.execute(get_data)
# data = cur.fetchall()
#
# for i in data:
#     print(i)





# import mysql.connector
# conn = mysql.connector.connect(host="localhost", username = "root", password = "12345", database = "college")
# cur = conn.cursor()
#
# get_data = """select
# students.name as name,
# students.roll_no as roll,
# fee_deposit.fees as fees
# from students,fee_deposit
# where students.roll_no = fee_deposit.roll_no"""
#
# cur.execute(get_data)
# data = cur.fetchall()
#
# for i in data:
#     print(i)



# import mysql.connector
# conn = mysql.connector.connect(host="localhost", username = "root", password = "12345", database = "college")
# cur = conn.cursor()
#
# get_data = """Select \
# students.name as name,\
# students.roll_no as roll,\
# fee_deposit.fees as fees \
# From students \
# INNER JOIN fee_deposit
# ON students.roll_no = fee_deposit.roll_no"""
#
# cur.execute(get_data)
# data = cur.fetchall()
#
# for i in data:
#     print(i)


# import mysql.connector
# conn = mysql.connector.connect(host="localhost", username = "root", password = "12345", database = "college")
# cur = conn.cursor()
#
# get_data = """Select \
# students.name as name,\
# students.roll_no as roll,\
# fee_deposit.fees as fees \
# From students \
# RIGHT JOIN fee_deposit
# ON students.roll_no = fee_deposit.roll_no"""
#
# cur.execute(get_data)
# data = cur.fetchall()
#
# for i in data:
#     print(i)
