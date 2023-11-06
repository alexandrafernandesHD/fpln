# Trabalho de casa 19/10/2023

import re
from collections import Counter
Nome = "Camilo-A_Brasileira_de_Prazins.md"

txt = open(Nome, encoding="UTF-8").read()

# 1. Quantos capítulos "# " (md) procurar ocorrências e contar

def numCapitulos (txt):
    linhas =  txt.split() #divide o texto em linhas
    contador = 0  # abre um contador
    for l in linhas:  #em cada linha
        if l.startswith("#"): #se começar por um #
            contador += 1  #o contador adiciona mais uma ocorrência quando encontra "#"
    return contador

contador = numCapitulos(txt)  

print(f"O número de capítulos é: {contador}")

# 2. Escrever para fora, índice dos capítulos 

def indice (txt):
    linhas =  txt.split("\n") #divide o texto em linhas
    capitulos=[] # cria uma nova lista
    for linha in linhas:  
        if linha.startswith("# "): # se a linha começar por #
            capitulos.append(linha) # junta os capitulos à lista
    with open("indice.txt", "w", encoding="UTF-8") as index_file: # ou f = ("indice.txt", "w", encoding="UTF-8")
         for linha in capitulos:
           index_file.write(linha + '\n')

indice (txt)

# 3. Ocorrências com palavras em minúsculas 

def ocoMinusculas (texto):
    palavras = re.findall (r'\w+', texto) # findall palavras
    minusculas = []
    oco = {}  #cria um dicionário vazio, uma lista de pares
    for palavra in palavras :
        palavra_minuscula = palavra.lower()  # todo o texto em minusculas
        minusculas.append(palavra_minuscula) # adiciona na lista minusculas
        if palavra_minuscula in oco:
             oco[palavra_minuscula] += 1 #adiciona mais uma oco
        else: 
            oco [palavra_minuscula] = 1 # se não pertence as oco são 1
   # for palavra, ocorrencias in oco.items():
       # print(f"{palavra}: {ocorrencias}")
    ocoAlfabeto = sorted(oco.items(), key=lambda item: item[0])  # pega nos items no dicionário oco põe em ordem alfabética, pega função lambda que extrai o 1º item do dicionário
    with open("ocoMinusculas.txt", "w", encoding="UTF-8") as output_file: # cria ficheiro output, ocoMinusculas.txt, "w" excreve, e faz o enconding
        for palavra, ocorrencias in ocoAlfabeto : #corre palavra e ocorrencias e escreve-as no ficheiro output
            output_file.write(f"{palavra}: {ocorrencias}\n") #\n: adiciona uma nova linha

ocoMinusculas(txt)

# 4. Quantas frases? (Contar quantas pontuações seguidas aparecem)



def frasesCount (texto):
    pontuacao = re.findall(r'\.\.\.|[!?]+|[!?]|[.]', texto) #encontrar todos ... ?! !? !? .
    contador = Counter(pontuacao) #função que conta e coloca num dicionário
    total = sum(contador.values()) # soma dos values no dicionário
    print (contador)
    print ("O número total de frases é: " + str(total))

frasesCount(txt)

# 5. Qual o comprimento médio da frase em palavras ex. se o texto tinha 50 palavras e 5 frases, o comprimento médio é 10 

def comprimentoMedio (texto):
    palavras = re.findall (r'\w+', texto)
    pontuacao = re.findall(r'\.\.\.|[!?]+|[\.]', texto) #encontrar todos ... ?! !? !? .
    contador = Counter(pontuacao) #função que conta e coloca num dicionário
    total = sum(contador.values()) # soma dos values no dicionário
    if total > 0:
        compMedio= len(palavras) / total
    else:
        compMedio = 0
    print ("O comprimento médio das frases em palavras é: " + str(compMedio))
    print(len(pontuacao)) # conta o len de pontuação que equivale ao número de frases
    print (contador.most_common(2))
    

comprimentoMedio(txt)

# 6. Livre
# A palavra mais longa, nº. de caracteres da mesma e localização no texto

def palavraLonga (texto):
    palavras = re.findall (r'\w+', texto) # encontra todas as palvras sem pontuação
    palavraComprida = max(palavras, key = len) # encontra a palavra mais comprida
    print ("A palavra mais comprida no texto é: " + palavraComprida)
    numeroCaracteres = len(palavraComprida) # tamanho da palavra mais comprida
    print(f"O número de caracteres em {palavraComprida} é: {numeroCaracteres}") 
    posicaoPals = palavras.index(palavraComprida) #procura a palavra mais comprida em Palavras 
    start = texto.find(palavras[posicaoPals]) #texto.find(palavraComprida) #procura no texto original o incio dessa palvra
    end = start + len(palavraComprida) #faz uma soma para calcular o número da localização dos caracteres
    print(f"A palavra está localizada em: {start}-{end}")
    print(texto[start:end])



palavraLonga (txt)
    
