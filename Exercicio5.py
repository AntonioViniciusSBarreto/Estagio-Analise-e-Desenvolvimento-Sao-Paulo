
lista = 'Olá Mundo' 
#Tamanho da lista
L = len(lista)
#Definindo o tamanho da lista invertida
#Multiplicação pela len da lista original para que a invertida tenha o mesmo tamanho
invertida = [None]*L

#Troca de posição das letras
for item in lista:
    L = L - 1
    invertida[L] = item

#Criação de uma string vazio onde será coloca a lista invertida
espaco = ''

#Colocando a lista invertida na string
for vazio in invertida:
    espaco += vazio 
  
print(espaco)