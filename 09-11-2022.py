import pandas as pd
import numpy as np

data = {"name":["john","david","peter"],
        "math":[87,78,np.nan],
        "science":[67,np.nan,np.nan]}

df = pd.DataFrame(data)
print(df)
print(df.isnull())














# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd

# data = {"name":["John","david","peter","lisa"],
#         "age":[23,45,20,34],
#         "gender":["male","male","male","female"]}
#
# df = pd.DataFrame(data)
# print(df)

# data = sns.load_dataset("tips")
# df = pd.DataFrame(data)
# # print(df)
# sns.countplot(data=df, x = "day",hue = "sex" )
# plt.show()












# import pandas as pd
#
# data = {"name":["John","david","peter","lisa"],
#         "age":[23,45,20,34],
#         "gender":["male","male","male","female"]}
#
# df = pd.DataFrame(data)
# df.to_csv("school_data1.csv",index=False)








#pip install openpyxl
# import pandas as pd

# data = {"name":["John","david","peter","lisa"],
#         "age":[23,45,20,34],
#         "gender":["male","male","male","female"]}

#data = [("David",23,"male"),("john",34,"male")]

# df = pd.DataFrame(data, columns=["name","age","gender"])
# data = pd.read_csv("E:/ayushi/python programs/Web Scraping/Mobiles_under50_000.csv")
# df = pd.DataFrame(data)
# print(df)
# print(df.head())













# import pandas as pd
#
# #names = ['John',"peter","David","lisa"]
# # dict1 = {"Name":"john","age":23,"gender":"male"}
# # numbers= [4,3,7,2,9,5,6]
# # s = pd.Series(numbers)
# #print(s)
# #print(s.mean())
# #print(s.head(2))
# #print(s.tail(2))
