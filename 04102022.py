import numpy as np
arr = np.array([[[1,2],[3,4]],[[5,6],[8,9]]])

print(arr[1][0][0])




# print(arr)
# print(len(arr))
# print(type(arr))
# print(arr.shape)
# print(arr.size)




# import numpy as np
# arr = np.array([[1,2,3,4],[2,3,4,6]])
# print(arr)
# arr2 = np.array([4,5,6,7])
#
# arr3 = arr+arr2
# print(arr3)




# import matplotlib.pyplot as plt
#
# x = [2,4,6,8,10,12,14]
# y = [45,34,64,25,39,55,67]
#
# plt.stem(x,y)
# plt.show()













# import matplotlib.pyplot as plt
# import numpy as np
#
# x = [2,4,6,8,10,12,14,16,18,20]
# y = [56,24,56,34,67,56,46,37,44,88]
# colors = np.array([2,4,6,8,10,12,14,16,18,20])
# plt.scatter(x,y,c = colors, cmap="spring")
# plt.colorbar()
# plt.show()







# import matplotlib.pyplot as plt
#
# x = [20,40,50,30,50,40,60,20,30,40,45,35,49]
#
# plt.hist(x)
# plt.show()






# import matplotlib.pyplot as plt
#
# x = [35,10,30,25]
# labels = ["Oneplus","Nokia","mi","Vivo"]
# c = ["red","yellow","blue","green"]
# exp = [0,0.2,0,0.2]
# plt.pie(x, labels = labels,autopct="%1i%%" ,colors = c, startangle=90, explode=exp, shadow = True)
# plt.legend(loc = 2)
# plt.show()





# import matplotlib.pyplot as plt
#
# x = ["part1","part2","part3","part4","part5"]
# y = [95,80,75,95,80]
# y1= [100,78,45,99,82]
#
# plt.plot(x,y,label = "men",marker = "^", color = "blue", alpha = 0.5, linewidth = 4)
# plt.plot(x,y1, label = "women", marker = "D", color = "red", linestyle = ":")
# plt.legend(loc = 1)
# plt.show()
