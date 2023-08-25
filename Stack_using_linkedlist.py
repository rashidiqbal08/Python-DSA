class Node:
	def __init__(self,value):
		self.data=value
		self.next=None

class stack:
	def __init__(self):
		self.top=None

	def isempty(self):
		return self.top==None

# 	#creating a method for push()
	def push(self,value):
		new_node=Node(value)
		new_node.next=self.top
		self.top=new_node

# 	#method for traversing( printing the value)
	def traverse(self):
		if self.isempty()==True:
			return "Stack is empty."
		else:
			temp=self.top
			while(temp!=None):
				print(temp.data)
				temp=temp.next

# 	#method for printing length
# 	def __len__(self):
# 		temp=self.top
# 		count=0
# 		while(temp!=None):
# 			count+=1
# 			temp=temp.next
# 		return count


# 	#method for push()
	def popp(self):
		if (self.isempty()):
			return "Stack is empty."
		else:
			popped_ele=self.top.data
			self.top=self.top.next
			#this will return the element that has been popped.
			return popped_ele


s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

# s.popp()

s.traverse()

