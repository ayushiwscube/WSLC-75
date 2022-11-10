a = {1,5,8,3}
b = {4,2,8,1}

print(a.union(b))
print(a.intersection(b))
print(b.difference(a))
print(a.symmetric_difference(b))









# l =[]
#
# for i in range(1,20):
#     if i % 2 == 0:
#         l.append(i)
#
# print(l)





# a = [12,34,5,2,4,6,3,5,63,6,8,4,6,87,8]
# print(a)
# print(len(a))
#
# avengers = {"hawkeye","ironman","thor","hulk","vision"}
# print(avengers)
# avengers.add("wanda")
# avengers.remove("thor")
# print(avengers)
# b = {12,34,5,2,4,6,3,5,63,6,8,4,6,87,8}
# print(b)
# print(len(b))












# a = "banana","apple","kiwi",45
#
# a = list(a)
# print(a)
# a.append("grapes")
# print(a)
# a = tuple(a)
# print(a)












# print(a)
# print(type(a))
# a.remove("apple")
# print(a)















# import pandas as pd
# import numpy as np
#
# data = {"name":["john","david","peter","lisa","jack","rebecca","zida"],
#         "math":[87,78,np.nan,90,87,67,90],
#         "science":[67,np.nan,np.nan,87,77,66,99],
#         "history":[np.nan,67,88,76,88,56,78],
#         "houses":["red","blue","yellow","red","green","yellow","blue"]}
#
# df = pd.DataFrame(data)
# print(df)
# gb = (df.groupby("houses"))
#
# for name,houses in gb:
#         print(name)
#         print(houses)
#         print()











# df.loc[len(df.index)] = ["Zida",90,78,68]
# print(df)




# print(df.isnull())
# print()
#print(df.fillna("hi"))
#print(df.fillna(method="pad"))
#print(df["math"].fillna("70"))
#
# ab = df.replace(to_replace= np.nan, value = 70)
# print(ab)

# ip = df.interpolate(method="linear", limit_direction="backward")
# print(ip)

# drop = df.drop(3, axis=0)
# print(drop)
