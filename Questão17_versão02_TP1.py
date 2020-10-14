def rotacionar_string():
    word = input('Digite uma palavra: ')
    x = int(input('Digite um número inteiro: '))
    try:
        if len(word) > x:
            new_word = word[x:] + word[:x]
            print(new_word)
    except:
        print('Número inválido.Programa reiniciado.')
    exit()


rotacionar_string()
