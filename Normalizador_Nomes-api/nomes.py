# Nova variante dos nomes 
def normalizafile (ficheiro):
   texto = open(ficheiro, encoding="utf-8").read()
   linhas = texto.splitlines()
   for name in linhas:  
      print (normaliza(name))

def normaliza(name):
    # normaliza um nome ao receber um nome
     lista = name.split() # lista com os nomes constintuintes do nome dado
     resultado = lista[-1] + "," # buscar o último nome + uma "","" 
     outros = lista[:-1]  # desde o principio menos o último 
     for n in outros:   # para cada nome nos outros
         resultado = resultado + " " + n  #resultado é o resultado + " " mais o n seguinte
     return resultado


   
normalizafile ("nomes.txt")  # imprimir o normalizar
