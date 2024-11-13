while True:
    try:
        key = int(input("Qual o deslocamento desejado para a criptografia\n"))
        break
    except:
        print("Selecione um número várlido")

alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

hash = {}
x = 0
for letra in alfabeto:
    hash[letra] = x
    x += 1

with open('mensagem.txt', 'r', encoding='utf-8') as file:
    conteudo = file.read()

codes = []

for char in conteudo:
    if char.lower() in alfabeto:
        codes.append((hash[char.lower()] + key)%26)
    else:
        codes.append(char)

characters = []
for num in codes:
    try:
        characters.append((alfabeto[int(num)]).upper())
    except:
        characters.append(num)

print("Texto encriptografado com sucesso")
with open('cypher.txt', 'w', encoding='utf-8') as file:
    file.write("".join(characters))