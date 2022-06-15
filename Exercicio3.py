#Importamos o modúlo json para podermos ler o arquivo
import json

#Abrir o arquivo como um objeto python e coloca-lo na váriavel 'arquivo'
with open('dados.json') as arq:
    arquivo = json.load(arq)

#Posição na lista
pos_maior = 0

#Valor inicial da lista
vmaior = arquivo[0]['valor']

#Processo de descobrir o maior valor da lista a partir da posição 1
while pos_maior < len(arquivo[1:]):
    #Valor inicial de comparação
    valorm = arquivo[pos_maior]['valor']
    #Verificação se o valor não é igual a zero, ou seja, é um fim de semana
    if valorm != 0.0:
        #Comparação entre o valor inicial e o atual
        if vmaior < valorm:
            #Se maior, o valor atual subistitui o inicial
            vmaior = valorm
    #Caso o valor seja 0.0, se passa para próxima posição e continua o loop          
    else:
        pos_maior +=1
        continue
    #A posição é incrementada
    pos_maior +=1

#Mesmo processo para descobrir o menor valor, apenas com o sinal de comparação invertido
vmenor = arquivo[0]['valor']
pos_menor = 0

while pos_menor < len(arquivo):
    valor = arquivo[pos_menor]['valor']
    if valor != 0.0:
        if vmenor  > valor:
            vmenor = valor
    else:
        pos_menor +=1
        continue
    pos_menor +=1

pos_soma = 0
#Valor inicial da soma
soma = 0
#Uma lógica similar as anteriores
while pos_soma < len(arquivo):
    s = arquivo[pos_soma]['valor']
    #Vemos se o valor não é nulo, ou seja, indica um fim de semana, e incrementamos a posição
    if s == 0.0:
        pos_soma += 1
        continue
    #Se ele não é nulo, somamos ele ao valor da soma e incrementamos a posição
    else:
        soma = s + soma 
        pos_soma+=1


print('O menor valor é {}'.format(vmenor))
print('O maior valor é {}'.format(vmaior))
print("A soma de todos os valores é: {}".format(soma))

