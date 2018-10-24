# Worst, Avg case : O(n^2)

class bubbleSort:
	def __init__(self, arr):
		self.arr = arr

	def sort(self):
		length = len(self.arr)
		for lastIndex in range(length-1, -1, -1):
			for idx in range(lastIndex):
				if self.arr[idx] > self.arr[idx+1]:
					self.arr[idx], self.arr[idx+1] = \
						self.arr[idx+1], self.arr[idx]
		return self.arr

 ## TEST ##
testArr = [8, 31, 48, 73, 3, 65, 20, 29, 11, 15]
bubble = bubbleSort(testArr)
print('RESULT = '+ str(bubble.sort()))
# RESULT = [3, 8, 11, 15, 20, 29, 31, 48, 65, 73]