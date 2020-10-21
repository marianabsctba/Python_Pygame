def verificar(a, b, c):
    #tupla
    t = (a, b, c)
    # ver se é triângulo
    if t[0] + t[1] > t[2] and t[1] + t[2] > t[0] and t[0] + t[2] > t[1]:
        print("Pode formar um triângulo!")   
        # qual tipo de triângulo
        if t[0] == t[1] == t[2]:
            print("Triângulo equilátero!")
        elif t[0] != t[1] != t[2] != t[0]:
            print("Triângulo escaleno!")
        else:
            print("Triângulo isósceles!")
    else:
        print("Não pode formar um triângulo!")  

  
a  =  float (input("Digite o lado a: " ))
b  =  float (input("Digite o lado b: " ))
c  =  float (input("Digite o lado c: " ))

verificar(a, b, c)
