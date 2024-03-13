# arr=[1,2,3,4,5,1,2,3]
# arr2=[]
# # for i in arr:
# #     while i not in arr2:
# #         arr2.append(i)
# # print(arr2)
#
# a=lambda arr2:set(arr)
# print(a(arr))
import array
arr = array.array('i', [1, 2, 3, 1, 5])
print("The new created array is : ", end="")
for i in range(0, 5):
    print(arr[i], end=" ")