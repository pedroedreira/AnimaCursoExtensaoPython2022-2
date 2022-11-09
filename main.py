print("Início da Aula 3 (09/11/2023)")

contador = 1

# Exibir de 1 até 10 repetidamente
while(contador <= 10):
  print(contador)
  contador = contador+1 #contador += 1


# Laço for (python for = for each)
fruta = "morango"
print(fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "manga"

#Lista
frutas = ["morango", "laranja", "manga"]

#Mostrar todas
print(frutas)

#Quero exibir apenas a 3a fruta (manga)
print(frutas[2])

#Exibir quantas frutas tem na lsita
print(len(frutas)) #length = tamanho

#Incluir uma fruta
frutas.append("pêra")

print(len(frutas)) #length = tamanho

print("Exemplos das frutas com While...")
frutas.append("uva")

i=0
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

print("Exemplo das frutas com FOR")
for fruta in frutas:
  print(fruta)