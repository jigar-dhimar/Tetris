from graphics import*


BLOCK_SIZE = 30
OUTLINE_WIDTH = 3

class Block(Rectangle):

    def __init__(self, pos, color):

        """The instance variables are:
        pos: a tuple that hold the position 
        color: the color of the block, held by a string"""
        
        self.x = pos.getX()
        self.y = pos.getY()
    

        #find the coordinates of the block as bigger tetris 
        #block on screen 
        p1 = Point(pos.x*30 + OUTLINE_WIDTH, pos.y*30 + OUTLINE_WIDTH)  
        p2 = Point(p1.x + 30, p1.y + 30)

        #creates block 
        Rectangle.__init__(self, p1, p2)
        self.setWidth(OUTLINE_WIDTH)
        self.setFill(color)


    def canMove(self, board, x=0, y=0):

            """checks if block can move
            x and y increments in respective directions
            """

            #finds new coordinates 
            self.newX = self.x + x
            self.newY = self.y + y

            return board.canMove(self.newX,self.newY)
    

    def move(self, x=0,y=0):
            """moves the block x and y squares"""

            self.x += x
            self.y += y  

            Rectangle.move(self, x*30, y*30)
