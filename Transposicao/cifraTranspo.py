alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

print("A chave deve ser uma palavra de até 8 caracteres, que não possua repetições")
while True:
    key = list(input("Qual a chave para a criptografia?\n"))
    if len(key) > 8:
        print("A chave contém mais de 8 caracteres. Selecione uma chave válida")
        continue
    if len(key) != len(set(key)):
        print("A chave contém caracteres repetidos. Selecione uma chave válida")
        continue
    for char in key:
        if char not in alfabeto:
            print("A chave contém caracteres inválidos. Selecione uma chave válida")
            continue
    break

#passa a mensagem para uma lista de caracteres minúsculos
with open('mensagem.txt', 'r', encoding='utf-8') as file:
    conteudo = file.read()
characters = []
for char in conteudo:
    characters.append(char.lower())

#completa a lista de caracteres com o alfabeto
offset = len(key) - len(characters)%len(key)
for i in range(offset):
    characters.append(alfabeto[i])
    
#cria a matriz separada por colunas
shuffle = []
for i in range(len(key)):
    shuffle.append([])
for i in range(len(characters)):
    shuffle[i%len(key)].append(characters[i])

#cria o dicionário com contendo a chave e coluna
final = {}
for i in range(len(key)):
    key[i]=ord(key[i])-97
    final[key[i]] = shuffle[i]

#monta o texto criptografado
final = sorted(final.items())
answer = ""
for value in final:
    answer += "".join(value[1])

#salva o texto criptografado
with open('cypher.txt', 'w', encoding='utf-8') as file:
    file.write(answer)
print("Texto encriptografado com sucesso")