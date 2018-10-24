# 2013311806 김탁영 - heapSort

class heapSort:
	def __init__(self, arr):
		self.arr = arr

	def sort(self):
		maxIndex = len(self.arr)-1
		self.buildHeap()
		for i in range(maxIndex,0,-1):
			self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
			self.heapify(0, i-1)

		return self.arr

	def buildHeap(self):
		maxIndex = len(self.arr)-1
		for i in range(maxIndex//2, -1, -1): # 최대 인덱스의 절반 지점부터 시작한다.
			self.heapify(i, maxIndex)

	def heapify(self, index, maxIndex): # arr[k]를 루트로 하는 트리가 힙성질 만족하도록 수선
		left = 2*index + 1 # index는 0부터 시작
		right = 2*index + 2
		smaller = None
		
		if right <= maxIndex: # 자식노드 2개
			if self.arr[left] < self.arr[right]:
				smaller = left
			else:
				smaller = right

		elif left <= maxIndex: # 자식노드 1개
			smaller = left
		else: # 자식노드 0개
			pass

		# 현재 인덱스의 노드와 left/right 중 smaller 인덱스와 비교, 현재 인덱스가 더 크다면 위치를 바꾼다.
		if smaller != None and self.arr[smaller] < self.arr[index]:
			self.arr[smaller], self.arr[index] = self.arr[index], self.arr[smaller]
			self.heapify(smaller, maxIndex)


## TEST ##
testArr = [8, 31, 48, 73, 3, 65, 20, 29, 11, 15]
heap = heapSort(testArr)
print('RESULT = ' + str(heap.sort()))	
# RESULT = [73, 65, 48, 31, 29, 20, 15, 11, 8, 3]
