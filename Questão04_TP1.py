def fatorial(numero):
    if numero < 0:
        return "Não foi possível calcular o fatorial. Número negativo."
    else:
        c = numero
        fat = 1
        while c > 0:
            print(c, end="")
            print(" x " if c > 1 else " = ", end="")
            fat *=c
            c -= 1
        return fat
    


numero = int(input("Fatorial de: ") )

print(f"Calculando o fatorial do número {numero}!:")
print(fatorial(numero))
