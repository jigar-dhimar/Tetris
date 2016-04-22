from boardClass import*
from random import*


shapeList = [IShape, JShape, OShape, SShape, TShape, ZShape]
direction = {"Left": (-1,0), "Right":(1,0), "Down":(0,1)}
class Tetris():


    def __init__(self, win):
        """The instance variables are:
        win: window to where the game will
        be drawn onto"""

        #other variables 
        self.boardWidth = 10 
        self.boardHeight = 20
        self.win = win

        #event binding 
        self.win.bind_all('<Key>', self.keyPressed)
        self.board = Board(win, self.boardWidth, self.boardHeight)
        


        #delay time before the shape moves
        #down a set amount down 
        self.delay = 1000 #in milliseconds 
        

        #make new shape 
        self.currentShape = self.createShape()
        

        #draw the shape to the screen 
        self.board.drawShape(self.currentShape)

        #animate the shape
        self.constantMoveShape()

    def createShape(self):
        """creates new shape onto screen"""

        #new shape selected using rand
        #after getting number it picks 
        #the corresponding shape from the list 
        #containing the names of all the shapes
        randInt = int(random()*5)
        

        #x and y coordinates 
        y=0
        x=int(self.boardWidth/2)

        #new shape at position x,y
        shape = shapeList[randInt](Point(x,y))
        return shape

        

    def constantMoveShape(self):

        """moves shape down"""

        #shape will move down a 
        #certain amount every set time interval
        self.move("Down")
        self.win.after(self.delay, self.constantMoveShape)

    def move(self, directionP):
    
        """moves direction down, left, right"""

        (dx,dy) = direction[directionP]
        
        #shape can be moved down 
        if self.currentShape.canMove(self.board, dx,dy):
            self.currentShape.move(dx,dy)
            return True
        else:
            if directionP == "Down":

                #shape is in final position 
                #add blocks to grid
                
                self.board.addShape(self.currentShape)

                #remove complete rows
                self.board.removeCompleteRows()

                #make new shape
                self.currentShape = self.createShape()
                

                #draw new shape
                ret = self.board.drawShape(self.currentShape)
                if ret == False:
                    self.board.gameover()
            return False 

    
    def rotate(self):

        """rotates shape on screen"""

        #checks if shape can rotate 
        if self.currentShape.canRotate(self.board) == True:

            #rotate shape 
            self.currentShape.rotate(self.board)

    def keyPressed(self, event):
        key = event.keysym 

        #checks if key pressed 
        #is in list of keys
        if key in direction:

            #key pressed is in list
            #calls helper method to 
            #perform corresponding action 
            self.move(key)

        #if the space key is pressed
        elif key == "space":
            
            #amount to move
            dx = 0
            dy = 1

            #shape will move down until it cannot 
            #move any further down or hits another block 
            while self.currentShape.canMove(self.board, dx, dy): 
                self.currentShape.move(dx, dy)

            #calls helper to make new shape
            #add current shape to grid 
            self.move("Down")
        
        #if up key is pressed 
        elif key == "Up":

            #piece should rotate if it can 
            self.rotate()
        
