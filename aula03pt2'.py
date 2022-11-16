#Criação de funções

preco = 1999.90

#Calcular apenas 5% de imposto, guardar na variavel imposto e exibir na tela
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)

#Criar uma função calcular_imposto() que calcular um imposto de 5% e retorna a quem pediu...
#Isso é a declaração da função (Como ela funciona)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

#Aqui é o uso... aqui é imposto a calcular.. e exibir na tela
preco = 299
imposto = calcular_imposto(preco)
print(f"Esse é com a função (7%): {imposto}")

#Calcular imposto de varios valores(1o Preço 2° Imposto))
valores = [100, 200, 300, 400]

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")

#Declarar uma função calcular_imposto_aliquota que recebe dois parametros: o preço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calculado. Se a aliquota não for informada, utilize 7% como padrão.

def calcular_imposto_aliquota(valor, aliquota=7):
  imposto = valor * (aliquota / 100)
  return imposto

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor)}")