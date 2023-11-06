import re

# 1 Completar os problemas que detetamos agora #espacos branco # dona substituir e voltar a substituir e # open
   #1.1 Fazer com que o ficheiro abra num ficheiro txt exterior
   #1.2 Corrigir a divisão de linhas Sr. e D.
   #1.3 Detetar os espaços brancos  


def fase1 (texto):
    fimFrase = r'(\.\.\.|[!?]+|[.])' # define uma expressão regular com os sinais de pontuação
    texto = re.sub(r'Sr\.', '#Sr#', texto) #substituir as abreviaturas por outro símbolo para evitar falsos positivos
    texto = re.sub(r'D\.', '#D#', texto)
    texto = re.sub(r'S\.', '#S#', texto)
    texto = re.sub(r'V\.', '#V#', texto)
    texto = re.sub(r'Ex\.', '#Ex#', texto)
    texto = re.sub(r'P\.', '#P#', texto)           
    novoTexto = re.sub(fimFrase, r'\1||\n', texto) # procura ocorrência do padrão no texto e adiciona ao primeiro grupo || e uma quebra de linha
    novoTexto = novoTexto.replace('#Sr#', 'Sr.') #substitui de volta as abreviaturas para a forma original
    novoTexto = novoTexto.replace('#D#', 'D.')
    novoTexto = novoTexto.replace('#S#', 'S.')
    novoTexto = novoTexto.replace('#V#', 'V.')
    novoTexto = novoTexto.replace('#Ex#', 'Ex.')
    novoTexto = novoTexto.replace('#P#', 'P.')
    return novoTexto
    

def fase2 (texto):
    Frases = re.split(r'\s*\|\|\s*', texto) # encontra as || e divide em frases
    return Frases


def fase3(lf, outputFile):
    with open(outputFile, "w", encoding="UTF-8") as output_file:
        numero = 0  #abre o contador 
        for frase in lf: # para cada frase
            numero += 1 #aumenta um número 
            frase = re.sub(r'\n', r'\n', frase) 
            #frase = re.sub(r'\n', r' ', frase) # frases por linhas sem os espaços brancos
            linhas = f"{numero} {frase}\n"  #imprime o número e a frase a seguir
            output_file.write(linhas) #escreve no ficheiro de output

   # comEspacos = re.sub (r'\n', r'\n\n+', frase)     
#fase3(lf)

texto1 = "Camilo-A_Brasileira_de_Prazins.md"
txt = open(texto1, encoding="UTF-8").read()

texto2 = fase1(txt)
lf3 = fase2(texto2)
fase3(lf3, "linhas.txt")



# 2 Dividir o texto por capítulos e procurar os anos presentes em cada capitulo split por cardinais no cap 1

def divisaoCapitulos (texto, output_file):
    with open(texto, 'r', encoding='utf-8') as file:   #abre e lê o texto
      texto = file.read()
    datas = r'\b\d{4}\b'   #expressão regular que encontra os 4 digitos
    capitulos = re.split(r'\n#', texto)  # divide em capitulos
    capitulos_datas = []  #nova lista com capitulos e datas
    for i, chapter in enumerate(capitulos, start=0):   # enumera
        datasCapitulos = re.findall(datas, chapter)    
        dicionarioCapitulos = {
            'Número do Capítulo': i,
            'Título': chapter,
            'Datas': datasCapitulos
        }
        capitulos_datas.append(dicionarioCapitulos)
    with open(output_file, 'w', encoding='utf-8') as file:
        for dicionarioCapitulos in capitulos_datas:
            file.write(f'Capítulo {dicionarioCapitulos["Número do Capítulo"]}:\n')
            file.write(f'Título {dicionarioCapitulos["Título"]}:\n')
            file.write('Datas: ' + ', '.join(dicionarioCapitulos['Datas']) + '\n\n')


texto3 = "Camilo-A_Brasileira_de_Prazins.md"
divisaoCapitulos(texto3, "capitulos.txt")
        

# 2.1 Versão curta 

def capitulosDatas (texto, output_file):
    with open(texto, 'r', encoding='utf-8') as file:   #abre e lê o texto
      texto = file.read()
    datas = r'\b\d{4}\b'   #expressão regular que encontra os 4 digitos
    capitulos = re.split(r'\n#.*\n', texto)  # divide em capitulos
    capitulos_datas = []  #nova lista com capitulos e datas
    for i, chapter in enumerate(capitulos, start=0):   # enumera
        datasCapitulos = re.findall(datas, chapter)    
        #tituloCap, _ = chapter.split("\n", 1)
        dicionarioCapitulos = {
            'Número do Capítulo': i,
            'Título': chapter.strip(),
            'Datas': datasCapitulos
        }
        capitulos_datas.append(dicionarioCapitulos)
    with open(output_file, 'w', encoding='utf-8') as file:
        for dicionarioCapitulos in capitulos_datas:
            file.write(f'Capítulo {dicionarioCapitulos["Número do Capítulo"]}:\n')
            file.write('Datas: ' + ', '.join(dicionarioCapitulos['Datas']) + '\n\n')


texto3 = "Camilo-A_Brasileira_de_Prazins.md"
capitulosDatas(texto3, "datas.txt")

# 3 Tomar nota de falsos positivos
#7500
# 4 Organizar o github
