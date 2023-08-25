class Node:
	def __init__(self,value):
		self.left = None
		self.data = value
		self.right = None

class Bst:
	def createNode(self,data):
		return Node(data)

	def insert(self,node,data):
		if node is None:
			return self.createNode(data)
		if data <node.data:
			node.left = self.insert(node.left,data)
		else:
			node.right = self.insert(node.right,data)
		return node


	#method for inorder traversal
	def InorderTraversal(self,root):
		if root is None:
			return 0
		self.InorderTraversal(root.left)
		print(root.data,end=" ")
		self.InorderTraversal(root.right)

	#method for searching in BST
	def SearchInBst(self,root,key):
		if root is None:
			return 0
		elif root.data>key:
			return self.SearchInBst(root.left,key)
		elif root.data == key:
			return 1
		else:
			return self.SearchInBst(root.right,key)
			
	
		





ar = [5,1,3,4,2,7]
btree = Bst()
root = btree.createNode(5)
# btree.insert(root,1)
# btree.insert(root,3)
# btree.insert(root,4)
# btree.insert(root,2)
# btree.insert(root,7)

#inserting element by iteration.
for i in range(1,len(ar)):
	btree.insert(root,ar[i])
print("All the node has been inserted.")
print("Inorder traversal-->",end=" ")
btree.InorderTraversal(root)
print()

#for seraching in bst
if (btree.SearchInBst(root,7)):
	print("Node found")
else:
	print("Not found.")
