#Garv Sachdeva
#2015B4A7055P

from Tkinter import *
from agent import *
from pruning import *
from human import *
from gui import *
from xd import *
from time import *

#turn 1 => player 1 (Human : White)
#turn 2 => player 2 (Bot : Black)
#1 simple minimax
#2 minimax with alpha beta pruning

I= 0
I = input("Enter 1 for simple minimax agent, enter 2 for minimax with pruning agent: ")

board = convert(initial_state_generator())
root = Tk()
canvas = canvas(root)

print('Start state')
show(board)
boardshow(board,canvas)

while(Terminal_test(board) == False):
	print('Player 1')
	board = human(board)
	show(board)
	boardshow(board,canvas)
	#input enter
	raw_input('Press enter to continue: ')

	print('Player 2')
	if(I==1):
		board = minimaxhead(board)
	if(I==2):
		board = minimax_prun_head(board)
	show(board)
	boardshow(board,canvas)

print "The game has ended"

root.mainloop()