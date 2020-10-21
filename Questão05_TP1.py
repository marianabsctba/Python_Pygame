def linha():
    print("=" * 40)

def verificar_tupla(tupla):
    linha()
    print("Verifique se uma letra está na tupla...")
    letra = input("Digite uma letra: ").strip().lower()
    if letra in tupla:
        print("O elemento está na tupla!")
        print(f"O índice do elemento na tupla é {tupla.index(letra)}")
    else:
        print("Desculpe, o elemento não está na lista.")
        
          
def dividir_tupla(tupla):
    linha()
    print("Veja a tupla dividida por 2...")
    dividir = len(tupla) // 2
    print(tupla[:dividir], tupla[dividir:])

    
        
def eliminar_elemento(tupla):
    linha()
    letra_2= input("Digite uma letra (de 'a' a 'f'), para eliminar da tupla: ").strip().lower()
    l = tupla.index(letra_2)
    print(tupla[:l] + tupla[l + 1:])
        


def inverter_elementos(tupla):
    linha()
    print("Veja agora a tupla invertida...")
    print(tupla[::-1])
    linha()


tupla = ("a", "b", "c", "d", "e", "f")

verificar_tupla(tupla)
dividir_tupla(tupla)
eliminar_elemento(tupla)
inverter_elementos(tupla)
