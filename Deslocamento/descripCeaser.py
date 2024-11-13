
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


#define alfabeto e frequencia das letras
alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
freq = {"a":13.9,"b":1.0,"c":4.4,"d":5.4,"e":12.2,"f":1.0,"g":1.2,"h":0.8,"i":6.9,"j":0.4,"k":0.1,"l":2.8,"m":4.2,"n":5.3,"o":10.8,"p":2.9,"q":0.9,"r":6.9,"s":7.9,"t":4.9,"u":4.0,"v":1.3,"w":0.0,"x":0.3,"y":0.0,"z":0.4}
freqCypher = defaultdict(int)

#frequencia da cifra
resp = []
for char in cypher:
    if char in alfabeto:
        resp.append(char)
        freqCypher[char.lower()] += 1
    else:
        resp.append(char)
freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
freqCypher = dict(sorted(freqCypher.items(), key=lambda item: item[1], reverse=True))


#pega os 3 primeiros elementos da frequencia da cifra
auxCypher = cypher
firstElements = list(freqCypher.items())[:3]
desloc = []

#pega o deslocamento necessário para os 3 primerios elementos
#pega a diferença entre as 3 letras mais frequente do alfabeto e as 3 letras mais frequentes da cifra
for element in firstElements:
    for letter in list(freq.keys())[:3]:
        ans = alfabeto.index(letter.upper()) - alfabeto.index(element[0].upper())
        desloc.append(ans)

#monta uma lista contendo os deslocamentos necessários com as possíveis frases
ans = []
trys = []
for deslocamento in desloc:
    for letter in auxCypher:
        if letter in alfabeto:
            ans.append((alfabeto.index(letter)+deslocamento)%26)
        else:
            ans.append(letter)
    trys.append(ans)
    ans = []

#transforma a lista de deslocamentos em frases
resposta = ""
final = []
for tentativa in trys:
    for num in tentativa:
        try:
            resposta += alfabeto[num]
        except:
            resposta += num
    final.append(resposta)
    resposta = ""

#verifica qual a frase mais provavel
maior = 0
for tentativa in final:
    if verify(tentativa) > maior:
        maior = verify(tentativa)
        resposta = tentativa

print(resposta)


