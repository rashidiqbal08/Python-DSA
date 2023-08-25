##code for binary search
def binary(arr,low,high,item):
	if low<=high:
		mid=(low+high)//2
		# print(mid)
		if arr[mid]==item:
			return mid
		elif arr[mid]>item:
			return binary(arr,low,mid-1,item)
		elif arr[mid]<item:
			return binary(arr,mid+1,high,item)
	else:
		return "Item not found"

arr=[10,20,30,40,50,60]

print(binary(arr,0,(len(arr)-1),30))