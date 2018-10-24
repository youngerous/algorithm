### ReadMe 참조

# 엘리베이터의 방향 
def elevatorDirection(nowFloor, aimFloor):
	if nowFloor > aimFloor:
		direction = 'down'
		return direction
	elif nowFloor < aimFloor:
		direction = 'up'
		return direction

# 엘리베이터와 같은 방향인가? : 합승할 때 & tmp에서 cur로 옮길 때 사용
def sameDirection(elevatorDirection, now, goal):
	if (elevatorDirection == 'down') and (now > goal):
		return True
	elif (elevatorDirection == 'down') and (now < goal):
		return False
	elif (elevatorDirection == 'up') and (now < goal):
		return True
	elif (elevatorDirection == 'up') and (now > goal):
		return False


# 엘리베이터가 방향에 따라 움직임
def mainMove(elevatorDirection, nowFloor):
	if (elevatorDirection == 'down') and (nowFloor != 1):
		nowFloor -= 1	
		return nowFloor

	elif (elevatorDirection == 'up') and (nowFloor != 10):
		nowFloor += 1
		return nowFloor
	else:
		return nowFloor

# 엘리베이터의 도착 여부를 판단하는 함수
def isArrived(nowFloor, aimFloor):
	if nowFloor == aimFloor:
		return True
	else: 
		return False

#엘리베이터 도착하면 목록에서 삭제하는 함수 && 대기 시간 추가
def popList(tempOrder, currentOrder, nowFloor, waitingTime, time):
	tmplist = list(currentOrder)	
	if bool(currentOrder) == True:
		for i in range(len(tmplist)):	#currentOrder 를 그대로 쓰면 도착 승객을 pop할 때 for문에서 그만큼 빠져버리기 때문에 tmplist를 사용
			if nowFloor == tmplist[i][2]:
				waitingTime.append(time - tmplist[i][0])
				currentOrder.remove(tmplist[i])
				tmpHow(tempOrder, nowFloor, currentOrder)
			else: 
				continue
	return


# newOrder에서 tmp로 갈 것이냐 cur로 갈 것이냐를 결정
def newToWhere(time, nowFloor, newOrder, currentOrder, tempOrder):
	if bool(newOrder) == False:
		return
	else:	
		if time == newOrder[0][0]:
			if sameDirection(elevatorDirection(nowFloor, currentOrder[0][2]), newOrder[0][1], newOrder[0][2]) == True and nowFloor == newOrder[0][1]:
				currentOrder.append(newOrder[0])
				newOrder.remove(newOrder[0])

			else:
				tempOrder.append(newOrder[0])
				newOrder.remove(newOrder[0])

# tmp 목록 처리 함수 (cur로 갈 것이냐 tmp에 남을 것이냐)
def tmpHow(tempOrder, nowFloor, currentOrder):
	if bool(tempOrder) == False:
		return

	if bool(currentOrder) == True:
		tmplist = list(tempOrder)
		for index in range(len(tmplist)):	#tempOrder 를 그대로 쓰면 도착 승객을 pop할 때 for문에서 그만큼 빠져버리기 때문에 tmplist를 사용
			if (sameDirection(elevatorDirection(nowFloor, currentOrder[0][2]), tmplist[index][1], tmplist[index][2]) == True) and (nowFloor == tmplist[index][1]):
				currentOrder.append(tmplist[index])
				tempOrder.remove(tmplist[index])
			else:
				continue
		return

	else:
		tmplist = list(tempOrder)
		for index in range(1, len(tmplist)):	#tempOrder 를 그대로 쓰면 도착 승객을 pop할 때 for문에서 그만큼 빠져버리기 때문에 tmplist를 사용
			if (sameDirection(elevatorDirection(nowFloor, tmplist[0][1]), tmplist[index][1], tmplist[index][2]) == True) and (nowFloor == tmplist[index][1]):
				currentOrder.append(tmplist[index])
				tempOrder.remove(tmplist[index])
			else:
				continue
		return

# 현황 출력 함수 - 최종 결과만 보려면 내용을 주석처리하시면 됩니다.
def showProcess(newOrder, currentOrder, tempOrder, time, nowFloor):
	print('버튼 누르지 않음:',newOrder,'\n탑승중:', currentOrder, '\n기다리는중:',tempOrder,'\n시간:',time,'\n현위치:', nowFloor, '\n')	
	return


# 명령 입력 함수
def getInput(lists):
	lists = [(1, 1, 6), (2, 1, 6), (3, 6, 1), (4, 5, 1), (7, 6, 1)] 
	
	return lists


def main():
	#############변수선언#############
	time = 0
	nowFloor = 1 #엘리베이터의 현 위치
	currentOrder = []	#엘리베이터가 실행 중인 명령
	newOrder = []	#외부 승객의 요청
	tempOrder = []	#시간은 일치하나 방향이 달라 보류된 외부 승객들
	waitingTime = []	#대기 시간의 리스트


	newOrder = getInput(newOrder)	
	################################

	while bool(newOrder) == True:	#외부 승객이 더 이상 없으면 종료

		#엘리베이터 내부에 승객이 없고, 밖에서 기다리는 손님도 없을 때
		if (bool(currentOrder) == False) and (bool(tempOrder) == False):
			while time != newOrder[0][0]:
				time += 1
				showProcess(newOrder, currentOrder, tempOrder, time, nowFloor)

			tempOrder.append(newOrder[0])
			newOrder.remove(newOrder[0])
			showProcess(newOrder, currentOrder, tempOrder, time, nowFloor)


		#엘리베이터 내부에 승객이 없고, 밖에서 기다리는 손님이 있을 때
		elif (bool(currentOrder) == False) and (bool(tempOrder) == True):
			#엘리베이터가 최우선 대기 승객(tempOrder)이 있는 위치에 도달할 때까지 이동한다. (tempOrder의 첫 튜플에 도달할 때까지 이동)
			while isArrived(nowFloor, tempOrder[0][1]) == False:
				nowFloor = mainMove(elevatorDirection(nowFloor, tempOrder[0][1]), nowFloor)
				time += 1
				showProcess(newOrder, currentOrder, tempOrder, time, nowFloor)

				tmpHow(tempOrder, nowFloor, currentOrder)

				if bool(newOrder) == True:
					if time == newOrder[0][0]:	#이동하는 중에 이동하려는 방향이 같은 외부 승객이 버튼을 눌렀을 때
						if sameDirection(elevatorDirection(nowFloor, tempOrder[0][1]), newOrder[0][1], newOrder[0][2]) == True and nowFloor == newOrder[0][1]:
							currentOrder.append(newOrder[0])
							newOrder.remove(newOrder[0])
						else:	#방향이 다르면 tempOrder에 추가한다.
							tempOrder.append(newOrder[0])
							newOrder.remove(newOrder[0])
						showProcess(newOrder, currentOrder, tempOrder, time, nowFloor)

				if bool(currentOrder) == True:
					break
				showProcess(newOrder, currentOrder, tempOrder, time, nowFloor)

			tmpHow(tempOrder, nowFloor, currentOrder)
			if bool(currentOrder) == True:
				continue

			currentOrder.append(tempOrder[0])	#tempOrder의 첫 번째 튜플에 도달하면 currentOrder에 추가한다.
			tempOrder.remove(tempOrder[0])
			showProcess(newOrder, currentOrder, tempOrder, time, nowFloor)

			tmpHow(tempOrder, nowFloor, currentOrder)
	

		#엘리베이터 내부에 승객이 있을 때
		else:	
			#승객을 태운 엘리베이터가 목적지에 도착할 때까지
			while isArrived(nowFloor, currentOrder[0][2]) == False: 
				nowFloor = mainMove(elevatorDirection(nowFloor, currentOrder[0][2]), nowFloor)
				time += 1

				newToWhere(time, nowFloor, newOrder, currentOrder, tempOrder)
				tmpHow(tempOrder, nowFloor, currentOrder)
				popList(tempOrder, currentOrder, nowFloor, waitingTime, time)
				showProcess(newOrder, currentOrder, tempOrder, time, nowFloor)

				if bool(currentOrder) == False:	#currentOrder에 명령이 없을 때, break하여 if문이나 elif문으로 이동시킨다.
					break

				if bool(currentOrder) == False and bool(newOrder) == False and bool(tempOrder) == False :	#모든 명령을 수행하면 break
					break

	while (bool(currentOrder) == True) or (bool(tempOrder) == True):	#외부 승객은 없으나, 대기 손님이 있을 경우
		# 승객이 탑승 중일 때
		if bool(currentOrder) == True:
			########### 위에 else와 똑같은 부분
			while isArrived(nowFloor, currentOrder[0][2]) == False: #승객을 태운 엘리베이터가 목적지에 도착할 때까지
				nowFloor = mainMove(elevatorDirection(nowFloor, currentOrder[0][2]), nowFloor)
				time += 1

				newToWhere(time, nowFloor, newOrder, currentOrder, tempOrder)
				tmpHow(tempOrder, nowFloor, currentOrder)
				popList(tempOrder, currentOrder, nowFloor, waitingTime, time)
						
				showProcess(newOrder, currentOrder, tempOrder, time, nowFloor)

				if bool(currentOrder) == False:	#currentOrder에 명령이 없으면 
					break
				if bool(currentOrder) == False and bool(newOrder) == False and bool(tempOrder) == False :
					break

		else:	###########위의 elif부분과 같음(currentOrder 없고 tempOrder 있을 때)
			while isArrived(nowFloor, tempOrder[0][1]) == False:
				nowFloor = mainMove(elevatorDirection(nowFloor, tempOrder[0][1]), nowFloor)
				time += 1
				showProcess(newOrder, currentOrder, tempOrder, time, nowFloor)
				tmpHow(tempOrder, nowFloor, currentOrder)
				
				if bool(currentOrder) == True:				
					showProcess(newOrder, currentOrder, tempOrder, time, nowFloor)
					break
			if bool(currentOrder) == True:
				continue

			currentOrder.append(tempOrder[0])
			tempOrder.remove(tempOrder[0])
			showProcess(newOrder, currentOrder, tempOrder, time, nowFloor)


			tmpHow(tempOrder, nowFloor, currentOrder)
			
  
	print('대기 시간의 리스트:', waitingTime)
	print('대기 시간의 총합:', sum(waitingTime))
	print('마지막 손님이 내린 시간:', time)
	return time, sum(waitingTime)



main() 
