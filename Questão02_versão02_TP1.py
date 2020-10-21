
def lin():
    print("\033[1;32m==\033[0;0m" * 30)


def idade(ano, mes, dia):
    from datetime import date
    atual_ano = date.today().year
    atual_mes = date.today().month
    atual_dia = date.today().day
    idade = atual_ano - ano
    if idade < 0:
        return f"\033[1;31mValor inválido. Reinicie o programa e tente novamente.\033[0;0m"
    else:
        if mes <= atual_mes:
           lin()
           print(f"Você possui {idade} ano(s), {abs(atual_mes - mes)} mes(es) e {abs(atual_dia - dia)} dia(s).")
           lin()
           
           idade_dias = (idade * 365) + (mes * 30) + dia
           return f"\033[1;34mSua idade em dias é {idade_dias}.\033[0;0m"
           lin()
        
        else:
           lin()
           print(f"Você possui {idade - 1} ano(s), {abs(atual_mes)} mes(es) e {abs(atual_dia - dia)} dia(s).")
           lin()
           
           idade_dias = (idade * 365) + (mes * 30) + dia
           return f"\033[1;34mSua idade em dias é {idade_dias}.\033[0;0m"
           lin()
            


ano = int(input("Em que ano você nasceu? "))
mes = int(input("Em que mês você nasceu? "))
dia = int(input("Em qual dia você nasceu? "))

lin()
print(idade(ano, mes, dia))
