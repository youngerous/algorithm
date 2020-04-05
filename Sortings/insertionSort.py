# Best case : O(n) -> 모두 정렬돼있을 때
# Worst, Avg case : O(n^2)

class InsertionSort:
	def __init__(self,arr):
		self.arr = arr

	def sort(self):
		length = len(self.arr)
		for i in range(1, length): # 0번째 index는 이미 정렬되어 있다고 가정
			currentValue = self.arr[i]
			index = i
			# currentValue가 index에 위치한 값보다 크면 while문 종료
			while index > 0 and currentValue < self.arr[index-1]:
				# print(self.arr)
				self.arr[index] = self.arr[index-1] # 조건 달성할 때까지 오른쪽으로 shift
				index -= 1

			# 제 자리를 찾은 값을 list에 위치시킨다.
			self.arr[index] = currentValue

		return self.arr

## TEST ##
if __name__ == "__main__":
	testArr = [8, 31, 48, 73, 3, 65, 20, 29, 11, 15]
	insertion = InsertionSort(testArr)
	print('RESULT = '+ str(insertion.sort()))
	# RESULT = [3, 8, 11, 15, 20, 29, 31, 48, 65, 73]


