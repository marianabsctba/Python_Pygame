from turtle import *

def draw(line, ang):
    shape("turtle")
    pencolor("blue")
    speed(100)
    for line in range(1, line):
        fd(line)
        right(90 + ang)

line = int(input("Digite um número que corresponda ao tamanho do desenho: "))
ang = int(input("Digite um número correspondente ao ângulo do desenho: "))

draw(line, ang)
