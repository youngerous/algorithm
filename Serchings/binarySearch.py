# binarySearch

def binarySearch(arr, start, end, key):
	if start > end:
		return False

	middle = (start+end)//2
	if key == arr[middle]:
		return middle
	elif key < arr[middle]:
		return binarySearch(arr, start, middle-1, key)
	elif key > arr[middle]:
		return binarySearch(arr, middle+1, end, key)
	else:
		return -1

 ## TEST ##
testArr = [3, 8, 11, 15, 20, 29, 31, 48, 65, 73]
print(binarySearch(testArr, 0, len(testArr)-1, 1)) # False
print(binarySearch(testArr, 0, len(testArr)-1, 29)) # 5


