#------------------------

#Aula02 pt 1

# comando input(): permitir que o user digite algo
# e Variáveis
nome = input("Digite seu nome: ")
idade = int(input("Qual a sua idade? ")) #int no início para deixar número inteiro
genero = input("Informe seu gênero M=Masculino, F=Feminino, 0=outros): ")

dobro = idade * 2

# comando de saída...exibir na tela
#print(nome)
#print(f"Boa noite, seu nome é {nome}")

#Fixação - Input de Nome e Idade + saída de frase
#Fixção - Se eu quisesse mostrar o DOBRO da idade informada?
print(f"O seu nome é {nome} e sua idade é {idade} anos. O dobro da sua idade é: {dobro} ")

# Estrutura condicional - if-else (SE-SE NÃO)
if (idade >= 18):
  print("Você é maior de idade, ótimo!")
else:
  print("Você não é maior de idade ainda")

#E se eu quisessem perguntar o gênero (M = Masculino e F = Feminino)
#Mostre (...e você também precisa/precisou prestar o serviço militar obrigatório)

if idade >= 18 and genero == "M":
  print("E você deveria prestar o serviço militar obrigatório")
else:
  print("Você não deveria prestar o serviço militar obrigatório")
