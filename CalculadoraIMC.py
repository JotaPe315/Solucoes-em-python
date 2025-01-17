p = float(input("Digite o seu peso em kg "))
a = float(input("Digite a sua altura em metros "))

imc = p/(a**2)

if imc <= 18.5 :
    print("O seu IMC é" , imc,", classificado como Abaixo do normal\n")
elif imc >= 18.6 and imc <=24.9 :
    print("O seu IMC é" , imc,", classificado como Peso normal\n")
elif imc >= 25 and imc <=29.9 :
    print("O seu IMC é" , imc,", classificado como Sobrepeso\n")
elif imc >= 30 and imc <=34.9 :
    print("O seu IMC é" , imc,", classificado como Obesidade grau I\n")
elif imc >= 35 and imc <= 39.9 :
    print("O seu IMC é" , imc,", classificado como Obesidade grau II\n")
else :
    print("O seu IMC é" , imc,", classificado como Obesidade grau III\n")

print("Classificação do IMC:\n 18,5 ou menos: Abaixo do normal\n Entre 18,6 e 24,9 Normal\n Entre 25,0 e 29,9 Sobrepeso\n Entre 30,0 e 34,9 Obesidade grau I\n Entre 35,0 e 39,9 Obesidade grau II\n Acima de 40,0 Obesidade grau III")