def imc (peso, altura):
    return peso / altura ** 2 
    

altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))
resultado = imc(peso, altura)

print (resultado)
if resultado < 16 :
    print ("Magreza grau III")

elif resultado < 16.9 :
    print ("Magreza grau II")

elif resultado < 18.4 :
    print ("Magreza grau I")

elif resultado < 24.9 :
    print ("Eutrofia ")

elif resultado < 29.9 :
    print ("Pré-obesidade")

elif resultado < 34.9 :
    print ('Obesidade moderada (grau I)')

elif resultado < 39.9 :
    print ('Obesidade severa (grau II)')

else :
    print ('Obesidade muito severa (grau III)')
