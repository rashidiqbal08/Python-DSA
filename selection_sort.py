def selection(arr):
	l=len(arr)
	for i in range(l):
		temp=i
		for j in range(i+1,l):
			if arr[temp]>arr[j]:
				temp=j
		arr[i],arr[temp]=arr[temp],arr[i]
def printarr(arr):
	print("Sorted array: ")
	for i in arr:
		print(i,end=' ')
	print()
arr=[3,4,1,3,8,2]
print(arr)
selection(arr)
printarr(arr)


