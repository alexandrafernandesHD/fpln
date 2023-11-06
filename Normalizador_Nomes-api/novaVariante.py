# Nova variante dos nomes 
def normalizafile (ficheiro):
   texto = open(ficheiro, encoding="utf-8").read()
   linhas = texto.splitlines()
   for name in linhas:  
      print (normaliza(name))

def normaliza(name):

     lista = name.split() 
     resultado = lista[-1] + "," 
     proprios = lista[:1] 
     caracteres = lista[-2] 
     firstChar = caracteres[0] + "."
     for n in proprios:   
         resultado = resultado + " " + n + " " + firstChar 
     return resultado

   
normalizafile ("nomes.txt")  
