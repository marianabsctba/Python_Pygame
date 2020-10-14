import turtle

def quadrado():
    print("Vamos desenhar um quadrado?")
    n = float(input("Qual é o comprimento do lado do quadrado: "))
    
    for lado in range(1,5):
        turtle.forward(n)
        turtle.setheading(90 * lado)

quadrado()
