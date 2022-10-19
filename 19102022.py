#bank system
#deposit, withdraw and view bankbalance








class company:

    def emp1(self,name):
        self.name = name
        print("the name is",self.name)

    def emp2(self):
        print("the name is",self.name)







# class companyA:
#     def emp1(self):
#         print("the name of the employee 1 is John")
#
# class companyB(companyA):
#     def emp1(self):
#         super().emp1()
#         print("the name of the employee 1 is lisa")
#
# a = companyB()
# a.emp1()





















# class companyA:
#     def semp_name(self,name):
#         self.__name = name
#     def gemp_name(self):
#         return self.__name
#
#     def semp_age(self,age):
#         self.__age = age
#     def gemp_age(self):
#         return self.__age
#
#
#     def emp_data(self):
#         print('the name of the employee is',self.__name)
#         print("the age of the employee is",self.__age - 2000)
#
# a = companyA()
# a.semp_name("John")
# a.semp_age(50000)
# a.emp_data()












# class companyA:
#     def __emp1(self):
#         print("my name is john")
#     def __init__(self):
#         self.__emp1()
#
# a = companyA()






# class companyA:
#
#     name = "john"
#     age = 23
#     __salary = 50000
#
# a = companyA()
# print(a.name)















# #parent class
# class companyA:
#     def emp1(self):
#         print("the name of the employee 1 is John")
#     def emp2(self):
#         print("the name of the employee 2 is david ")
#
# #child class
# class companyB:
#     def emp3(self):
#         print("the name of the employee 3 is Lisa")
#     def emp4(self):
#         print("the name of the employee 4 is zida")
#
# class companyC(companyA,companyB):
#     def emp5(self):
#         print("the name of the employee 5 is peter")
# e = companyA()
# e.emp1()
# d = companyB()
# d.emp3()
# f = companyC()
# f.emp3()
