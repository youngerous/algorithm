class InsertionSort:
	"""
	Complexity: O(N^2)
		- O(N) for moving key(step)
		- O(N) for pairwise swap
	
	Assumption: Operations of Comparison and Swap are equal in cost.
		- But usually comparison is more expensive than swap.
		- When using Binary Search, we can make comparison cost O(NlogN).
		- However, inserting(swap) cost is still O(N^2).

	This algorithm does in-place sort. It needs O(1) auxiliary space (swapping variable).
	"""
	def sort(self, arr):
		length = len(arr)
		for key in range(1, length): # Assumption: index zero is already sorted.
			current_value = arr[key]
			index = key
			
			while index > 0 and current_value < arr[index-1]:
				arr[index] = arr[index-1] # swap
				index -= 1
			arr[index] = current_value

		return arr

if __name__ == "__main__":
	testArr = [8, 31, 48, 73, 3, 65, 20, 29, 11, 15]
	insertion = InsertionSort()
	print('RESULT = '+ str(insertion.sort(testArr)))
	# RESULT = [3, 8, 11, 15, 20, 29, 31, 48, 65, 73]
