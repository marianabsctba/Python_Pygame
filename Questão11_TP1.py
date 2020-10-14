import turtle

def triangulo():
    n = float(input("Qual é o comprimento do lado do triângulo? "))
    for lado in range(1,4):
        turtle.forward(n)
        turtle.setheading(120 * lado)

triangulo()
