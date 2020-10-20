import math
import turtle


def verificar(a, b, c):
    # ver se é triângulo
    if (a < b + c) and (b < a + c) and (c < a + b):
        print("Pode formar um triângulo!")   
        
        # qual tipo de triângulo
        if a == b == c:
            print("Triângulo equilátero!")
        elif a != b != c != a:
            print("Triângulo escanelo!")
        else:
            print("Triângulo isósceles!")
    else:
        print("Não pode formar um triângulo!")  
        

def q(numero):
    return (numero*numero)
    

def desenhar_triangulo(a, b, c):
    #calcula angulo
    
    p = 3.1415
    angulo_c = math.acos((q(a) +q(b) -q(c)) / (2*a*b))
    angulo_a = math.acos(q(b) +q(c) -q(a)) / (2*b*c))
    angulo_b = p - angulo_a - angulo_c 
    
    angulo_c = 180 - (180 / p * angulo_c)
    angulo_a = 180 - (180 / p * angulo_a)
    angulo_b = 180 - (180 / p * angulo_b)

    #desenha triângulo
    turtle.showturtle()
    turtle.penup()
    turtle.setpos(-50,0)
    turtle.pencolor("hotpink")
    turtle.pendown()
    turtle.forward(a)
    turtle.left(angulo_c)
    turtle.pencolor("yellow")
    turtle.forward(b)
    turtle.left(angulo_a)
    turtle.pencolor("blue")
    turtle.forward(c)

  
a = float(input("Digite o lado a: \n"))
b = float(input("Digite o lado b: \n"))
c = float(input("Digite o lado c: \n"))

verificar(a, b, c)
desenhar_triangulo(a, b, c)
