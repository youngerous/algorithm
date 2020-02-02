class quickSort:
	def __init__(self):
		pass

	def sort(self, arr, start, end):
		if start < end:
			point = self.partition(arr, start, end)
			self.sort(arr, start, point-1)
			self.sort(arr, point+1, end)
		return arr

	def partition(self, arr, start, end):
		pivot = arr[end]	#마지막 인덱스 기준
		smallerValuesIdx = start-1
		for index in range(start, end):
			if arr[index] <= pivot:
				smallerValuesIdx += 1
				# print('index:'+str(index)+'		smallerValuesIdx:'+str(smallerValuesIdx) + '	pivot:'+str(end))
				arr[smallerValuesIdx], arr[index] = arr[index], arr[smallerValuesIdx]
		arr[smallerValuesIdx+1], arr[end] = arr[end], arr[smallerValuesIdx+1]
		# print('smallerValuesIdx: '+ str(smallerValuesIdx+1))
		return smallerValuesIdx + 1 # pivot이 위치한 자리 리턴

## TEST ##
if __name__ == "__main__":
	testArr = [8, 31, 48, 73, 3, 65, 20, 29, 11, 15]
	quick = quickSort()
	print('RESULT = '+ str(quick.sort(testArr,0,len(testArr)-1)))
	# RESULT = [3, 8, 11, 15, 20, 29, 31, 48, 65, 73]		





		