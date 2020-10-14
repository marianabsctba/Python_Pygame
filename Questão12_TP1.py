import turtle

def circulo():
    n = float(input("Qual o tamanho do raio do círculo? "))
    turtle.circle(n)
    turtle.setheading(90)
    turtle.forward(n)

circulo()
