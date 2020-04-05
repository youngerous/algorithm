class MergeSort:
	def __init__(self):
		pass

	def sort(self, arr):
		length = len(arr)
		if length > 1:
			midPoint = length//2

			leftHalf = arr[:midPoint]
			rightHalf = arr[midPoint:]

			self.sort(leftHalf)
			self.sort(rightHalf)
			self.merge(leftHalf, rightHalf, arr)
			return arr

	def merge(self, leftHalf, rightHalf, arr):
		length = len(arr)
		finalIndex = 0
		
		leftIdx = 0
		rightIdx = 0
		leftLen = len(leftHalf)
		rightLen = len(rightHalf)

		while leftIdx < leftLen and rightIdx < rightLen:
			if(leftHalf[leftIdx] > rightHalf[rightIdx]):
				arr[finalIndex] = rightHalf[rightIdx]
				rightIdx += 1
				finalIndex += 1
			else:
				arr[finalIndex] = leftHalf[leftIdx]
				leftIdx += 1
				finalIndex += 1

		# when left done
		while rightIdx < rightLen:
			arr[finalIndex]	= rightHalf[rightIdx]
			rightIdx += 1
			finalIndex += 1

		# when right done
		while leftIdx < leftLen:
			arr[finalIndex] = leftHalf[leftIdx]
			leftIdx += 1
			finalIndex += 1

		return arr

## TEST ##
if __name__ == "__main__":
	testArr = [8, 31, 48, 73, 3, 65, 20, 29, 11, 15]
	mSort = MergeSort()
	print('RESULT = '+ str(mSort.sort(testArr)))
	# RESULT = [3, 8, 11, 15, 20, 29, 31, 48, 65, 73]