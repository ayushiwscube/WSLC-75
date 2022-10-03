db = {"India":"New delhi", "Australia":"Sydney"}

db["Australia"] = "canberra"

print(db)



# company = {"Name":["John","Lisa","Peter"],
#            "emp_id": [12345,12346,12347]}
#
# print(company)
#
# for i,j in company.items():
#     print (i,"-",j)


# company = {"employee1":{"Name":"John","Emp_id":12345,"gender":"male"},
#            "employee2":{"Name":"Peter","Emp_id":12346,"gender":"male"},
#            "employee3":{"Name":"Lisa","Emp_id":12347,"gender":"female"}}
#
# print (company["employee2"]["Emp_id"])
# print(company["employee3"]["Name"])
#
# for i,j in company.items():
#     print(i,j)




# db = {"India":"new delhi"}
# del db["India"]
# print (db)



"""create empty database

press 1 to add data
press 2 to view value data
press 3 to delete data
press 4 to view complete data"""
#
# db = {}
#
# while True:
#     choice = int(input("enter your choice from 1-4: "))
#     if choice == 1:
#         country = input('enter country name: ')
#         capital = input("enter capital name: ")
#         db[country] = capital
#         print("data added")
#
#     elif choice == 2:
#         country = input("enter country name: ")
#         print(db[country])
#
#
#     elif choice == 3:
#         country = input("enter country name: ")
#         del db[country]
#         print(db)
#
#     elif choice  == 4:
#         for x,y in db.items():
#             print(x,y)

# print(db["India"])

# for i,j in db.items():
#     print(i,"-",j)

# for i in db.values():
#     print(i)


# for i in db.keys():
#     print (i)




# db = {}
#
# while True:
#     country = input('enter country name: ')
#     capital = input("enter capital name: ")
#     db[country] = capital
#
#     repeat = input("repeat again? ")
#     if repeat == "no":
#         break
# print (db)













# numbers = [9,5,2,6,3,78,3,7,0,4,6,4,5,7]
#
# odd_num = []
# even_num = []
# for i in numbers:
#     if i % 2 == 0:
#         even_num.append(i)
#     else:
#         odd_num.append(i)
# print(even_num)
# print(odd_num)