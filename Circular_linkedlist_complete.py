# class node:
# 	def __init__(self,value):
# 		self.data = value
# 		self.next = None
# class CLL:
# 	def __init__(self):
# 		self.head = None
# 		self.tail = None
# 		self.n = 0

# 	#method for returning the length of CLL
# 	def __len__(self):
# 		return self.n
	
# 	#method for inserting at beginning
# 	def insert_head(self, value):
# 		new_node = node(value)
# 		if self.head is None:
# 			self.head = new_node
# 			self.tail = new_node
# 			self.tail.next = self.head
# 			self.n +=1
# 			print("Element inserted: ",value)

# 		else:
# 			new_node.next = self.head
# 			self.tail.next = new_node
# 			self.head = new_node
# 			self.n +=1
# 			print("Element inserted: ",value)

# 	#insert at the end
# 	def at_end(self,value):
# 		new_node = node(value)
# 		if self.head is None:
# 			self.head = new_node
# 			self.tail = new_node
# 			self.tail.next = self.head
# 			#increasing the length of ll
# 			self.n+=1
# 		else:
# 			new_node.next = self.head
# 			self.tail.next = new_node
# 			self.tail = new_node
# 			self.tail.next = self.head
# 			#increasing the length of ll
# 			self.n+=1
	
# 	#method for inserting at specific positio
# 	def at_specific(self,after,value):
# 		new_node = node(value)
# 		if self.head is None:
# 			self.head = new_node
# 			self.tail = new_node
# 			self.tail.next = self.head

# 			self.n+=1

# 		#if after value is at the end
# 		elif self.tail.data == after:
# 			self.at_end(value)
# 		else:
# 			temp = self.head
# 			while(temp.next != self.head):
# 				if temp.data == after:
# 					break
# 				temp = temp.next
# 			if temp.next!= self.head:
# 				new_node.next = temp.next
# 				temp.next = new_node
# 				self.n +=1
# 			else:
# 				print("Value not found")

# 	#method for display the data
# 	def display(self):
# 		if self.head is None:
# 			print("CLL is empty.")

# 		else:
# 			temp = self.head
# 			print(temp.data,"->",end="")
# 			while(temp.next != self.head):
# 				temp= temp.next
# 				print(temp.data,"->",end="")
				









# L1 = CLL()
# L1.insert_head(21)
# L1.at_end(22)
# L1.at_end(23)
# L1.at_end(24)
# L1.at_end(25)
# # L1.at_specific(25,26)
# L1.display()

# print()
# print("length of the CLL: ",len(L1))
# a = *@*



a = 'aa/bb'
print(a)
b = ''
for j in a:
	if j !='/':
		b+=j

print(b)
