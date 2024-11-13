
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

def dividendos(n):
    retorno = []
    for i in range(1, n):
        if i >= 9:
            break
        if n % i == 0:
            retorno.append(i)
    return retorno

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

cifra = []
for char in cypher:
    cifra.append(char.upper())

final =[]
order = defaultdict(list)
divisores = dividendos(len(cifra))
for div in divisores:
    order.clear()
    for i in range(len(cifra)):
        order[(i//(len(cifra)//div))].append(cifra[i])
    perm = permutacoes(div)
    frase = []
    for p in perm:
        for tentativa in p:
            frase.append("".join(order[tentativa]))

        resp = ""
        for i in range(len(frase[0])):
            for j in range(div):
                resp += (frase[j][i])
        final.append(resp)
        frase = []


#verifica qual a frase mais provavel
maior = 0
for tentativa in final:
    if verify(tentativa) > maior:
        maior = verify(tentativa)
        resposta = tentativa


print(resposta)