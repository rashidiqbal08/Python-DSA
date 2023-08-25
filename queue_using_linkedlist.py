##IMPLEMENTATION OF QUEUE USING LINKEDLIST
# from collections import deque
class Node:
	def __init__(self,value):
		self.data=value
		self.next=None

class queue:
	def __init__(self):
		self.front=None
		self.rear=None

# 	#method for inqueue:
	def inqueue(self,data):
		new_node = Node(data)
		if self.front is None:
			self.front = new_node
			self.rear = self.front
			print("Element inserted at first: ",data)
		else:
			self.rear.next = new_node
			self.rear = new_node
			print("Element inserted: ",data)

# 	#method for dequeue(deletion)
	def dequeue(self):
		if self.front is None:
			print("Queue is empty")
		else:
			print("Element deque: ",self.front.data)
			self.front = self.front.next

# 	#method for traverasal a queue
# 	def traversal(self):

# 		#traversal from front
# 		temp=self.front
# 		print("Elements in queue: ")
# 		while temp is not None:
# 			print(temp.data,end=' ')
# 			temp=temp.next
			
# 	#method for size of the queue
# 	def __len__(self):
# 		temp=self.front
# 		count=0
# 		while temp is not None:
# 			count+=1
# 			temp=temp.next
# 		return count

q1=queue()
q1.inqueue(10)
q1.inqueue(20)
q1.inqueue(30)
q1.inqueue(40)
q1.dequeue()
q1.dequeue()
# # q1.dequeue()
# # q1.dequeue()
# # q1.dequeue()

# print("length of the queue is: ",len(q1))
# q1.traversal()

