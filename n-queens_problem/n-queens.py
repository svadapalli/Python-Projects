import matplotlib.pyplot as plt
import numpy as np

def initialize(n):
	for key in ['queen', 'row', 'col', 'dNWtoSE', 'dNEtoSW']:
		board[key] = {}
	for i in range(n):
		board['queen'][i] = -1
		board['row'][i] = 0
		board['col'][i] = 0
	for i in range(-(n-1),n):
		board['dNEtoSW'][i] = 0
	for i in range(2*n-1):
		board['dNWtoSE'][i] = 0

def printboard(board):
	## normal print with just the indeces for each queen
	# for row in sorted(board['queen'].keys()):
	# 	print (row, board['queen'][row])

	## to print all possible solutions for given 'n'

	# for row in sorted(board['queen'].keys()):
	# 	print (row, board['queen'][row]),
	# print ("")



## To print the board with matplotlib ##pretty
	list = []
	for row in sorted(board['queen'].keys()):
		list.append(board['queen'][row])
	board = np.zeros((n,n,3))
	board += 0.5 # "Black" color
	board[::2, ::2] = 1 # "White" color
	board[1::2, 1::2] = 1 # "White" color

	fig, ax = plt.subplots()
	ax.imshow(board, interpolation='nearest')

	queen = plt.imread('queen.png')
	extent = np.array([-0.4, 0.4, -0.4, 0.4]) # (0.5 would be the full cell)
	for y, x in enumerate(list):
	    ax.imshow(queen, extent=extent + [x, x, y, y])

	ax.set(xticks=[], yticks=[])
	ax.axis('image')

	plt.show()
		

def free(i,j):
	return (board['queen'][i] == -1 and board['row'][i] == 0 and board['col'][j] == 0 and board['dNWtoSE'][i+j] == 0 and board['dNEtoSW'][j-i] == 0)

def addqueen(i,j):
	board['queen'][i] = j
	board['row'][i] = 1
	board['col'][j] = 1
	board['dNWtoSE'][i+j] = 1
	board['dNEtoSW'][j-i] = 1

def undoqueen(i,j):
	board['queen'][i] = -1
	board['row'][i] = 0
	board['col'][j] = 0
	board['dNWtoSE'][i+j] = 0
	board['dNEtoSW'][j-i] = 0

def placequeen(i):
	## For one solution
	n = len(board['queen'].keys())
	for j in range(n):
		if free(i,j):
			addqueen(i,j)
			if i == n-1:
				return (True)
			else:
				extendsolution = placequeen(i+1)
			if extendsolution:
				return(True)
			else:
				undoqueen(i,j)
	else:
		return(False)

	## For all possible solutions, use below code and change the Print board function

	# n = len(board['queen'].keys())
	# for j in range(n):
	# 	if free(i,j):
	# 		addqueen(i,j)
	# 		if i == n-1:
	# 			printboard()
	# 		else:
	# 			extendsolution = placequeen(i+1)
	# 		undoqueen(i,j)


board = {}
n = int(input("Please enter the number of Queens : "))
initialize(n)
if placequeen(0):
	printboard(board)