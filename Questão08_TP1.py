def verificar(a, b, c):
    # ver se é triângulo
    if (a < b + c) and (b < a + c) and (c < a + b):
        print("Pode formar um triângulo!")   
        # qual tipo de triângulo
        if a == b == c:
            print("Triângulo equilátero!")
        elif a != b != c != a:
            print("Triângulo escaleno!")
        else:
            print("Triângulo isósceles!")
    else:
        print("Não pode formar um triângulo!")  
        
  
a  =  float ( input ( "Digite o lado a: \ n " ))
b  =  float ( input ( "Digite o lado b: \ n " ))
c  =  float ( input ( "Digite o lado c: \ n " ))
verificar(a, b, c)
