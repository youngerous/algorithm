# 평균 선형시간 선택 알고리즘
	# 평균 수행 시간: theta(n)
	# 최악의 경우: theta(n^2)

# quickSort를 사용한다.
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

	# 배열[start, ... ,end]에서 target번째 작은 원소를 찾는다.
	def select(self, arr, start, end, target):
		if start == end:
			return arr[start]

		point = self.partition(arr, start, end)
		nth = point - start + 1 # 기준 원소(point)가 전체에서 nth번째 작은 원소임을 의미

		if target < nth: # 기준원소보다 작은 경우
			return self.select(arr, start, point-1, target) 	# 왼쪽 그룹 탐색
		elif target == nth:
			return arr[nth]
		else: # 기준원소보다 큰 경우
			return self.select(arr, point+1, end, target - nth)	# 오른쪽 그룹 탐색


if __name__ == "__main__":
	## TEST ##
	testArr = [8, 31, 48, 73, 3, 65, 20, 29, 11, 15] 
	# 정렬 시 숫자 순위 = [3, 8, 11, 15, 20, 29, 31, 48, 65, 73]	
	linearSelect = quickSort()

	# n번째 작은 수 찾기
	print('RESULT = '+ str(linearSelect.select(testArr, 0, len(testArr)-1, 7))) # 31
	print('RESULT = '+ str(linearSelect.select(testArr, 0, len(testArr)-1, 2))) # 8


