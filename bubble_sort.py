# ##implementation of bubble sort

# def bubble_sort(arr,n):
# 	for i in range(n-1):
# 		#it will make code more optimized, won't iterate more if element did'nt swap
# 		swapped=False
# 		for j in range(n-i-1):
# 			if arr[j]>arr[j+1]:
# 				arr[j],arr[j+1]=arr[j+1],arr[j]
# 				swapped=True
# 		if swapped==False:
# 			return arr

# # arr=list(map(int,input("Enter the elements of an array: ").split()))
# arr=[50,30,60,10,40]
# print("Array before sorting: ",arr)
# print(len(arr))
# print("Array after sorting: ",bubble_sort(arr,len(arr)))
def bubble(arr,n):
    count=0
    for j in range(n-1):
        swapped=False
        for l in range(n-j-1):
            if arr[l]>arr[l+1]:
                count+=1
                arr[l],arr[l+1]=arr[l+1],arr[l]
                swapped=True
    print(count)
        # if swapped==False:
        #     return count
p=[1,2,3,4]
n=4
bubble(p,n)