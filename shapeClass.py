from blockClass import*

class Shape():

    """ base class for all tetris shapes"""


    def __init__(self, coords, color):

        """the instance variables are:
        coords: a list for each of the blocks 
        in a given tetris piece

        color: color of the piece"""

        #list to hold each of the blocks 
        #in the piece
        self.blocks = []

        #rotation direction is set to the right
        #by default can be changed for individual pieces
        self.rotationDirection = 1

        self.shiftRotationDirection = False

        #adds each block in the piece to the list
        for pos in coords:
            self.blocks.append(Block(pos, color))


    def getBlocks(self):

        """returns the list of blocks
        for a given piece """
        return self.blocks


    def draw(self, win):

        """draws each block to the screen"""

        #for loop goes through 
        #block list and draw each individual block 
        for i in range(len(self.blocks)):
            self.blocks[i].draw(win)


    def move(self, xMove, Ymove):

        """Moves the block by the inputted amounts
        in the x and y directions"""

        #goes through block list and moves
        #each of the individual blocks 
        for i in range(len(self.blocks)):
            self.blocks[i].move(xMove, Ymove)


    def canMove(self, board, dx,dy):

        """checks if the shape can move in the
        given direction"""
        
        #if any of the individual blocks 
        #in the piece cannot move than 
        #the function returns false 
        for i in range(len(self.blocks)):
            if self.blocks[i].canMove(board,dx,dy) == False:
                return False

        #none of the individual blocks 
        #returned false, so it is okay to move
        return True



    def getRotationDirection(self):
        """returns the current direction of rotation"""
        return self.rotationDirection


    def canRotate(self, board):
        """checks if the piece can rotate on the board"""
        
        #gets the direction the piece will rotate 
        rotationDir = self.getRotationDirection()
        
        #center block that does not move
        center = self.centerBlock

        #list to hold how much 
        #each block will move 
        #in the x and y direction
        self.dx = []
        self.dy = []

        #goes through each block in piece 
        for block in self.blocks:
           

            #calculates how far the 
            #piece is away from the center
            x = block.x - center.x
            y = block.y - center.y


            #rotates the block by 
            #flipping the x and y 
            #coordinates
            x2 = - rotationDir * y
            y2 = rotationDir * x
            
            #calculates how far
            #each block moved from 
            #its original position 
            dx = x2-x
            dy = y2-y
            
            self.dx.append(dx)
            self.dy.append(dy)
            
            #if an individual block cannot 
            #be moved without conflict 
            #the function returns false 
            #which means the piece as a 
            #whole cannot rotate 
            if not block.canMove(board,dx,dy):
                return False
       
        #all blocks can move
        #thus the piece can move
        return True

     
    def rotate(self, board):
        """rotates the piece on the board"""

        #gets rotation direction 
        rotationDir = self.getRotationDirection()
        
        #gets the center piece 
        #which does not move 
        center = self.centerBlock


        k = 0

        #goes through each block in piece
        for block in self.blocks:

            #moves each individual piece 
            block.move(self.dx[k], self.dy[k])
            k += 1

        
        #if the piece is able to rotate
        #which is determined by a 
        #boolean instance variable 
        #(True= can rotate, false= cannot rotate)
        if self.shiftRotationDirection:

            #changes rotation direction by 
            #multiplying by negative one 
            #so next time it rotates the 
            #opposite direction 
            self.rotationDirection *= -1


########################## Tetris Pieces ###################################

class IShape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 2, center.y),
                  Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, 'blue')
        self.shiftRotationDirection = True
        self.centerBlock = self.blocks[2]

class JShape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y),
                  Point(center.x + 1, center.y + 1)]
        Shape.__init__(self, coords, 'orange')        
        self.centerBlock = self.blocks[1]

class LShape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y),
                  Point(center.x - 1, center.y + 1)]
        Shape.__init__(self, coords, 'cyan')        
        self.centerBlock = self.blocks[1]


class OShape(Shape):
    def __init__(self, center):
        coords = [Point(center.x    , center.y),
                  Point(center.x - 1, center.y),
                  Point(center.x   , center.y + 1),
                  Point(center.x - 1, center.y + 1)]
        Shape.__init__(self, coords, 'red')
        self.centerBlock = self.blocks[0]

    def rotate(self, board):
        # Override Shape's rotate method since _Shape does not rotate
        return 

class SShape(Shape):
    def __init__(self, center):
        coords = [Point(center.x    , center.y),
                  Point(center.x    , center.y + 1),
                  Point(center.x + 1, center.y),
                  Point(center.x - 1, center.y + 1)]
        Shape.__init__(self, coords, 'green')
        self.centerBlock = self.blocks[0]
        self.shiftRotationDirection = True
        self.rotationDirection = -1


class TShape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y),
                  Point(center.x    , center.y + 1)]
        Shape.__init__(self, coords, 'yellow')
        self.centerBlock = self.blocks[1]


class ZShape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y), 
                  Point(center.x    , center.y + 1),
                  Point(center.x + 1, center.y + 1)]
        Shape.__init__(self, coords, 'magenta')
        self.centerBlock = self.blocks[1]
        self.shiftRotationDirection = True
        self.rotationDirection = -1      