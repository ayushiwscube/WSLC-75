import sqlite3

conn = sqlite3.connect("college_data.db")
cur = conn.cursor()
view_data = cur.execute("""SELECT * FROM STUDENTS1 LIMIT(3)""")
#view_data = cur.execute("""SELECT * FROM STUDENTS1 ORDER BY ROLL_NO DESC""")
# view_data = cur.execute("""SELECT * FROM STUDENTS1 WHERE grade = "8th" """)

for i in view_data:
    print(i)

conn.commit()







#
# import sqlite3
#
# conn = sqlite3.connect("college_data.db")
# cur = conn.cursor()
# l = []
# while True:
#     roll = int(input("enter roll no: "))
#     name = input("enter name: ")
#     grade = input("enter grade: ")
#     email = input("enter email: ")
#     phone = int(input("enter phone number: "))
#
#     t = (roll,name,grade,email,phone)
#     l.append(t)
#     add_data = """INSERT INTO STUDENTS1
#     (ROLL_NO, NAME, GRADE, EMAIL, PHONE_NO)
#     VALUES(?,?,?,?,?)"""
#     repeat = input("repeat again? ")
#     if repeat == "no":
#         break
#
# cur.executemany(add_data, l)
# conn.commit()
#










# import sqlite3
#
# conn = sqlite3.connect("college_data.db")
# cur = conn.cursor()
#
# students = """ CREATE TABLE IF NOT EXISTS STUDENTS1
# (SNO INTEGER PRIMARY KEY AUTOINCREMENT,
# ROLL_NO INTEGER,
# NAME VARCHAR(255) NOT NULL,
# GRADE VARCHAR(255) NOT NULL,
# EMAIL VARCHAR(255) NOT NULL,
# PHONE_NO INTEGER NOT NULL)"""
#
# cur.execute(students)
# conn.commit()
