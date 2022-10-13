import random
c_score = 0
u_score = 0
ties = 0
print("Rock paper Scissors")
print("""Rules for winning: 
          1. Rock vs Paper --> Paper wins
          2. Paper vs Scissors --> Scissors
          3. Scissors vs Rock --> Rock""")
print()
while True:
     print("""press 1 for rock
     press 2 for paper
     press 3 for scissors""")

     user_choice = int(input("enter a number between 1-3: "))

     while user_choice <1 or user_choice > 3:
          user_choice = int(input("enter valid number: "))

     if user_choice == 1:
          uc = "Rock"
     elif user_choice == 2:
          uc = "Paper"
     else:
          uc = "Scissors"

     print("User's choice is",uc)

     rps = ["Rock","Paper","Scissors"]
     cc = random.choice(rps)

     print("Computer's choice is",cc)

     #winning conditions
     if (uc == "Rock" and  cc =="Paper") or (cc == "Rock" and  uc =="Paper"):
          result = "Paper"

     elif (uc == "Paper" and cc == "Scissors") or (cc == "Paper" and uc == "Scissors"):
          result = "Scissors"

     elif(uc == "Scissors" and cc == "Rock") or (cc == "Scissors" and uc == "Rock"):
          result = "Rock"

     else:
          result = "Tie"

     if result == uc:
          print("User wins")
          u_score +=1
     elif result == cc:
          print("Computer wins")
          c_score +=1
     else:
          print("Its a tie")
          ties+=1
     print("user's score is ",u_score)
     print("Computer's score is ",c_score)
     print('ties are ',ties)

     repeat = input("play again? ")
     if repeat == "no":
          break









#Attribute Error
# try:
#      import random
#
#      choice = random.xyz()
# except AttributeError as a:
#      print(a)


#Type Error
# try:
#      print (12+"hello")
# except TypeError as t:
#      print(t)



#Module not found error
# try:
#      import harrypotter
# except ModuleNotFoundError as m:
#      print(m)


#Key Error
# try:
#      a = {"Name":"john"}
#      print(a["Age"])
# except:
#      print("given key is not present in the dictionary")


# Index Error
# l = ["apple","mango","banana"]
# try:
#      print(l[3])
# except IndexError as a:
#      print(a)


#Value Error
# try:
#      num1 = int(input("enter a number here: "))
#      num2 = int(input("enter a number here: "))
#
#      print(num1/num2)
# except (ValueError,ZeroDivisionError) as k:
#      print(k)
#
#
# print("welcome to wscube tech")


#Zero Division Error
# num1 = int(input("enter a number here: "))
# num2 = int(input("enter a number here: "))
# try:
#      num3 = num1/num2
#      print(num3)
# except:
#      print("cannot divide a number with zero")
#
# print("welcome to wscubetech")
