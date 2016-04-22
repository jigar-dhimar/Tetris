from tetrisClass import*
from graphics import*
from buttonclass import*



def splashscreen():

    win = GraphWin("", 400, 400)
    win.setBackground("blanchedalmond")

    tetrisCon = Text(Point(200,80), "Tetris Controls")
    tetrisCon.setSize(23)
    tetrisCon.draw(win)


    #game control list 
    contList = ["Up: rotates current piece", 
                "Down: moves piece down",
                "Left: moves piece to the left", 
                "Right: moves piece to the right",
                "Space: drops piece down"]



    #draws explanation for game controls onto screen             
    inc = 0
    for control in contList:
        con = Text(Point(200, 120+30*inc), control)
        con.setSize(20)
        inc = inc + 1
        con.draw(win)

    #continue button 
    continueButton = Button(win, Point(320,320), 70,50,"Continue", "seagreen")
    continueButton.activate()


    #program will not continue until 
    #the button is clicked 
    pt = win.getMouse()
    while continueButton.clicked(pt) != True:
        pt = win.getMouse()
    win.close()

def main():

    splashscreen()
    win = GraphWin("Tetris", 10*30, 20*30)
    game = Tetris(win)
    win.mainloop()

if __name__ == '__main__':
    main()