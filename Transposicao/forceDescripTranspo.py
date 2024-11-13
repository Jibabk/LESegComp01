
from collections import defaultdict
import itertools

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

#Pega os dividendos menores que 9 de um número
def dividendos(n):
    retorno = []
    for i in range(1, n):
        if i >= 9:
            break
        if n % i == 0:
            retorno.append(i)
    return retorno

#Pega todas as permutações para uma lista de [0..n] elementos
def permutacoes(n):
    return (list(itertools.permutations(list(range(n)))))
 

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
final =[]
order = defaultdict(list)
divisores = dividendos(len(cifra))

# para cada divisor se obtem o resultado mais provável
for div in divisores:

    #separa a cifra em uma quantidade de colunas igual ao divisor
    order.clear()
    for i in range(len(cifra)):
        order[(i//(len(cifra)//div))].append(cifra[i])
    perm = permutacoes(div)
    frase = []

    #Para cada permutação possível é calculado a probabilidade de ser uma frase em portugues
    for p in perm:
        for tentativa in p:
            frase.append("".join(order[tentativa]))

         #monta a resposta final e adciona ela a uma lista contendo a resposta mais provavel para cada divisor
        resp = ""
        for i in range(len(frase[0])):
            for j in range(div):
                resp += (frase[j][i])
        final.append(resp)
        frase = []


#compara os resultados de cada tamanho de divisor e escolhe o maior
maior = 0
for tentativa in final:
    if verify(tentativa) > maior:
        maior = verify(tentativa)
        resposta = tentativa


print(resposta)
