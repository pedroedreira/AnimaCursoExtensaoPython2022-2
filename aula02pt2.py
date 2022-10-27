#------------------------#
#Aula02 pt 2

#Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, mostra "Você é bichão, mesmo..."

nome = input("Digite seu nome: ")
nota = float(input("Digite sua nota: "))

print(f"Olá {nome}, sua nota é {nota}.")

if (nota == 10):
  print("Parabéns, você é um ótimo aluno")
elif (nota >= 6 and nota < 10):
  print("Você não tirou a nota máxima, porém atingiu a média")
else:
  print("Você não atingiu a média")
  