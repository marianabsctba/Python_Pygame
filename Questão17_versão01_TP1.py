def rotacionar_string(word, x):
    if len(word) > x:
        new_word = word[x:] + word[:x]
        print(new_word)
    else:
        print('Número inválido.Programa reiniciado.')
        exit()

        
word = input('Digite uma palavra: ')
x = int(input('Digite um número inteiro: '))

rotacionar_string(word, x)
