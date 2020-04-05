class MergeSort:
	"""
	Standard Recursive Algorithm

	Complextiy: O(NlogN)
		- O(N) for merging
		- Height of recursive tree is (1+logN)

	This algorithm needs O(N) auxiliary space for copying sub-arrays.
	"""
	def sort(self, arr):
		length = len(arr)
		if length > 1:
			midPoint = length//2

			leftHalf = arr[:midPoint]
			rightHalf = arr[midPoint:]

			self.sort(leftHalf)
			self.sort(rightHalf)
			arr = self._merge(leftHalf, rightHalf, arr) # every work is done in this routine.
			return arr

	def _merge(self, leftHalf, rightHalf, arr):
		length = len(arr)
		finalIndex = 0
		leftIdx, rightIdx = 0, 0
		leftLen, rightLen = len(leftHalf), len(rightHalf)

		while leftIdx < leftLen and rightIdx < rightLen:
			if leftHalf[leftIdx] > rightHalf[rightIdx]:
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

if __name__ == "__main__":
	testArr = [8, 31, 48, 73, 3, 65, 20, 29, 11, 15]
	mSort = MergeSort()
	print('RESULT = '+ str(mSort.sort(testArr)))
	# RESULT = [3, 8, 11, 15, 20, 29, 31, 48, 65, 73]