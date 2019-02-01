#Garv Sachdeva
#2015B4A7055P

from Tkinter import *
from time import *

coordinates = [ [ [],[200,100],[300,100],[400,100],[500,100],[] ],
    			[ [150,200],[250,200],[350,200],[450,200],[550,200],[] ],
				[ [100,300],[200,300],[300,300],[400,300],[500,300],[600,300] ],
    			[ [150,400],[250,400],[350,400],[450,400],[550,400],[] ],
         		[ [],[200,500],[300,500],[400,500],[500,500],[]] ]

def canvas(root):
	canvas = Canvas(root,width = 700 , height = 550)
	canvas.pack()
	ui(root)
	return canvas


def ui(root):
	bot = Frame(root ,pady = 10, padx = 10)
	bot.pack(side = TOP)
	def close_window ():
		root.destroy()
		raise SystemExit 

	button = Button (bot, text = "Quit", command = close_window)
	#button.pack()
	l = Label(bot,text = " Instructions ")
	l.grid(row = 0,column = 0 )
	l3 = Label(bot,text = " Player 1(Human) White , Player 2(BOT) Black ",font = ("",12))
	l3.grid(row = 1,column = 0 )
	l1 = Label(bot,text = "1. To move,enter your input in console ")
	l1.grid(row = 2,column = 0 )
	l1 = Label(bot,text = "2. Please check the input format in the document provided.")
	l1.grid(row = 3,column = 0 )
	l2 = Label(bot,text = "3. After your move press Enter in the console to see the BOT's move")
	l2.grid(row = 4,column = 0 )
	l5 = Label(bot,text = "4. Repeat till the game ends. Press Quit to exit.")
	l5.grid(row = 5,column = 0 )
	button.grid(row = 6,column = 0 )
	l.config( font = ("",20))
	button.config(width = 30)
	#button = Button(None, text = "Next move")
	


def draw(canvas):

	canvas.create_text(65, 50, anchor=W,text="X",font = ("",12))
	canvas.create_text(100-5, 50, anchor=W,text="0",font = ("",12))
	canvas.create_text(150-5, 50, anchor=W,text="1",font = ("",12))
	canvas.create_text(200-5, 50, anchor=W,text="2",font = ("",12))
	canvas.create_text(250-5, 50, anchor=W,text="3",font = ("",12))
	canvas.create_text(300-5, 50, anchor=W,text="4",font = ("",12))
	canvas.create_text(350-5, 50, anchor=W,text="5",font = ("",12))
	canvas.create_text(400-5, 50, anchor=W,text="6",font = ("",12))
	canvas.create_text(450-5, 50, anchor=W,text="7",font = ("",12))
	canvas.create_text(500-5, 50, anchor=W,text="8",font = ("",12))
	canvas.create_text(550-5, 50, anchor=W,text="9",font = ("",12))
	canvas.create_text(600-5, 50, anchor=W,text="10",font = ("",12))

	canvas.create_text(50,70, anchor=W,text="Y",font = ("",12))
	canvas.create_text(50,100, anchor=W,text="0",font = ("",12))
	canvas.create_text(50,200, anchor=W,text="1",font = ("",12))
	canvas.create_text(50,300, anchor=W,text="2",font = ("",12))
	canvas.create_text(50,400, anchor=W,text="3",font = ("",12))
	canvas.create_text(50,500, anchor=W,text="4",font = ("",12))

	canvas.create_line(45,40,80,80 ,fill = "black",width=3)
	canvas.create_line(200,100,500,100 ,fill = "orange",width=3)
	canvas.create_line(150,200,550,200 ,fill = "orange",width=3)
	canvas.create_line(100,300,600,300 ,fill = "orange",width=3)
	canvas.create_line(150,400,550,400 ,fill = "orange",width=3)
	canvas.create_line(200,500,500,500 ,fill = "orange",width=3)

	canvas.create_line(100,300,200,500 ,fill = "orange",width=3)
	canvas.create_line(150,200,300,500 ,fill = "orange",width=3)
	canvas.create_line(200,100,400,500 ,fill = "orange",width=3)
	canvas.create_line(300,100,500,500 ,fill = "orange",width=3)
	canvas.create_line(400,100,550,400 ,fill = "orange",width=3)
	canvas.create_line(500,100,600,300 ,fill = "orange",width=3)

	canvas.create_line(100,300,200,100 ,fill = "orange",width=3)
	canvas.create_line(150,400,300,100 ,fill = "orange",width=3)
	canvas.create_line(200,500,400,100 ,fill = "orange",width=3)
	canvas.create_line(300,500,500,100 ,fill = "orange",width=3)
	canvas.create_line(400,500,550,200 ,fill = "orange",width=3)
	canvas.create_line(500,500,600,300 ,fill = "orange",width=3)

	return canvas

def boardshow(board,canvas):
	canvas.delete(ALL)
	draw(canvas)
	for i in range(5):
		for j in range(11):
			
			if( board[i][j] == 1):
				x = coordinates[i][j/2][0]
				y = coordinates[i][j/2][1]
				canvas.create_oval(x-25, y-25, x+25, y+25,fill="white")
			if( board[i][j] == 2):
				x = coordinates[i][j/2][0]
				y = coordinates[i][j/2][1]
				canvas.create_oval(x-25, y-25, x+25, y+25,fill="black")
	