# LESegComp01
Criptografia e descriptografia de Deslocamento e Transposição

## Deslocamento
### Como gerar a cifra de Deslocamento
1. Coloque a mensagem desejada no arquivo `mensagem.txt`.
2. Rode o arquivo `cifraCeaser.py` no path `./Deslocamento` :
    ```bash
    python3 cifraCeaser.py
    ```
3. Escolha uma chave numérica para o deslocamento durante a execução do script.
4. A mensagem criptografada será salva em `cypher.txt`.

### Como descriptografar a cifra de Deslocamento por força bruta
1. Utilize a mesma chave numérica usada para criptografar.
2. Rode o arquivo `forceDescripCeaser.py` no path `./Deslocamento`:
    ```bash
    python3 forceDescripCeaser.py
    ```
3. A mensagem descriptografada será exibida.

### Como descriptografar a cifra de Deslocamento por análise de distribuição
1. Utilize a mesma chave numérica usada para criptografar.
2. Rode o arquivo `descripCeaser.py` no path `./Deslocamento`:
    ```bash
    python3 descripCeaser.py
    ```
3. A mensagem descriptografada será exibida.

## Transposição
### Como gerar a cifra de Transposição
1. Coloque a mensagem desejada no arquivo `mensagem.txt`.
2. Rode o arquivo `cifraTranspo.py` no path `./Transposicao`:
    ```bash
    python3 cifraTranspo.py
    ```
3. Escolha uma palavra-chave para determinar a ordem das colunas durante a execução do script.
4. A mensagem criptografada será salva em `cypher.txt`.

### Como descriptografar a cifra de Transposição por força bruta 
(pode demorar alguns segundos)
1. Utilize a mesma palavra-chave usada para criptografar.
2. Rode o arquivo `forceDescripTranspo.py` no path `./Transposicao`:
    ```bash
    python3 forceDescripTranspo.py
    ```
3. A mensagem descriptografada será exibida.

### Como descriptografar a cifra de Transposição por análise de distribuição
1. Utilize a mesma palavra-chave usada para criptografar.
2. Rode o arquivo `descripTranspo.py` no path `./Transposicao`:
    ```bash
    python3 descripTranspo.py
    ```
3. A mensagem descriptografada será exibida.
