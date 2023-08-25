class Stack:
	def __init__(self):
		self.stack = []

	#adding the value in the stack
	def add(self,value):
		self.stack.append(value)
		return True

	#top of the stack method
	def peek(self):
		return self.stack[-1]

	#removing the first element entered
	def remove(self):
		if len(self.stack) <=0:
			print("Stack underflow")
		else:
			print("Element popped: ",self.peek())
			return self.stack.pop()

	#printing the value of the stack
	def traverse(self):
		if len(self.stack) ==0:
			print("Stack empty")
		else:
			print(self.stack)


a=Stack()
a.add(10)
a.add(20)
a.add(30)
a.remove()
a.remove()
a.remove()
a.remove()




# a.traverse()

