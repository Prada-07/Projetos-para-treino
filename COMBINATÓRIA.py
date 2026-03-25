import sys

while True:
    try:
        a = float(input("Digite o valor da variável A: "))
        break
    except ValueError:
        print("Valor inválido. Por favor, digite um número real para a variável A.")   
while True:
    try:
        b = float(input("Digite o valor da variável B: "))
        break
    except ValueError:
        print("Valor inválido. Por favor, digite um número real para a variável B.")        
while True:
    try:
        c = float(input("Digite o valor da variável C: "))
        break
    except ValueError:
        print("Valor inválido. Por favor, digite um número real para a variável C.")
while True:
    try:
        d = float(input("Digite o valor da variável D: "))
        break
    except ValueError:
        print("Valor inválido. Por favor, digite um número real para a variável D.")

while True:
    operação = str(input("Deseja ver as adições, subtrações, multiplicações, divisões ou todas? (A/S/M/D/T): ")).upper()
    if operação in ["A", "S", "M", "D", "T"]:
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (A/S/M/D/T).")

letra_1 = str(input("Deseja ver as combinações com quais variáveis? (A/B/C/D): ")).strip().upper()
while True:
        if letra_1 == "A":
             valor_1 = a
             break
        elif letra_1 == "B":
             valor_1 = b
             break
        elif letra_1 == "C":
                valor_1 = c
                break
        elif letra_1 == "D":
              valor_1 = d
              break
        else:
              print("Opção inválida. Por favor, escolha uma variável válida (A/B/C/D).")
while True:
    letra_2 = input("Escolha outra variável diferente da primeira (A/B/C/D): ").strip().upper()
    if letra_2 == letra_1:
        print("Erro: escolha uma variável diferente de", letra_1)
        continue
    if letra_2 not in ["A", "B", "C", "D"]:
        print("Opção inválida. Digite A, B, C ou D.")
        continue
    if letra_2 == "A":
        valor_2 = a
        break
    elif letra_2 == "B":
        valor_2 = b
        break
    elif letra_2 == "C":
        valor_2 = c
        break
    elif letra_2 == "D":
        valor_2 = d
        break
         
if operação == "A":
    print (f"Adição \n{valor_1} + {valor_2} = {valor_1 + valor_2}")   
elif operação == "S":
    print (f"Subtração \n{valor_1} - {valor_2} = {valor_1 - valor_2}")
elif operação == "M":
    print (f"Multiplicação \n{valor_1} * {valor_2} = {valor_1 * valor_2}")
elif operação == "D":
    print (f"Divisão \n{valor_1} / {valor_2} = {valor_1 / valor_2}")
elif operação == "T":
    print (f"Adição \n{valor_1} + {valor_2} = {valor_1 + valor_2}")
    print (f"Subtração \n{valor_1} - {valor_2} = {valor_1 - valor_2}")
    print (f"Multiplicação \n{valor_1} * {valor_2} = {valor_1 * valor_2}")
    print (f"Divisão \n{valor_1} / {valor_2} = {valor_1 / valor_2}")
    
sys.exit()    
