
from collections import defaultdict


#verifica a chance de ser uma frase em portugues
def verify(resposta):
    chance = 0
    for i in range(len(resposta) - 1):
        if resposta[i] in alfabeto:
            if resposta[i+1] in alfabeto:
                chance += float(digrafos[alfabeto.index(resposta[i].upper())][alfabeto.index(resposta[i+1].upper())])
            else:
                continue
        else:
            continue                    
    return chance

#Pega os dividendos menores que 26 de um número
def dividendos(n):
    retorno = []
    for i in range(1, n):
        if i > 26:
            break
        if n % i == 0:
            retorno.append(i)
    return retorno

#Compara duas colunas e retorna a probabilidade de comporem uma palavra
def comparaStrings(base, adicional):
    chance = 0
    for i in range(len(base)):
        chance += float(digrafos[alfabeto.index(base[i].upper())][alfabeto.index(adicional[i].upper())])
    return chance

#pegar o texto cifrado do arquivo cypher.txt
with open('cypher.txt', 'r', encoding='utf-8') as file:
    cypher = file.read()

#pegar as chances dos digrafos do arquivo digrafos.txt
with open('digrafos.txt', 'r', encoding='utf-8') as file:
    conteudo = file.read()
digrafos = conteudo.split("\n")
for i in range(len(digrafos)):
    digrafos[i] = digrafos[i].split(" ")
    digrafos[i][1] = float(digrafos[i][1])


#define alfabeto e frequencia das letras
alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#separa a cifra em uma lista de caracteres
cifra = []
for char in cypher:
    cifra.append(char.upper())

#pega os divisores do tamanho da cifra
end = []
order = defaultdict(list)
divisores = dividendos(len(cifra))

# para cada divisor se obtem o resultado mais provável
for div in divisores:

    #separa a cifra em uma quantidade de colunas igual ao divisor
    order.clear()
    for i in range(len(cifra)):
        order[(i//(len(cifra)//div))].append(cifra[i])

    final = []
    final.append(order[0])

    order.pop(0)

    #para cada coluna é verificado qual é a coluna mais provável de ser sua vizinha até que seja identificado a posição de cada coluna
    while True:
        if not order:
            break
        maior = 0
        #compara cada coluna
        for key in order:
            direita = comparaStrings(final[-1], order[key])
            esquerda = comparaStrings(order[key], final[0])
            if maior < direita:
                tuple = (-1, key)
                maior = direita
            if maior < esquerda:
                tuple = (0, key)
                maior = esquerda
        #Seleciona coluna e remove do pool de colunas ainda não utilizadas
        if tuple[0] == 0:
            final.insert(0, order[tuple[1]])
            order.pop(tuple[1])
        else:
            final.append(order[tuple[1]])
            order.pop(tuple[1])
    #monta a resposta final e adciona ela a uma lista contendo a resposta mais provavel para cada divisor
    resp = ""
    for i in range(len(final[0])):
        for j in range(len(final)):
            resp += (final[j][i])
    end.append(resp)

#compara os resultados de cada tamanho de divisor e escolhe o maior
maior = 0
for tentativa in end:
    if verify(tentativa) > maior:
        maior = verify(tentativa)
        resposta = tentativa


print(resposta)

    
