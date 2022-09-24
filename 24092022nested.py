# for i in range(1,6): #rows
#     for j in range(1,i+1): #columns
#         print (i, end =" ")
#     print()


"""
1
22
333
4444
55555
"""

"""
*****
****
***
**
*
"""

for i in range(0,6):
    for j in range(0,6-i):
        print ("*",end = "")
    print ()


"""
   *
  * *
 * * *
* * * *
 
"""
# rows = 5
# k = 2*rows - 2
# for i in range(0,6):
#     for j in range(0,k):
#         print(end=" ")
#     k = k - 1
#     for j in range(0, i+1):
#         print("*", end = " ")
#     print("")




















# while True:
#     print ("""press 1 for addition
#     press 2 for subtraction
#     press 3 for multiplication
#     press 4 for division""")
#     choice = int(input('enter your choice for 1-4: '))
#     if choice == 1:
#         while True:
#             num = int(input('enter a number here: '))
#             num1 = int(input("enter a number here: "))
#             print (num + num1)
#             repeat1 = input("do you want to add more data? ")
#             if repeat1 == "no":
#                 break
#     elif choice == 2:
#         num = int(input('enter a number here: '))
#         num1 = int(input("enter a number here: "))
#         print(num - num1)
#
#     repeat = input("do you want to repeat again?")
#     if repeat == "no":
#         break