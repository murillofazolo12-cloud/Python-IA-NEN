#Entrada de dados
nota = float(input("digite a sua nota (0 a 10)"))

if nota >= 6.0: 
    print("parabens, você foi aprovado!")
elif(nota >= 5.0 and nota < 6.0):
    print(" você ficou de recuperação , tente  novamente!")
else: 
    print("você está reprovado!")
