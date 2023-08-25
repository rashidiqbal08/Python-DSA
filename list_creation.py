# ##CREATING LIST WITH THE HELP OF CLASSES
# import ctypes
# class myList:
#     def __init__(self):
#         self.size=1
#         self.n= 0    #n=current no of items

#         #now creating c type array with size =self.size
#         self.A=self.__make_array(self.size)
#     def __make_array(self,capacity):
#         #create a c types array
#         return (capacity*ctypes.py_object)()
#     def __len__(self):
#         return self.n
#     def append(self,item):
#         if self.n==self.size:
#             self.__resize(self.size*2)
#         #append the array
#         self.A[self.n]=item
#         self.n=self.n+1

#     #resize function
#     def __resize(self,new_capacity):
#         #creating array with new capacity
#         B=self.__make_array(new_capacity)
#         self.size=new_capacity

#         #now copy the content of A into B
#         for i in range(0,self.n):
#             B[i]=self.A[i]
#         #reassign A
#         self.A=B

#     #method for print
#     def __str__(self):
#         result=''
#         for i in range(self.n):
#             result=result+str(self.A[i])+','
#         # return result
#         #for sq bracket
#         return '[' + result[:-1] + ']'

#     #method for indexing
#     def __getitem__(self, index):
#         if index>=0 and index<=self.n:
#             return self.A[index]
#         else:
#             return "Index out of range"

#     #pop method(delete the last element)
#     def pop(self):

#         #decrement the value of n by 1
#         if self.n>0:
#             self.n-=1
#         else:
#             return "list underflow"






# l=myList()

# # l.append(2)
# # l.append("Rashid")
# # l.append(True)
# # l.append(45.33)
# print("My_list: ",l)
# print("length is : ",len(l))
# # print(l[2])
# l.pop()
# #after removing the last element
# print(l)


