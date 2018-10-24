# sequentialSearch (linearSearch)

def sequentialSearchUnordered(arr, key): # in case of unordered data
	# time complexity: O(n)
	index = 0
	length = len(arr)
	while index < length and arr[index] != key:
		index += 1

	if index < length:
		return index
	else:
		return -1

def sequentialSearchOrdered(arr, key):	# in case of ordered data
	# time complexity: O(n)
	index = 0
	length = len(arr)
	while arr[index] < key:
		index += 1

	if arr[index] == key:
		return index
	else:
		return -1


## TEST ##
print('### Sequential Search Unordered ###')
testArr = [8, 31, 48, 73, 3, 65, 20, 29, 11, 15] 
print(sequentialSearchUnordered(testArr, 8)) # 0
print(sequentialSearchUnordered(testArr, 20)) # 6

print('### Sequential Search Ordered ###')
testArr2 = [3, 8, 11, 15, 20, 29, 31, 48, 65, 73]
print(sequentialSearchOrdered(testArr2, 15)) # 3
print(sequentialSearchOrdered(testArr2,22)) # -1


