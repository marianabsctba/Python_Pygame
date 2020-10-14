def verificar_tupla():
    letra = input("Digite uma letra: ").strip().lower()
    tupla = ("a", "b", "c", "e")
    if letra in tupla:
        print("O elemento está na tupla!")
        print(f"O índice do elemento na tupla é {tupla.index(letra)}")
    else:
        print("Desculpe, o elemento não está na lista.")
        
verificar_tupla()
