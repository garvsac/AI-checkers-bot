from Tkinter import *
import random
import time

class game_controller(object):
    
    def ai(self):
#       randTop, randLeft = random.choice(self.canvas.data["BoardVal"])
#       self.canvas.itemconfig(self.canvas.data["Board"][randTop][randLeft][0], fill='blue')
#       self.canvas.data["BoardVal"].remove( [randTop, randLeft] )
         
        for d_top, topRow in self.canvas.data["Checker"].iteritems():
            for d_left, checker in topRow.iteritems():
                moveList = []
                cutList = []
                test = []
                
                listLen = len(self.cutList)
                
                if self.canvas.itemcget(checker[0], "fill") == self.computerColor:
                    if "man" in self.canvas.itemcget(checker[0], "tag"):
                        test.append(self.test_man_cutList( d_top, d_left, "topLeft"))
                        test.append(self.test_man_cutList( d_top, d_left, "topRight"))
                        test.append(self.test_man_cutList( d_top, d_left, "bottomLeft"))
                        test.append(self.test_man_cutList( d_top, d_left, "bottomRight"))
                    elif "king" in self.canvas.itemcget(checker[0], "tag"):
                        test.append(self.test_king_cutList(d_top, d_left, "topLeft"))
                        test.append(self.test_king_cutList(d_top, d_left, "topRight"))
                        test.append(self.test_king_cutList(d_top, d_left, "bottomLeft"))
                        test.append(self.test_king_cutList(d_top, d_left, "bottomRight"))
                
                
                if test:
                    for tuple in test:
                        if tuple[0]:
                            moveList.append(tuple[0])
                        if tuple[1]:
                            cutList.append(tuple[1])
                                
                    if moveList:
                        self.selectMove.append([d_top, d_left, moveList])
                    if cutList:
                        self.selectCut.append([d_top, d_left, cutList])
        
        if self.selectCut:
            checker = random.choice(self.selectCut)
            move = random.choice(checker[2])[0] 
            
            self.moveChecker(move[0], move[1], checker[0], checker[1])
            
            if "man" in self.canvas.itemcget(self.canvas.data["Checker"][move[0]][move[1]][0], "tag"):
                self.removeChecker(move[0], move[1], move[2], checker[0], checker[1])
                if move[0] == 355:
                    self.canvas.itemconfig(self.canvas.data["Checker"][move[0]][move[1]][0], tag='king', dash=(5, 1, 2, 1), dashoff=3, width=5)
            elif "king" in self.canvas.itemcget(self.canvas.data["Checker"][move[0]][move[1]][0], "tag"):
                self.removeChecker(move[0], move[1], move[2], checker[0], checker[1])
        elif self.selectMove:
            checker = random.choice(self.selectMove)
            move = random.choice(checker[2])[0] 
            
            self.moveChecker(move[0], move[1], checker[0], checker[1])
            
            if "man" in self.canvas.itemcget(self.canvas.data["Checker"][move[0]][move[1]][0], "tag"):
                if move[0] == 355:
                    self.canvas.itemconfig(self.canvas.data["Checker"][move[0]][move[1]][0], tag='king', dash=(5, 1, 2, 1), dashoff=3, width=5)
        
        else:
            print "game over"
            
        self.selectCut = []
        self.selectMove = []
                
        self.cutList = []
        self.moveList = []
        self.turn = "player"
    
    def mouseCalc(self, x, y):
        return int( (x -5) // 50 ) * 50 + 5, int( (y -5) // 50 ) * 50 + 5
    
    def get_dir(self, dir):
        if dir == "topLeft":
            topDir = -1
            leftDir = -1
        elif dir == "topRight":
            topDir = -1
            leftDir = 1
        elif dir == "bottomLeft":
            topDir = 1
            leftDir = -1
        elif dir == "bottomRight":
            topDir = 1
            leftDir = 1
            
        return topDir, leftDir
    
    def removeChecker(self, top, left, dir, selectTop, selectLeft):
        topDir, leftDir = self.get_dir(dir)
        topDir *= -1
        leftDir *= -1
        
        for count in range(1, abs(((top-5) - (selectTop-5)) / 50)+1):
            if left+(50*count*leftDir) in self.canvas.data["Checker"][top+(50*count*topDir)]:
                self.canvas.delete(self.canvas.data["Checker"][top+(50*count*topDir)][left+(50*count*leftDir)][0])
                                
                self.canvas.data["Checker"][top+(50*count*topDir)].pop( left+(50*count*leftDir) )   
                
    def moveChecker(self, top, left, selectTop, selectLeft):
        self.canvas.coords(  self.canvas.data["Checker"][selectTop][selectLeft][0], left, top, left+50, top+50  )
        self.canvas.data["Checker"][top][left] = self.canvas.data["Checker"][selectTop][selectLeft]
        self.canvas.data["Checker"][selectTop].pop( selectLeft )
    
    def man_cutList(self, top, left, dir, moveList, cutList, moveBool=True):
        topDir, leftDir = self.get_dir(dir)
        
        if top+(topDir*50) in self.canvas.data["Checker"]:
            if left+(leftDir*50) not in self.canvas.data["Checker"][top+(topDir*50)]:
                if left+(leftDir*50) in self.canvas.data["Board"][top+(topDir*50)]:
                    if self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "fill") == self.playerColor and dir in ("topLeft", "topRight") and moveBool:
                        moveList.append( [top+(topDir*50), left+(leftDir*50), "move" ] )
                    elif self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "fill") == self.computerColor and dir in ("bottomLeft", "bottomRight") and moveBool:
                        moveList.append( [top+(topDir*50), left+(leftDir*50), "move" ] )
            elif self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "fill") == self.playerColor:
                if self.canvas.itemcget(self.canvas.data["Checker"][top+(topDir*50)][left+(leftDir*50)][0], "fill") == self.computerColor:
                    if top+(topDir*100) in self.canvas.data["Checker"] and left+(leftDir*100) not in self.canvas.data["Checker"][top+(topDir*100)] and left+(leftDir*100) in self.canvas.data["Board"][top+(topDir*100)]:
                        cutList.append( [top+(topDir*100), left+(leftDir*100), dir ] )      
            elif self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "fill") == self.computerColor:
                if self.canvas.itemcget(self.canvas.data["Checker"][top+(topDir*50)][left+(leftDir*50)][0], "fill") == self.playerColor:
                    if top+(topDir*100) in self.canvas.data["Checker"] and left+(leftDir*100) not in self.canvas.data["Checker"][top+(topDir*100)] and left+(leftDir*100) in self.canvas.data["Board"][top+(topDir*100)]:
                        cutList.append( [top+(topDir*100), left+(leftDir*100), dir ] )
                        
                        
    def king_cutList(self, top, left, dir, moveList, cutList, moveBool=True):
        topDir, leftDir = self.get_dir(dir)

        count = 1
        self.cut = False
        
        while True:
            if top+(50*count*topDir) in self.canvas.data["Checker"]:
                if left+(50*count*leftDir) not in self.canvas.data["Checker"][top+(50*count*topDir)]:
                    if not self.cut:
                        if moveBool:
                            moveList.append( [top+(50*count*topDir), left+(50*count*leftDir), "move" ] )
                    else:
                        cutList.append( [top+(50*count*topDir), left+(50*count*leftDir), dir ] )
                elif self.canvas.itemcget(self.canvas.data["Checker"][top+(50*count*topDir)][left+(50*count*leftDir)][0], "fill") == self.computerColor and self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "fill") == self.playerColor:
                    if top+(50*count*topDir)+(topDir*50) in self.canvas.data["Checker"] and left+(50*count*leftDir)+(leftDir*50) not in self.canvas.data["Checker"][top+(50*count*topDir)+(topDir*50)] and left+(50*count*leftDir)+(leftDir*50) in self.canvas.data["Board"][top+(50*count*topDir)+(topDir*50)]:
                        self.cut = True
                        cutList.append( [top+(50*count*topDir)+(topDir*50), left+(50*count*leftDir)+(leftDir*50), dir ] )
                    else:
                        break
                elif self.canvas.itemcget(self.canvas.data["Checker"][top+(50*count*topDir)][left+(50*count*leftDir)][0], "fill") == self.playerColor and self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "fill") == self.computerColor:
                    if top+(50*count*topDir)+(topDir*50) in self.canvas.data["Checker"] and left+(50*count*leftDir)+(leftDir*50) not in self.canvas.data["Checker"][top+(50*count*topDir)+(topDir*50)] and left+(50*count*leftDir)+(leftDir*50) in self.canvas.data["Board"][top+(50*count*topDir)+(topDir*50)]:
                        self.cut = True
                        cutList.append( [top+(50*count*topDir)+(topDir*50), left+(50*count*leftDir)+(leftDir*50), dir ] )
                    else:
                        break
                else:
                    break
            else:
                break
                        
            count+=1

    def test_man_cutList(self, top, left, dir, moveBool=True):
        topDir, leftDir = self.get_dir(dir)
        
        moveList = []
        cutList = []
        
        if top+(topDir*50) in self.canvas.data["Checker"]:
            if left+(leftDir*50) not in self.canvas.data["Checker"][top+(topDir*50)]:
                if left+(leftDir*50) in self.canvas.data["Board"][top+(topDir*50)]:
                    if self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "fill") == self.playerColor and dir in ("topLeft", "topRight") and moveBool:
                        moveList.append( [top+(topDir*50), left+(leftDir*50), "move" ] )
                    elif self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "fill") == self.computerColor and dir in ("bottomLeft", "bottomRight") and moveBool:
                        moveList.append( [top+(topDir*50), left+(leftDir*50), "move" ] )
            elif self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "fill") == self.playerColor:
                if self.canvas.itemcget(self.canvas.data["Checker"][top+(topDir*50)][left+(leftDir*50)][0], "fill") == self.computerColor:
                    if top+(topDir*100) in self.canvas.data["Checker"] and left+(leftDir*100) not in self.canvas.data["Checker"][top+(topDir*100)] and left+(leftDir*100) in self.canvas.data["Board"][top+(topDir*100)]:
                        cutList.append( [top+(topDir*100), left+(leftDir*100), dir ] )      
            elif self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "fill") == self.computerColor:
                if self.canvas.itemcget(self.canvas.data["Checker"][top+(topDir*50)][left+(leftDir*50)][0], "fill") == self.playerColor:
                    if top+(topDir*100) in self.canvas.data["Checker"] and left+(leftDir*100) not in self.canvas.data["Checker"][top+(topDir*100)] and left+(leftDir*100) in self.canvas.data["Board"][top+(topDir*100)]:
                        cutList.append( [top+(topDir*100), left+(leftDir*100), dir ] )
        
        return moveList, cutList                
                        
    def test_king_cutList(self, top, left, dir, moveBool=True):
        topDir, leftDir = self.get_dir(dir)
        
        moveList = []
        cutList = []
        
        count = 1
        self.cut = False
        
        while True:
            if top+(50*count*topDir) in self.canvas.data["Checker"]:
                if left+(50*count*leftDir) not in self.canvas.data["Checker"][top+(50*count*topDir)]:
                    if left+(50*count*leftDir) in self.canvas.data["Board"][top+(50*count*topDir)]:
                        if not self.cut:
                            if moveBool:
                                moveList.append( [top+(50*count*topDir), left+(50*count*leftDir), "move" ] )
                        else:
                            cutList.append( [top+(50*count*topDir), left+(50*count*leftDir), dir ] )
                elif self.canvas.itemcget(self.canvas.data["Checker"][top+(50*count*topDir)][left+(50*count*leftDir)][0], "fill") == self.computerColor and self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "fill") == self.playerColor:
                    if top+(50*count*topDir)+(topDir*50) in self.canvas.data["Checker"] and left+(50*count*leftDir)+(leftDir*50) not in self.canvas.data["Checker"][top+(50*count*topDir)+(topDir*50)] and left+(50*count*leftDir)+(leftDir*50) in self.canvas.data["Board"][top+(50*count*topDir)+(topDir*50)]:
                        self.cut = True
                        cutList.append( [top+(50*count*topDir)+(topDir*50), left+(50*count*leftDir)+(leftDir*50), dir ] )
                    else:
                        break
                elif self.canvas.itemcget(self.canvas.data["Checker"][top+(50*count*topDir)][left+(50*count*leftDir)][0], "fill") == self.playerColor and self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "fill") == self.computerColor:
                    if top+(50*count*topDir)+(topDir*50) in self.canvas.data["Checker"] and left+(50*count*leftDir)+(leftDir*50) not in self.canvas.data["Checker"][top+(50*count*topDir)+(topDir*50)] and left+(50*count*leftDir)+(leftDir*50) in self.canvas.data["Board"][top+(50*count*topDir)+(topDir*50)]:
                        self.cut = True
                        cutList.append( [top+(50*count*topDir)+(topDir*50), left+(50*count*leftDir)+(leftDir*50), dir ] )
                    else:
                        break
                else:
                    break
            else:
                break
                        
            count+=1
            
        return moveList, cutList
            
    def click_cutList(self, top, left):
        self.select = [top, left]
        self.canvas.itemconfig(self.canvas.data["Board"][top][left][0], fill='red')
                
        if "man" in self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "tag"):
            self.man_cutList( top, left, "topLeft", self.moveList, self.cutList)
            self.man_cutList( top, left, "topRight", self.moveList, self.cutList)
            self.man_cutList( top, left, "bottomLeft", self.moveList, self.cutList)
            self.man_cutList( top, left, "bottomRight", self.moveList, self.cutList)

        elif "king" in self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "tag"):
        
            self.king_cutList(top, left, "topLeft", self.moveList, self.cutList)
            self.king_cutList(top, left, "topRight", self.moveList, self.cutList)
            self.king_cutList(top, left, "bottomLeft", self.moveList, self.cutList)
            self.king_cutList(top, left, "bottomRight", self.moveList, self.cutList)
                
    def mouseClick(self, event):
        left, top  = self.mouseCalc(event.x, event.y)
        
        if top in self.canvas.data["Board"] and left in self.canvas.data["Board"][top] and self.turn == "player":
            if self.select != []:
                
                if [top, left] == self.select:
                    pass
                
                elif [top, left, "topLeft"] in self.cutList:
                    self.moveChecker(top, left, self.select[0], self.select[1])
                    if "man" in self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "tag"):
                        self.removeChecker(top, left, "topLeft", self.select[0], self.select[1])
                        if top == 5:
                            self.canvas.itemconfig(self.canvas.data["Checker"][top][left][0], tag='king', dash=(5, 1, 2, 1), dashoff=3, width=5)
                    elif "king" in self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "tag"):
                        self.removeChecker(top, left, "topLeft", self.select[0], self.select[1])

                    self.turn = "computer"
                elif [top, left, "topRight"] in self.cutList:
                    self.moveChecker(top, left, self.select[0], self.select[1])
                    if "man" in self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "tag"):
                        self.removeChecker(top, left, "topRight", self.select[0], self.select[1])
                        if top == 5:
                            self.canvas.itemconfig(self.canvas.data["Checker"][top][left][0], tag='king', dash=(5, 1, 2, 1), dashoff=3, width=5)
                    elif "king" in self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "tag"):
                        self.removeChecker(top, left, "topRight", self.select[0], self.select[1])

                    self.turn = "computer"
                elif [top, left, "bottomLeft"] in self.cutList:
                    self.moveChecker(top, left, self.select[0], self.select[1])
                    if "man" in self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "tag"):
                        self.removeChecker(top, left, "bottomLeft", self.select[0], self.select[1])
                    elif "king" in self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "tag"):
                        self.removeChecker(top, left, "bottomLeft", self.select[0], self.select[1])

                    self.turn = "computer"
                elif [top, left, "bottomRight"] in self.cutList:
                    self.moveChecker(top, left, self.select[0], self.select[1])
                    if "man" in self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "tag"):
                        self.removeChecker(top, left, "bottomRight", self.select[0], self.select[1])
                    elif "king" in self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "tag"):
                        self.removeChecker(top, left, "bottomRight", self.select[0], self.select[1])
                        
                    self.turn = "computer"
                elif self.cutList:
                    pass
                elif [top, left, "move"] in self.moveList:
                    self.moveChecker(top, left, self.select[0], self.select[1])
                    if "man" in self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "tag"):
                        if top == 5:
                            self.canvas.itemconfig(self.canvas.data["Checker"][top][left][0], tag='king', dash=(5, 1, 2, 1), dashoff=3, width=5)
                    self.turn = "computer"
                
                
                
                self.canvas.itemconfig(self.canvas.data["Board"][self.select[0]][self.select[1]][0], fill=self.boardColorMain)
                self.select = []
                
                self.cutList = []
                self.moveList = []

                
                if self.turn == "computer":
                    self.ai()
                
                for d_top, topRow in self.canvas.data["Checker"].iteritems():
                    for d_left, checker in topRow.iteritems():
                        
                        if self.canvas.itemcget(checker[0], "fill") == self.playerColor:
                            if "man" in self.canvas.itemcget(checker[0], "tag"):
                                self.man_cutList( d_top, d_left, "topLeft", self.moveList, self.cutList, False)
                                self.man_cutList( d_top, d_left, "topRight", self.moveList, self.cutList, False)
                                self.man_cutList( d_top, d_left, "bottomLeft", self.moveList, self.cutList, False)
                                self.man_cutList( d_top, d_left, "bottomRight", self.moveList, self.cutList, False)
                            elif "king" in self.canvas.itemcget(checker[0], "tag"):
                                self.king_cutList(d_top, d_left, "topLeft", self.moveList, self.cutList, False)
                                self.king_cutList(d_top, d_left, "topRight", self.moveList, self.cutList, False)
                                self.king_cutList(d_top, d_left, "bottomLeft", self.moveList, self.cutList, False)
                                self.king_cutList(d_top, d_left, "bottomRight", self.moveList, self.cutList, False)
                
            elif top in self.canvas.data["Checker"] and left in self.canvas.data["Checker"][top] and self.canvas.itemcget(self.canvas.data["Checker"][top][left][0], "fill") == self.playerColor:
                self.click_cutList(top, left)

    def mouseMoved(self, event):
        left, top  = self.mouseCalc(event.x, event.y)
        
        if left != self.left or top != self.top:
            
            if self.top in self.canvas.data["Board"] and self.left in self.canvas.data["Board"][self.top]:
                if self.canvas.itemcget(self.canvas.data["Board"][self.top][self.left][0], "fill") in ("#d80000", "#0c0cff"):
                    self.canvas.itemconfig(self.canvas.data["Board"][self.top][self.left][0], fill=self.color)

            if top in self.canvas.data["Board"] and left in self.canvas.data["Board"][top]:
                if self.canvas.itemcget(self.canvas.data["Board"][top][left][0], "fill") not in ("red", "blue"):
                    self.color = self.canvas.itemcget(self.canvas.data["Board"][top][left][0], "fill") 
                    self.canvas.itemconfig(self.canvas.data["Board"][top][left][0], fill='#d80000')
            
            self.left = left
            self.top = top

    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(root, width=565, height=410)

        self.canvas.pack()
        self.canvas.bind("<Motion>", self.mouseMoved)
        self.canvas.bind("<Button-1>", self.mouseClick)
        
        self.boardColorMain = "brown"
        self.boardColorSec = "white"
        
        self.canvas.data = { }
        self.canvas.data["Board"] = {}
        self.canvas.data["BoardVal"] = []

        self.canvas.data["Checker"] = {}
        self.canvas.data["CheckerVal"] = []
        
        self.turn = "player"
        
        self.left = 55
        self.top = 55
        
        self.select = []
        self.selectCut = []
        self.selectMove = []
        
        self.cutList = []
        self.moveList = []
        self.moveSupList = []
        
        self.playerColor = "black"
        self.computerColor = "white"
        
        self.color = self.boardColorMain
        
        curColor = self.boardColorMain
        curPos = 0
        
        for i in range(8):
            self.canvas.data["Board"][5+i*50] = {}
            if curColor == self.boardColorMain:
                curColor = self.boardColorSec
            else:
                curColor = self.boardColorMain
            for j in range(8):
                self.canvas.data["Board"][5+i*50][5+j*50] = [ self.canvas.create_rectangle( 5+ j*50, 5+ i*50, 5+ j*50 + 50, 5+ i*50 + 50, outline='black', fill=curColor) ]
                self.canvas.data["BoardVal"].append( [5+i*50, 5+j*50] )
                
                if curColor == self.boardColorMain:
                    curColor = self.boardColorSec
                else:
                    curColor = self.boardColorMain



        
        for i in range(0,3):
            self.canvas.data["Checker"][5+i*50] = {}

            if curPos == 0:
                curPos = 50
            else:
                curPos = 0
                
            for j in range(0,8,2):
                self.canvas.data["Checker"][5+i*50][5+j*50 +curPos ] = [ self.canvas.create_oval( 5+ j*50 +curPos , 5+ i*50, 5+ j*50 + 50 +curPos , 5+ i*50 + 50, outline='red', fill=self.computerColor, tag="man") ]
                self.canvas.data["CheckerVal"].append( [5+i*50, 5+j*50 +curPos ] )
        
        self.canvas.data["Checker"][5+3*50] = {}
        self.canvas.data["Checker"][5+4*50] = {}
        
        for i in range(5,8):
            self.canvas.data["Checker"][5+i*50] = {}
            
            if curPos == 0:
                curPos = 50
            else:
                curPos = 0
                
            for j in range(0,8,2):
                self.canvas.data["Checker"][5+i*50][5+j*50 +curPos ] = [ self.canvas.create_oval( 5+ j*50 +curPos , 5+ i*50, 5+ j*50 + 50 +curPos , 5+ i*50 + 50, outline='red', fill=self.playerColor, tag="man") ]
                self.canvas.data["CheckerVal"].append( [5+i*50, 5+j*50 +curPos ] )
                
        
if __name__ == "__main__":
    root = Tk()
    root.title("Checkers Tk")
    root.resizable(0,0)
    game = game_controller(root);
    root.mainloop()