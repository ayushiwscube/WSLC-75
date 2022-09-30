avengers = ["Hulk","Thor","Ironman","Captain America","Spiderman","Antman"]
number = [1,2,3,3,6,4,4,6,3,56,78,8,4,3,6]
# for i in avengers:
#     print(i)

my_list = [i for i in number if i > 6]
print(my_list)



# import random
#
# words = ["telephone","lamp","smartphone","oneplus","saturn","wscubetech","earth"]
#
# word = random.choice(words)
#
# total_chances = 7
# guessed_word = "-"*len(word)
# word = word.upper()
# while total_chances != 0:
#     print(guessed_word)
#     letter = input("guess a letter: ").upper()
#     if letter in word:
#         for index in range(len(word)):
#             if word[index] == letter:
#                 guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]
#
#         if guessed_word == word:
#             print ("congratulations you won!")
#             break
#     else:
#         total_chances -= 1
#         print("incorrect guess")
#         print("total chances left ",total_chances)
#
# else:
#     print("you lost!!")
#     print('all the chances exhausted')
#
# print("the correct word is",word)
# print("thank you for playing")




# print("~~~~ Grocery List ~~~~")
# grocery = []
#
# while True:
#     print("""
#     press 1 to add an item
#     press 2 to delete an item
#     press 3 to view the whole list""")
#
#     choice = int(input("enter your choice frm 1-3: "))
#     if choice == 1:
#         item = input("enter the item you want to add: ").upper()
#         grocery.append(item)
#         print()
#         print(grocery)
#
#     elif choice ==2:
#         item = input("enter the item you want to delete: ").upper()
#         grocery.remove(item)
#         print()
#         print(grocery)
#
#     elif choice == 3:
#         print(grocery)
#
#     else:
#         print("invalid option")
#
#     repeat = input("repeat again? ")
#     if repeat == "no":
#         break














# avengers = ["Hulk","Thor","Ironman","Captain America","Spiderman","Antman"]
# numbers = [1,6,3,6,3,7,3,7,3,6,3,6,9]

# print(avengers)
# avengers.pop(3)
# print(avengers)


# print(avengers)
# avengers.remove("Captain America")
# print(avengers)



# avengers.sort()
# print(avengers)



# numbers.sort()
# print(numbers)


# print(avengers)
# avengers.insert(2, "vision")
# print(avengers)

# avengers.append("vision")
# print(avengers.index("Spiderman"))
# print(len(avengers))
# print(numbers.count(6))