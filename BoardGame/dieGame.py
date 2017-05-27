import matplotlib.pyplot as plt
import numpy as np
from random import randint

def initialize(m,n):
	for row in range(m):
		board[row] = {}
	for row in range(m):
		for col in range(n):
			board[row][col] = 0
	
def playGame(board):
	initPos = (0, 0)
	list = []
	img = 'cross.png'
	while(checkRow(board) == True and checkCol(board) == True):
		raw_input("Please press enter to roll the die... ")
		roll = randint(1,6)
		print "Die rolled is: "+str(roll)
		newPos = findNewPos(initPos, roll)
		print "New X placed at: "+str(newPos)
		i = newPos[0]
		j = newPos[1]
		board[i][j] = 1
		initPos = newPos
		list.append(newPos)
		printboard(list, img)

	return initPos
	#return board



def checkRow(board):
	for row in range(m):
		sum = 0
		for col in range(n):
			sum += board[row][col]
			if sum == n:
				return False
	return True
	

def checkCol(board):
	for col in range(n):
		sum = 0
		for row in range(m):
			sum += board[row][col]
			if sum == m:
				return False
	return True


def findNewPos(initPos, roll):
	i = initPos[0]
	j = initPos[1]
	if i == m-1:
		#print "entered last row"
		if i%2 == 0:
			if roll <= ((n-1)-j):
				newPos = (i, j+roll)
				return newPos
			if roll > ((n-1)-j):
				consumedInCurr = (n-1)-j
				if roll - consumedInCurr > n:
					newPos = (1, n-(roll - consumedInCurr -n))
					return newPos
				newPos = (0, (roll-consumedInCurr-1))
				return newPos

		if i%2 != 0:
			if roll <= j:
				newPos = (i, j-roll)
				return newPos
			if roll > j:
				consumedInCurr = j
				if roll - consumedInCurr > n:
					newPos = (1, n-(roll-consumedInCurr-n))
					return newPos
				newPos = (0, (roll-j)-1)
				return newPos

	if i%2 == 0:
		if roll <= ((n-1)-j):
			newPos = (i, j+roll)
			return newPos
		if roll > ((n-1)-j):
			consumedInCurr = (n-1)-j
			if roll - consumedInCurr > n:
				if i+1 == m-1:
					newPos = (0,(roll-consumedInCurr-n)-1)
					return newPos
				newPos = (i+2, (roll - consumedInCurr -n)-1)
				return newPos
			newPos = (i+1, n-(roll-consumedInCurr))
			return newPos

	if i%2 != 0:
		if roll <= j:
			newPos = (i, j-roll)
			return newPos
		if roll > j:
			consumedInCurr = j
			if roll - consumedInCurr > n:
				if i+1 == m-1:
					newPos = (0, (roll-consumedInCurr-n)-1)
					return newPos
				newPos = (i+2, n-(roll-consumedInCurr-n))
				return newPos
			newPos = (i+1, (roll-j)-1)
			return newPos

def printboard(list, img):
	
	board = np.zeros((m,n,3))
	board += 0.5 # "Black" color
	board[::2, ::2] = 1 # "White" color
	board[1::2, 1::2] = 1 # "White" color

	fig, ax = plt.subplots()
	ax.imshow(board, interpolation='nearest')
	ax.set_ylim(m, 0)

	cross = plt.imread(img)
	extent = np.array([-0.4, 0.4, -0.4, 0.4])
	for y, x in list:
	    ax.imshow(cross, extent=extent + [x, x, y, y])

	ax.set(xticks=[], yticks=[])
	ax.axis('image')

	plt.waitforbuttonpress()
	plt.close()

def findCheckRow(k, l):
	for x in range(n):
		if board[k][x] == 0:
			return False
	return True

def findCheckCol(k, l):
	for y in range(m):
		if board[y][l] == 0:
			return False
	return True

def drawWinBoard(k,l):
	listLast = []
	img = 'cross_red.png'
	rowWin = findCheckRow(k,l)
	if rowWin == True:
		for j in range(n):
			listLast.append((k,j))
		printboard(listLast,img)

	colWin = findCheckCol(k, l)
	if colWin == True:
		for i in range(m):
			listLast.append((i,l))
		printboard(listLast, img)


board = {}
m = int(input("Please enter the number of rows : "))
n = int(input("Please enter the number of columns : "))
initialize(m,n)

lastPos = playGame(board)
k = lastPos[0]
l = lastPos[1]
drawWinBoard(k,l)

print "You win!"