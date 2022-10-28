







# import mysql.connector
# conn = mysql.connector.connect(host="localhost", username = "root", password = "12345", database = "library")
# cur = conn.cursor()
# new_data = input("enter updated book name: ")
# prev_data = input("enter prev book name: ")
#
# t = (new_data,prev_data)
# update_data = """update borrowed_books set book = %s where book = %s """
# cur.execute(update_data, t)
# conn.commit()



#import mysql.connector
# conn = mysql.connector.connect(host="localhost", username = "root", password = "12345", database = "library")
# cur = conn.cursor()
# subject = input("enter book name: ")
# t = (subject,)
# delete_data = """delete from borrowed_books where book = %s """
#
# cur.execute(delete_data,t)
# conn.commit()




# import mysql.connector
# conn = mysql.connector.connect(host="localhost", username = "root", password = "12345", database = "library")
# cur = conn.cursor()
# # get_data = "select * from borrowed_books"
# # get_data = "select name,book from borrowed_books"
# # get_data = """select * from borrowed_books where book = "physics" """
# get_data = """select * from borrowed_books where book like "%y%" and ph_no like "%77%" """
#
# cur.execute(get_data)
# data = cur.fetchall()
#
# for i in data:
#     print(i)













# import mysql.connector
# conn = mysql.connector.connect(host="localhost", username = "root", password = "12345", database = "library")
# cur = conn.cursor()
# l = []
# while True:
#     roll= int(input("enter roll no: "))
#     name = input("enter name: ")
#     book = input("enter book name: ")
#     email = input("enter email: ")
#     ph_no = input("enter phone number: ")
#     t = (roll,name,book,email,ph_no)
#     l.append(t)
#     data = (""" insert into borrowed_books
#     (roll_no,name,book,email,ph_no)
#     values(%s,%s,%s,%s,%s)""")
#
#
#     repeat = input("repeat again? ")
#     if repeat == "no":
#         break
# cur.executemany(data,l)
# conn.commit()














# import mysql.connector
# conn = mysql.connector.connect(host="localhost", username = "root", password = "12345", database = "library")
# cur = conn.cursor()
#
# cur.execute(""" insert into borrowed_books
# (roll_no,name,book,email,ph_no)
# values(1,"Krishna","maths","krishna@gmail.com",987654321)""")
#
# conn.commit()









# import mysql.connector
# conn = mysql.connector.connect(host="localhost", username = "root", password = "12345", database = "library")
# cur = conn.cursor()
#
# data = """ create table if not exists borrowed_books
# (roll_no int(5) primary key,
# name varchar(30) not null,
# book varchar(20) not null,
# email varchar(30) not null,
# ph_no int(10) not null)"""
#
# cur.execute(data)




# import mysql.connector
# conn = mysql.connector.connect(host="localhost", username = "root", password = "12345", database = "library")
# cur = conn.cursor()
#
# cur.execute("""create database library""")
