








"""
tiny int (3)
integer
big int

text
varchar(255)

date = mm-dd-yyyy
time = hh:mm:ss
datetime = mm-dd-yyyy hh:mm:ss
timestamp =current value
"""


"""
create a database for school
it should have two tables
1 for student data like roll_no, name, age, class, phone number, email
2 for fees_data roll no, name, fee_deposit

press 1 to view the data on the basis of roll_no
press 2 to insert the data
press 3 to delete the data on the basis of roll_no
press 4 to update the data (ask user what do they want to update)
press 5 for principal access
    ask for password
    if password is correct
        display the fee data
    else
        say access denied
"""

















# import sqlite3
#
# conn = sqlite3.connect("college_data.db")
# cur = conn.cursor()
#
# update_data = """UPDATE STUDENTS1 SET GRADE = "5th" WHERE GRADE = "4th" """
#
# cur.execute(update_data)
# conn.commit()

# import sqlite3
#
# conn = sqlite3.connect("college_data.db")
# cur = conn.cursor()
#
# delete_data = """DELETE FROM STUDENTS1 WHERE GRADE = "4th" and ROLL_NO = 1 """
#
# cur.execute(delete_data)
# conn.commit()
