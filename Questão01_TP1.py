def line():
    print("=" * 40)
    

def hello():
    line()
    print("Olá, seja bem-vindo ao programa que soma os números ímpares em um intervalo proposto.")

def sum():
    line()
    num = int(input("Digite um número: "))
    s = 0
    for a in range(1, num, 2):
        if a % 2 != 0:
            s += a
    print("A soma dos números ímpares entre 1 e", num+1, "é", s)
    
hello()
sum()
line()
print('FIM')
line()
