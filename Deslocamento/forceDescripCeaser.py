
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

#define alfabeto 
alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#coloca todas as possibilidades de deslocamento em uma lista
resp = []
for char in cypher:
    resp.append(char.upper())

final = []
aux = []
for i in range(27):
    for j in range(len(resp)):
        if resp[j] in alfabeto:
            aux.append(alfabeto[(alfabeto.index(resp[j]) + i)%26])
        else:
            aux.append(resp[j])
            continue
    final.append(aux.copy())
    aux = []


#verifica qual a frase mais provavel
maior = 0
for tentativa in final:
    if verify(tentativa) > maior:
        maior = verify(tentativa)
        resposta = tentativa

print("".join(resposta))

