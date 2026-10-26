#codigo errado 

def dobro(x):
    resultado = x * 2
r = dobro(5)
print(r)

#codigo certo 

def dobro(x):
 resultado = x * 2
 return resultado

r = dobro(5)
print(r)

#Exemplo com a função
def exibir(mensagem="Olá!"):
    print(mensagem)

#1. Chamada que usa o valor padrão:
exibir()

#2. Chamada que não usa o valor padrão:
exibir ("Bom dia!")

def registrar(sensor, *leituras, **info):
    print(sensor, len(leituras), info)
 
registrar('T01', 25, 26, 27, local='Linha 1')




LIMITE = 70

def verificar(temp):
    excesso = temp - LIMITE
    return excesso

print(verificar(75))