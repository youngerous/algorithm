class CountingSort:
	def __init__(self, arr):
		self.arr = arr
	
	def sort(self):
		length = len(self.arr)
		sortedArr = [] # 결과를 저장할 리스트
		tempArr = [] # 계수를 저장할 리스트

		# 계수를 저장하기 위한 길이 정의 (중복제거한 원소의 갯수와 입력리스트 내의 최댓값 비교)
		setLen = len(set(self.arr)) if len(set(self.arr)) > max(self.arr) else max(self.arr)+1

		# 결과 리스트를 입력 리스트 길이만큼 0으로 초기화
		for i in range(length):
			sortedArr.append(0)

		# 계수 리스트는 계수 길이에 맞게 0으로 초기화
		for j in range(setLen):
			tempArr.append(0)

		# 입력 리스트 값을 인덱스로 한 계수 리스트의 값 증가
		for i in range(length):
			tempArr[self.arr[i]]+=1

		# tempArr[lastIndex] == lastIndex보다 작거나 같은 원소의 총 개수(누적합)
		for j in range(1,setLen):
			tempArr[j] += tempArr[j-1]
		print('tempArr = '+str(tempArr))

		# 결과 리스트에 할당
		for i in range(length-1,-1,-1):
			sortedArr[tempArr[self.arr[i]]-1] = self.arr[i]
			print('i='+str(i)+'\t-> '+str(self.arr[i])+'\t'+str(sortedArr))
			tempArr[self.arr[i]] -= 1
			print('tempArr = '+ str(tempArr) + '\n')

		return sortedArr

## TEST ##
if __name__ == "__main__":
	testArr = [1,0,4,6,5,5,3,7,4,0,1]
	counting = CountingSort(testArr)
	print('RESULT = ' + str(counting.sort()))	
	# RESULT = [0, 0, 1, 1, 3, 4, 4, 5, 5, 6, 7]

