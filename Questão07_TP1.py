#Prof. falou que não era para fazer esses exercícios. Eu fiz, mas o modifiquei pensando num tabuleiro. 

import turtle
    
def desenhar():
    for y in range(90, 361, 90):
        for x in range(-160,160,80):
            turtle.begin_fill()
            turtle.penup()
            turtle.goto(x,y)
            turtle.pendown()

            for k in range(4):
                turtle.forward(40)
                turtle.left(90)
            turtle.end_fill()  

    turtle.done()

desenhar()
