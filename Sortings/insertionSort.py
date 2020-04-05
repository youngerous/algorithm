class InsertionSort:
	"""
	Complexity: O(N^2)
		- O(N) for moving key(step)
		- O(N) for pairwise swap
	
	Assumption: Operations of Comparison and Swap are equal in cost.
		- But usually comparison is more expensive than swap.
		- When using Binary Search, we can make comparison cost O(NlogN).
		- However, inserting(swap) cost is still O(N^2).
	"""
	def __init__(self, arr):
		self.arr = arr

	def sort(self):
		length = len(self.arr)
		for key in range(1, length): # Assumption: index zero is already sorted.
			current_value = self.arr[key]
			index = key
			
			while index > 0 and current_value < self.arr[index-1]:
				self.arr[index] = self.arr[index-1] # swap
				index -= 1
			self.arr[index] = current_value

		return self.arr

if __name__ == "__main__":
	testArr = [8, 31, 48, 73, 3, 65, 20, 29, 11, 15]
	insertion = InsertionSort(testArr)
	print('RESULT = '+ str(insertion.sort()))
	# RESULT = [3, 8, 11, 15, 20, 29, 31, 48, 65, 73]


