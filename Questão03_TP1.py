def fatorial(num, show=False):
    if num < 0:
        return "Não foi possível calcular o fatorial. Número negativo."
    else:
        fat = 1
        for c in range(numero, 0, -1):
            if show:
                print(c, end="")
                if c > 1:
                    print(" x ", end="")
                else:
                    print(" = ", end="")
            fat *= c
        return fat
            
        
num = int(input("Fatorial de: "))
print(fatorial(numero, show=True))
