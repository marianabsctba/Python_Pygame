import turtle

def quadrado():
    n = float(input("Qual o comprimento do quadrado? "))
    sub_q = int(input("Quantos quadrados serão desenhados dentro do quadrado? "))
    
    for x in range(0, sub_q):
        for i in range(1,5):
            turtle.forward(n)
            turtle.setheading(90 * i)
        
        turtle.penup()
        turtle.forward(0.2 * n)
        turtle.setheading(90)
        turtle.forward(0.2 * n)
        turtle.pendown()
        n = 0.5 * n
        turtle.setheading(0)

quadrado()
