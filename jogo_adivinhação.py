import random 

numero_secreto = random.randint(1,100)
palpite = int(input("adivinhe o numero de 1 a 100 (apenas uma chance)"))


if palpite == numero_secreto:
     print("você acertou")
else:
    print(f"errou! o numero era {numero_secreto}")
