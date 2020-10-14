def soma():
    num = int(input("Digite um número: "))
    s = 0
    for a in range(1, num, 2):
        if a % 2 != 0:
            s += a
    print("A soma dos números ímpares entre 1 e", num, "é", s)
    print('FIM')


soma()
