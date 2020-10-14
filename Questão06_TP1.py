import turtle

def graus():
    g = 0
    tartaruga = turtle.Turtle()
    tartaruga.shape("turtle")
    tartaruga.fillcolor("pink")
    tartaruga.pensize(5)
    
    while g < 360:
        tartaruga.forward(300)
        tartaruga.setheading(180 + g)
        tartaruga.write(str(g) + "°")
        tartaruga.forward(300)
        g = g + 15
        tartaruga.setheading(g)
    
print(graus())
