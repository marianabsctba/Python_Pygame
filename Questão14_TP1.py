import turtle
turtle.title("Utilizando nossas Funções!")

def quadrado():
    turtle.setheading(0)
    for i in range(1,5):
        turtle.forward(100)
        turtle.setheading(90*i)

def triangulo():
    turtle.setheading(0)
    for i in range(1,4):
        turtle.forward(100)
        turtle.setheading(120*i)

def circulo():
    turtle.setheading(0)
    turtle.circle(100)

def cima():
  turtle.setheading(90)
  turtle.forward(50)

def baixo():
  turtle.setheading(270)
  turtle.forward(50)

def esquerda():
  turtle.setheading(180)
  turtle.forward(50)

def direita():
  turtle.setheading(0)
  turtle.forward(50)


turtle.listen()

turtle.onkey(cima, 'Up')
turtle.onkey(baixo, 'Down')
turtle.onkey(esquerda, 'Left')
turtle.onkey(direita, 'Right')
turtle.onkey(quadrado, 'q')
turtle.onkey(triangulo, 't')
turtle.onkey(circulo, 'c')
