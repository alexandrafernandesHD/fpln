import re
texto = "folha8.OUT.txt"

#1. Calcular quantas publicações

def publicacoes(texto):
    noticias = open(texto, 'r', encoding='utf-8').read()
    pub = re.findall(r'<pub>', noticias)
    contador = len(pub)
    print(f"O número de publicações é {contador}")

publicacoes(texto)


#2 + 3 Extrair a lista das TAGS e as suas ocorrências

def tagsOco(texto, output):
    with open(texto, 'r', encoding='utf-8') as file:
        noticias = file.read()
    noticias = noticias.replace('\n', ' ')    
    tagOco = re.findall(r'tag:{([^}]+)}', noticias)
    contador = {}
    for tag in tagOco:
        if tag in contador:
            contador[tag] += 1
        else:
            contador[tag] = 1
    sorted_ocurrences = sorted(contador.items(), key=lambda x: x[1], reverse=True)
    with open(output, 'w', encoding='utf-8') as output_file:
        for tag, count in sorted_ocurrences:
            output_file.write(f"{tag}: {count}\n")


output_file_path = "tags.txt" 

tagsOco(texto, output_file_path)

# 4 Intervalo de datas

from datetime import datetime
import locale
#Função que cria um dicionário com os meses em Pt e o equivalente em Eng
def parse_portuguese_date(date_str):
    months_pt = {
        'Janeiro': 'January',
        'Fevereiro': 'February',
        'Março': 'March',
        'Abril': 'April',
        'Maio': 'May',
        'Junho': 'June',
        'Julho': 'July',
        'Agosto': 'August',
        'Setembro': 'September',
        'Outubro': 'October',
        'Novembro': 'November',
        'Dezembro': 'December'
    }

    for pt_month, en_month in months_pt.items():
        date_str = date_str.replace(f' de {pt_month} de ', f' {en_month} ')
    
    return date_str

def intervaloDatas(texto):
    with open(texto, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    datas_linhas = [linha.strip() for linha in linhas if linha.startswith('#DATE')] 
    padrao_datas_pt = r'#DATE: \[\w+\] Redacção F8 — (\d+ de (Janeiro|Fevereiro|Março|Abril|Maio|Junho|Julho|Agosto|Setembro|Outubro|Novembro|Dezembro) de \d{4})'
   

    lista_datas = []
    for linha in datas_linhas:
        match_pt = re.search(padrao_datas_pt, linha)      
        if match_pt:
            lista_datas.append(parse_portuguese_date(match_pt.group(1)))

    objetos_datas = [datetime.strptime(parse_portuguese_date(data), '%d %B %Y') for data in lista_datas]

    locale.setlocale(locale.LC_TIME, 'pt_PT.UTF-8')

    data_mais_antiga = min(objetos_datas)
    data_mais_recente = max(objetos_datas)

    print(f"A data mais antiga é {data_mais_antiga.strftime('%d de %B de %Y')} e a data mais recente é {data_mais_recente.strftime('%d de %B de %Y')}")

intervaloDatas(texto)

#5. Exercício livre 

#Quantas publicações por dia?
def contagemPublicacoes(texto, arquivo_saida):
    with open(texto, 'r', encoding='utf-8') as file:
        conteudo = file.read()

    datas_pub = re.findall(r'#DATE: .+ (\d{1,2} de \w+ de \d{4})', conteudo)
    contagem_datas = {}

    for data_pub in datas_pub:
        if data_pub in contagem_datas:
            contagem_datas[data_pub] += 1
        else:
            contagem_datas[data_pub] = 1


    with open(arquivo_saida, 'w', encoding='utf-8') as output_file:
        for data, contagem in contagem_datas.items():
            output_file.write(f"Dia {data} - {contagem}\n")

arquivo_saida = "noticiaspordatas.txt"
contagemPublicacoes(texto, arquivo_saida)

#Top 10 dos dias por publicações

def top10(texto):
    with open(texto, 'r', encoding='utf-8') as file:
        conteudo = file.read()

    datas_pub = re.findall(r'#DATE: .+ (\d{1,2} de \w+ de \d{4})', conteudo)
    contagem_datas = {}

    for data_pub in datas_pub:
        if data_pub in contagem_datas:
            contagem_datas[data_pub] += 1
        else:
            contagem_datas[data_pub] = 1

    top_10 = sorted(contagem_datas.items(), key=lambda x: x[1], reverse=True)[:10]

    with open('top10.txt', 'w', encoding='utf-8') as output_file:
        output_file.write("Top 10 dos dias com mais publicações:\n")
        for data, contagem in top_10:
            output_file.write(f"{data}: {contagem}\n")


top10(texto)
