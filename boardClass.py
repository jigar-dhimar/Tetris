from shapeClass import*

class Board():


    def __init__(self, win, width, height):
        """the instance variables are:
        win: where the board will be drawn 
        width: width of the board, integer
        height: height of the board, integer"""

        #instance variables
        self.width = width
        self.height = height
        self.canvas = win
        self.canvas.setBackground('light gray')


        #dictionary to hold location of blocks
        self.grid = {}


    def drawShape(self, shape):

        """draws shapes onto board"""

        #if the space is open 
        if shape.canMove(self, 0, 0):

            #shape drawn 
            shape.draw(self.canvas)

            #yes shape can be drawn 
            return True

        #shape cannot be drawn return false 
        return False


    def canMove(self, x,y):

        """checks if it is okay to move to square x,y"""

        #checks dictionary for (x,y)
        if x in range(10):
            if y in range(20):
                if (x,y) not in self.grid:
                    #position not in dictionary
                    #returns true okay to move
                    return True
        #is in dictionary cannot move 
        return False

    def addShape(self, shape):

        """adds the location of 
        each block to the dictionary"""

        Blist = shape.getBlocks()

        #goes through each block 
        #in the piece
        for block in Blist:

            #adds location to dictionary
            x = block.x
            y = block.y
            self.grid[x,y] = block

    def deleteRow(self, y):
        """removes all blocks in row y"""

        #goes through each column in 
        #given row and deletes blocks
        #and the location from the dictionary
        for x in range(self.width):
            block = self.grid[x,y]
            del self.grid[x,y]
            block.undraw()


    def isRowComplete(self,y):

        """checks each row to see if it is complete"""

        #goes through each x value in row
        for x in range(self.width):

            #if block is not at location 
            #the row is not filled
            if (x,y) not in self.grid:
                return False
        
        #all x locations in a given row
        #have blocks which means the row 
        #is complete
        return True

    def moveDownRows(self,yStartRow):

        """shifts down remaining rows"""
       
        #goes through each block in row 
        for x in range(10):
           
            #goes through each row from bottom 
            for y in reversed(range(yStartRow+1)):
                
                #if there is a block at (x,y)
                if (x,y) in self.grid:

                    #temp variable to hold block object
                    block = self.grid[x,y]

                    #del block from grid
                    del self.grid[x,y]

                    #move block down on screen 
                    block.move(0,1)

                    #add block to grid with updated position 
                    self.grid[x,y+1] = block
                   


    def removeCompleteRows(self):

        """checks entire grid for completed rows"""

        #goes through each row in game window
        for i in range(self.height):

            #checks if row is complete
            if self.isRowComplete(i) == True:

                #deletes row 
                self.deleteRow(i)

                #shifts down the remaining rows
                self.moveDownRows(i-1)

    def gameover(self):
        
        # draw white oval so can read text
        oval = Oval(Point(0,1.2*20/2*30), Point(10*(30),.8*20/2*30))
        oval.setFill('white')
        oval.draw(self.canvas)

        # draw text displaying 'Game Over!!!'
        text = Text(Point(10/2*(30),20/2*30),'Game Over!')
        text.setSize(22)
        text.setStyle('bold')
        text.draw(self.canvas)
