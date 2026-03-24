# Projetos-para-treino
a = float(input("Digite o valor da variável A: "))
b = float(input("Digite o valor da variável B: "))    
c = float(input("Digite o valor da variável C: "))
d = float(input("Digite o valor da variável D: "))

operação = str(input("Deseja ver as adições, subtrações, multiplicações, divisões ou todas? (A/S/M/D/T): ")).upper()
letra_1 = str(input("Deseja ver as combinações com quais variáveis? (A/B/C/D): ")).upper()
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
              
letra_2 = str(input("Deseja ver as combinações com quais variáveis? (A/B/C/D): ")).upper()
while True:
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
        else:
              print("Opção inválida. Por favor, escolha uma variável válida (A/B/C/D).")
while True:
   if letra_1 == letra_2:
       print("As variáveis devem ser diferentes. Por favor, escolha variáveis diferentes.")
   else:
         break
     
if operação == "A":
    print("Adição:")
    print (f"{valor_1} + {valor_2} = {valor_1 + valor_2}")   
elif operação == "S":
    print("Subtração:")
    print (f"{valor_1} - {valor_2} = {valor_1 - valor_2}")
elif operação == "M":
    print("Multiplicação:")
    print (f"{valor_1} * {valor_2} = {valor_1 * valor_2}")
elif operação == "D":
    print("Divisão:")
    print (f"{valor_1} / {valor_2} = {valor_1 / valor_2}")
elif operação == "T":
    print("Adição:")
    print (f"{valor_1} + {valor_2} = {valor_1 + valor_2}")
    print("Subtração:")
    print (f"{valor_1} - {valor_2} = {valor_1 - valor_2}")
    print("Multiplicação:")
    print (f"{valor_1} * {valor_2} = {valor_1 * valor_2}")
    print("Divisão:")
    print (f"{valor_1} / {valor_2} = {valor_1 / valor_2}")
