# # ##CREATION OF LINKED LIST
# # #
class Node:

    def __init__(self,value):
        self.data=value
        self.next=None

#creating a linkedlist
class Linkedlist:
    #creation of head
    def __init__(self):
        self.head=None
        self.n=0
    def __len__(self):
        return self.n
    
# #
# #     #Method for inserting from head
    def insert_head(self, value):
        #creating new node
        new_node = Node(value)
        #making connection to the next node
        new_node.next = self.head

        #reassign head node
        self.head = new_node
        #increasing the length
        self.n = self.n+1
# #     #method for printing the value
    def __str__(self):

        #making head node as current/temp
        current=self.head

        #creating string variable for output
        result=''

        #loop will run till the last node when(head=NONE)
        while(current!=None):
            result= result+ str(current.data)+'->'

            #assining current node to next
            current=current.next

        # results
        return result[:-2]
# #
# ##insert at the end(append)
    def append(self,value):

        # creating a new node
        new_node = Node(value)

        # assining self as current/temp node
        current = self.head

        #check if linkedlist is empty.
        if self.head==None:
            self.head=new_node
            self.n+=1
            return

        #loop will run till last node
        while(current.next!=None):
            current=current.next

        #inserting node at the end
        current.next=new_node

        #increasing the length of node
        self.n+=1

##method for insertion in between
    def insert_after(self,after,value):
        new_node=Node(value)
        current=self.head

        while(current!=None):
            if current.data==after:
                break
            #increasing the current
            current=current.next

        if current==None:
            print("Value Not found.")
        else:
            new_node.next=current.next
            current.next=new_node
            self.n+=1
# #
# #     #method of clear
#     def clear(self):
#         self.n=0
#         self.head=None
# #
# ##method for deleting the head
#     def del_head(self):
#         #check if LL is empty
#         if self.head==None:
#             return "Linked list is empty"
#         else:
#             self.head=self.head.next
#             self.n-=1

# #Method for deleting the tail
#     def pop(self):
#         current=self.head

#         #if there is empty ll
#         if self.head==None:
#             return "LinkedList is empty."

#         #if there is only one node(head)
#         if current.next==None:
#             self.del_head()
#             self.n-=1
#             return

#         #now start traversing
#         while(current.next!=None):
#             current=current.next

# #Method for deleting by values.
#     def remove(self,value):
#         current=self.head
#         # if self.head==None:
#         #     return print("Linked list is empty")
#         if current.data==value:
#             self.del_head()
#             return
#         while current.next!=None:
#             if current.next.data==value:
#                 break
#             current=current.next
#         if current.next==None:
#             return "item not found"
#         else:
#             current.next=current.next.next
#             self.n=self.n-1

# #Method for searching(it will return the index of the element)
#     def search(self,value):
#         current=self.head
#         if self.head==None:
#             return "LinkedList is empty"
#         position=0
#         while current!=None:
#             if current.data==value:
#                 return position
#             current=current.next
#             position+=1
#         if current==None:
#             return "Item not found."

# #method for searching by index
#     def get(self, item):
#         current=self.head
#         if self.head==None:
#             return "Linkedlist is empty"
#         position=0
#         while(current!=None):
#             if position==item:
#                 return current.data
#             current=current.next
#             position+=1
#         if current==None:
#             return "Item not found"

#     #method to get the second 2 index no from last
#     def second(self):
#         current=self.head
#         while(current!=None):
#             if current.next.next.next==None:
#                 return current.data

#             current=current.next
    


# # n=Node(10)
l1=Linkedlist()
# print(len(l1))
print("length before insertion: ",len(l1))

l1.insert_head(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
# l1.append(6)
# # l1.append(7)
# # l1.insert_after(1,4)
# # l1.clear()
print("inserted value in linkedlist",l1)
print("Final length: ",len(l1))
# # # l1.clear()1
# # l1.del_head()
# # print("Final length: ",len(l1))
# # print(l1.search(5))

# print(l1)
# # print(l1.second())
# # print(l1.get(0))


















