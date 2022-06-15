#O usuário define a quantidade de números que a sequência possuirá

tamanho = int(input("Informe o tamanho desejado da sequência fibonacci: "))  

#O usuário define o número que será procurado na sequência
num = int(input("Informe o número que deseja encontrar na sequência: "))


#Criação da função Fibonacci
def fibonacci(tamanho,num):
    #Toda sequência Fibonacci começa com 0 e 1
    sequencia = [0,1]

    #Como já temos os dois primeiros termos da lista, o range começa na posição 2 e vai até a ultima posição
    #definida pelo usuário na variavél 'tamanho'
    for i in range(2,tamanho):
        #Somamos os números nas duas posições anteriores para forma o que estará na posição atual    
        prox_num = sequencia[-1] + sequencia[-2]

        #Adicionamos o resultado da soma a lista
        sequencia.append(prox_num)
    
    #Criação da variável 'pos' para marcar a posição que estamos na lista
    pos = 0

    #Vamos andar a lista até chegar ao fim dela 
    while pos < len(sequencia):
        #Checamos se o número na posição atual da sequencia é igual ao número dado pelo usuário
        #Se sim, ele retorna a mensagem e termina o loop
        if sequencia[pos] == num:
            print("O número {} aparece na posição {} dessa sequência Fibonacci.".format(num, pos+1))
            break
        #Se não, incrementamos a posição 
        else:
            pos += 1
            #E checamos se ele está na ultima posição da sequência
            #Se sim, é retornada a mensagem
            if pos == len(sequencia):
                print("O número {} não aparece nessa sequência Fibonacci".format(num))
            #Se não, o loop continua
            else:
                continue

       
fibonacci(tamanho,num)