def girar(string_usuario, girar):     
    for letra in range(0,x):
        string_usuario = string_usuario[-1] + string_usuario[:len(string_usuario)-1]
        print(string_usuario[-1] + string_usuario[:len(string_usuario)-1])


string_usuario = input("Digite uma palavra: ")
x = int(input("Quantas vezes você quer girar a palavra selecionada? "))    
       
girar(string_usuario, girar)
