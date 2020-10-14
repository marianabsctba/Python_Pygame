import turtle
import math

def poligono(turtle, n, r):
    poligono1(turtle, n, r)
    turtle.pu()
    turtle.fd(r*2 + 10)
    turtle.pd()
    
def poligono1(turtle, n, r):
    ang = 360.0 / n
    for i in range(n):
        poligono2(turtle, r, ang/2)
        turtle.lt(ang)

def poligono2(turtle, r, ang):
    y = r * math.sin(ang * math.pi / 180)

    turtle.rt(ang)
    turtle.fd(r)
    turtle.lt(90+ang)
    turtle.fd(2*y)
    turtle.lt(90+ang)
    turtle.fd(r)
    turtle.lt(180-ang)

bob = turtle.Turtle()

bob.pu()
bob.bk(130)
bob.pd()

size = int(input("Digite o tamanho das arestas do polígono: "))
quant = int(input("Digite o número de segmentos: "))
    
poligono(bob, quant, size)
