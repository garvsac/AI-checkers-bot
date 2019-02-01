#Garv Sachdeva
#2015B4A7055P

from xd import *

def human(board):
	x=0
	y=0
	while(x < 0 or x > 4 or y < 0 or y > 10 or board[x][y] != 1):
		y = input("X initial: ")
		x = input("Y initial: ")
		if( x < 0 or x > 4 or y < 0 or y > 10 or board[x][y] != 1):
			print 'Not a valid input'
	i=0
	j=0
	while( is_valid(board,x,y,i,j)==0 ):
		j1 = input("X final: ")	
		i1 = input("Y final: ")
		i = i1 - x
		j = j1 - y
		if( is_valid(board,x,y,i,j)==0 ):
			print 'Not a valid input'
	return exe_move(board,x,y,i,j)

	 
