#Garv Sachdeva
#2015B4A7055P

import random
from time import time
from copy import deepcopy

#initial no of pieces
pieces=10

arr=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#possible moves (y,x)
mv = [ [1,1],[1,-1],[-1,1],[-1,-1],[0,2],[0,-2],
	   [2,2],[2,-2],[-2,2],[-2,-2],[0,4],[0,-4] ]

#random state generator 
def initial_state_generator():
    for x in range(pieces):
    	k = random.randint(0,23)
    	while( arr[k%24] != 0 ):
        	k=k+1
      	arr[k%24] = 1
      	c = random.randint(0,23)
      	while( arr[c%24] != 0):
        	c=c+1
      	arr[c%24] = 2
    return arr

#convert linear from to matrix form
def convert(arr):
	board = [['#','#',arr[0],'#',arr[1],'#',arr[2],'#',arr[3],'#','#' ],
			 ['#',arr[4],'#',arr[5],'#',arr[6],'#',arr[7],'#',arr[8],'#' ],
			 [arr[9],'#',arr[10],'#',arr[11],'#',arr[12],'#',arr[13],'#',arr[14] ],
			 ['#',arr[15],'#',arr[16],'#',arr[17],'#',arr[18],'#',arr[19],'#' ],
			 ['#','#',arr[20],'#',arr[21],'#',arr[22],'#',arr[23],'#','#' ]
			]
	return board

#print current board config
def show(board):
	for i in range(5):
		for j in range(11):
			if(board[i][j] == '#'):
				print(' '),
				continue
			print(board[i][j]),
		print (" ")

#checks if a move is valid or not
def is_valid(board,i,j,x,y):
	pox = i+x
	poy = j+y
	if(pox < 0 or pox > 4 or poy < 0 or poy > 10 or board[i][j] == 0 or board[i][j] == '#'):
		return 0
	if(board[pox][poy] != 0):
		return 0
	if(abs(x)+abs(y) == 4 and (board[i][j] == board[i + x/2][j + y/2] or board[i + x/2][j + y/2] == 0) ):
		return 0
	#print(i+1,j/2+1,x,y)
	return 1

#count no of whites and blacks on the board
def count_pieces(board):
	white = 0
	black = 0
	for i in range(5):
		for j in range(11):
			if(board[i][j] == 1):white=white+1
			if(board[i][j] == 2):black=black+1
	return [white,black]

#evaluation function(for AI) add .x no of corners
def eval(board):
	return count_pieces(board)[1] - count_pieces(board)[0]

#execute move and return new board
def exe_move(board,i,j,x,y):
 	copyboard = deepcopy(board)
 	temp = copyboard[i][j]
 	copyboard[i][j] = 0
 	copyboard[i+x][j+y] = temp
 	if(abs(x)+abs(y) == 4 and copyboard[i+x/2][j+y/2] != '#'):
 		copyboard[i+x/2][j+y/2] = 0
 	#print eval(copyboard)
 	return copyboard

#returns all the possible successors player turn is given  
def Successor_function(board , turn):
	succ = []
	for i in range(5):
		for j in range(11):
			for m in mv:
				if( turn==board[i][j] and is_valid(board,i,j,m[0],m[1]) == 1):
					s = exe_move(board,i,j,m[0],m[1])
					#show(s)
					succ.append(s)
	return succ

#check if terminal state
def Terminal_test(board):
	if(count_pieces(board)[0] == 0 or count_pieces(board)[1] == 0):
		return True
	return False

def eval_teminal(board):
	return count_pieces(board)[1] - count_pieces(board)[0]

