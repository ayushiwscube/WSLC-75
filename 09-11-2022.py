# import numpy as np

# arr1 = np.array([[1,4],[3,7]])
# arr2 = np.array([[8,1],[3,5]])
#
# print(arr1*arr2)

# mat1 = np.matrix([[1,2,3],[4,8,7],[7,6,7]])
# mat2 = np.matrix([[2,3],[4,2]])
#
# print(mat1)
# print(np.transpose(mat1))
# print(np.linalg.det(mat1))
# print(np.linalg.inv(mat1))
# print(mat2)

# print (mat1.dot(mat2))
# print(np.trace(mat2))
# print(np.diagonal(mat1))







# import numpy as np
#
# arr1 = np.array([[3,np.nan],[7,9]])
# arr2 = np.array([[5,8],[1,4]])
#
# # print(np.nanmean(arr1))
# # print(arr1.flatten())
# # print(np.nansum([arr1,arr2],axis=0))
#
# # arr3 = (np.concatenate([arr1,arr2],axis=0))
# # print(arr3)











# import numpy as np
#
# arr = np.array([[[6,4],[9,3]],[[6,4],[9,3]]])

# for i in arr:
#     for j in i:
#         for k in j:
#             print(k)

# for i in np.nditer(arr):
#     print(i)

# for index,i in np.ndenumerate(arr):
#     print(index,i)

# l = [1,4,8,3]
#
# for index,i in enumerate(l):
#     print(index,i)
