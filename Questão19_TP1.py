from turtle import*

def draw_square(square):
    shape("turtle")
    pencolor("red")
    speed(100)
    for square in range(0, square):
        fd(square)
        rt(90)


square = int(input('Digite um número (corresponde ao tamanho do quadrado): '))

draw_square(square)
