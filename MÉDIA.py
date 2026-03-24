from math import ceil

while True:
    
    n1 = float(input("Digite a primeira nota do aluno: "))
    if 0 <= n1 <= 10:
        break
    else:
        print("Nota inválida. Adicione uma nota acima de 0 e maior que 10")

while True:
    
    n2 = float(input("Digite a segunda nota do aluno: "))
    if 0 <= n2 <= 10:
        break
    else:
        print("Nota inválida. Adicione uma nota acima de 0 e maior que 10")

while True:
    
    n3 = float(input("Digite a terceira nota do aluno: "))
    if 0 <= n3 <= 10:
        break
    else:
        print("Nota inválida. Adicione uma nota acima de 0 e maior que 10")


m = (n1+n2+n3)/3
média = round(m, 2)

if média < 6:
    print (f"A média do aluno é: {média:.2f}\nO aluno reprovou :(")

else:
    print (f"A média do aluno é {média:.2f} \nO aluno esta aprovado :)")    
