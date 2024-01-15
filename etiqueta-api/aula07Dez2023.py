"""Dado um texto, vamos substituir cada verbo por <v lema="verbo no infinitivo">...</v>"""

import spacy

nlp = spacy.load("pt_core_news_lg")  #nlp - natural language processer

# Process whole documents
text = """Quando o João Duarte chegou a Braga, alugou um enorme carro azul. foi para a quinta do pai, em Terras de Bouro, tratar dos animais e 
dos apetrechos agrícolas."""
doc = nlp(text) #criou-se a árvore documental 

# Analyze syntax
#print("Verbs:", [(token.text, token.lemma_) for token in doc if token.pos_ == "VERB"]) #tokens são as palavras e a pontuação pos - part of speech (categoria morfo-sint.)
for frase in doc.sents:
    for token in frase:
       if token.pos_ == "VERB":
          print(f'<v lema="{token.lemma_}">{token.text}</v> ',end='') #imprimir o token
       else: 
          print(f'{token.text} ',end='')
    
    print("---")


# Find named entities, phrases and concepts
for entity in doc.ents: #entidades aqui são os Nomes próprios (lugares, pessoas, instituições)
    print(entity.text, entity.label_) #label poderá ser: Pessoa, Local, Instituição
