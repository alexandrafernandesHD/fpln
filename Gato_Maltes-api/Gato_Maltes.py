import re
texto = """Era uma vez um gato maltês, 
que tocava piano e falava francês, 
queres que te conte outra vez?"""

# a função que conte as palavras com comprimento 3
#b. Escreva a lista das palavras ordenadamente (ordem alfabética)
#c. Qual a palavra mais comprida?
#d. Calcular o número de ocorrências de cada palavra no texto 
#e. Outras perguntas 
#Versão que possa ler de outro ficheiro

# a

def countwords (texto):
    words = texto.split()
    contador = 0 
    for palavra in words:
        a = palavra.removesuffix("?")
        texto = palavra.split()
        if len(a) == 3:
            contador = contador + 1
            print (palavra, "=3")
    print (contador)
            
countwords(texto)

# b 

def ordemAlfabetica (texto):
    palavras = texto.split() #dividir a string em palavras
  #  minusculas = [] #nova lista 
  #  for palavra in palavras: 
#        minusculas.append(palavra.lower()) #junta tudo em minusculo na nova lista
    minusculas = [palavra.lower() for palavra in palavras]
    minusculas.sort()
    print (minusculas)

ordemAlfabetica (texto)

# c 
def palavraMaiscomprida(texto):
    semInt = texto.removesuffix("?")
    semVirg = semInt.replace(",", "")
    semExcl = semVirg.replace("!", "")
    sem2Pontos = semExcl.replace(":", "")
    semPonto = sem2Pontos.replace(".", "")
    semPonVir = semPonto.replace(";", "")
    semTrav = semPonVir.replace("-", "")
    textoNovo = semTrav.split()
    longest_word = max(textoNovo, key=len) #max - pega numa lista e calcula o maior dessa lista
    contador = len(longest_word)
    print("A palavra mais comprida é:", longest_word)
    print("O número de caracteres na palavra mais comprida é:", contador)
    
    
palavraMaiscomprida(texto)


# d

def ocorrencias (texto):
    texto = re.sub(r'[.,!:?]', '', texto)
    words = texto.split()
    print(words)
    oco = {}  #cria um dicionário vazio, uma lista de pares
    for palavra in words :
        if palavra in oco:
            oco[palavra] = oco[palavra] +1 #adiciona mais uma oco
        else: 
            oco [palavra] = 1 # se não pertence as oco são 1
    for key in sorted(oco) :
        print(f"{key}\t{oco[key]}")
 
ocorrencias(texto)
