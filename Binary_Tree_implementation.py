#IMPLEMENTATION OF TREE DATA STRUCTURE

#Creating a node class
class Node:
	def __init__(self,value):
		self.left = None
		self.data = value
		self.right = None

#creating a tree class
class Tree:
	

	#method for creating a new Node.
	def CreateNone(self,data):
		
		return Node(data)

	#method for inserting an element 
	def insert(self,node,data):

		#if node is none then create new node
		if node is None:
		
			return self.CreateNone(data)
		if data <node.data:
			
			node.left = self.insert(node.left,data)
		if data> node.data:
			
			node.right = self.insert(node.right,data)
		return node

	#method for Inorder traversal
	def InorderTraversal(self, root):
		
		#in each step we have to check if root is none or not.
		if root is not None:
			
			#if it's not none do recursive call
			self.InorderTraversal(root.left)

			#then 2nd step print the root.data if it's None.
			print(root.data,end=" ")

			#then recursive call for root.right
			self.InorderTraversal(root.right)
		
	#method for preorder traversal
	def PreorderTraversal(self,root):
		if root is not None:
			print(root.data)
			self.PreorderTraversal(root.left)
			self.PreorderTraversal(root.right)

	#method for postorder traversal
	def postorderTraversal(self,root):
		if root is not None:
			self.postorderTraversal(root.left)
			self.postorderTraversal(root.right)
			print(root.data)

	#method for count of nodes
	def countOfNodes(self,root):
		if root == None:
			return 0
		leftCount = self.countOfNodes(root.left)
		rightCount = self.countOfNodes(root.right)
		return leftCount+rightCount+1

	#method for sum of the total nodes
	def SumOfNodes(self,root):
		if root == None:
			return 0
		leftSum = self.SumOfNodes(root.left)
		rightSum = self.SumOfNodes(root.right)
		return leftSum+rightSum+root.data

	#method for calculating the height of tree
	def HeightOfTree(self,root):
		if root == None:
			return 0
		lefHeight = self.HeightOfTree(root.left)
		rightHeight = self.HeightOfTree(root.right)
		return max(lefHeight,rightHeight) + 1

#driver code 

#creating an object of class Tree
tree = Tree()

#creating a root node
root = tree.CreateNone(5)

#inserting an element
tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,7)
tree.insert(root,6)
tree.insert(root,8)

print("Inorder sorted tree-->")
print(tree.InorderTraversal(root))
# print("PreorderTraversal-->")
# print(tree.PreorderTraversal(root))
# print("postorderTraversal-->")
# print(tree.postorderTraversal(root))


##Leetcode questions
# print("Total no of nodes-->",tree.countOfNodes(root))
# print("Total sum of nodes -->",tree.SumOfNodes(root))
# print("Total height of the tree-->",tree.HeightOfTree(root))