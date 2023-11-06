# Replace

texto = "Eu ontem comprei morangos"

x = texto.replace("morangos", "maçãs")

print(x)


#Contar palavras: 

texto = """Espera-nos uma viagem de conhecimento e descoberta com várias paragens ao longo do percurso para desvendar
 os mistérios das noites estreladas, conhecer pelo nome as principais estrelas e as constelações noturnas"""
 
print ("The original string is : " + texto)
res = texto.count(" ")+1
print ("The number of words in string are : " + str(res))

#Título

texto = "o homem que mordeu o cão"

x = texto.title()

print(x)

#Dividir o texto

texto = "ontem o josé jantou bacalhau. hoje almoçou pizza. logo vai jantar atum."

x = texto.split(".")

print(x)

#Pode ser impresso?

txt = """Entre outras curiosidades, os caminheiros poderão também apreender noções e métodos de orientação 
baseados nas estrelas e dicas de leitura de um mapa celeste. No final da atividade, orientada pela Borealis, 
os participantes têm oportunidade de observar estrelas e planetas com telescópio."""

x = txt.isprintable()

print(x)

txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)

#Começa por

txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)


txt = "Hello, welcome to my world."

x = txt.startswith("Hi")

print(x)


txt = """Entre outras curiosidades, os caminheiros poderão também apreender noções e métodos de orientação 
baseados nas estrelas e dicas de leitura de um mapa celeste. No final da atividade, orientada pela Borealis, 
os participantes têm oportunidade de observar estrelas e planetas com telescópio."""
x = txt.startswith("Entre")

print(x)
