# Worst, Avg case : O(n^2)

class selectionSort:
	def __init__(self, arr):
		self.arr = arr

	def sort(self):
		length = len(self.arr)
		for lastIndex in range(length-1, -1, -1):
			largestIndex = self.findLargestIndex(lastIndex)
			# print('should change? lastIndex is '+str(lastIndex))
			self.arr[lastIndex], self.arr[largestIndex] = \
				self.arr[largestIndex], self.arr[lastIndex]
			# print('ARR = ' + str(self.arr)+'\n')
		return self.arr
			
	def findLargestIndex(self, maxIndex): # max함수를 쓰지 않고 구현하자
		maxValue = self.arr[0]
		largestIndex = 0
		for index in range(1,maxIndex+1):
			if maxValue < self.arr[index]:
				maxValue = self.arr[index]
				largestIndex = index
		# print('MAXINDEX:' + str(maxIndex))
		# print('DEBUG: largestIndex = '+str(largestIndex))
		return largestIndex


## TEST ##
if __name__ == "__main__":
	testArr = [8, 31, 48, 73, 3, 65, 20, 29, 11, 15]
	selection = selectionSort(testArr)
	print('RESULT = '+ str(selection.sort()))
	# RESULT = [3, 8, 11, 15, 20, 29, 31, 48, 65, 73]