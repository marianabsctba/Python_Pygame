
def triangulos(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        print("Não pode formar um triângulo!")
    else:
        print("Pode formar um triângulo!")
        if a == b and b == c:
            print("Triângulo equilátero!")
        elif a == b or b==c or a == b:
            print(" Triângulo isósceles!")
        else:
            print("Triângulo escaleno!")
            
    
a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))

triangulos(a, b, c)
