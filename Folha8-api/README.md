# FPLN: Folha8

Este trabalho consistiu na realização de cinco exercícios. Quatro dados pelo docente da UC e um  extra que estava ao critério de cada aluno.
Antes de começar os exercícios fiz importação das expressões regulares e atribuí a variável texto à string "folha8.OUT.txt". 

## Exercício 1 - Qual o número de publicações?

- Neste exercício, o objetivo era encontrar o número de publicações presentes no ficheiro txt fornecido anteriormente.

Comecei por criar uma função chamada "publicacoes".
Criei a variável noticias que invoca o texto e que o lê e usa o enconding UTF-8. 
A fim de encontrar o número de publicações, decidi que uma vez que cada publicação está etiquetada com as etiquetas <pub> e </pub>, ao contar o número de ocorrências de <pub> em noticias, encontraria o número de publicações.
Assim, usei uma expressão regular que encontrasse o padrão <pub> em noticias. Chamei a essa variável pub, e na linha a seguir usando a função len() contei o número de <pub> presentes nessa variável.
Por fim, fiz uma impressão numa f string onde está a string "O número de publicações é de" e em seguida o contador. 
Fora da função, invoquei publicacoes(texto) e obtive o número de publicações, 8777. 

## Exercício 2 e 3 - Extrair a lista de TAGS e as suas respetivas ocorrências

- Considerei que os exercícios 2 e 3 poderiam ser realizados no mesmo código uma vez que estes estão diretamente relacionados. 

Comecei por definir uma função chamada tagsOco que recebe um texto e terá um output onde será possível verificar as TAGS extraídas e o seu respetivo número de ocorrências.
A variável noticias contém o ficheiro dado e lido com o encoding UTF-8. Na linha a seguir, posteriormente, fiz na mesma variável replace de \n por um espaço ' ', porque no resultado final algumas tags que eram compostas por combinações de palavras estavam a ficar separadas, como por exemplo:
"lei da
rolha: 2"
Após essa alteração, cada TAG ficou numa linha só como pretendido.
"lei  da rolha: 2"
A seguir, criei a variável tagOco, com o objetivo de extrair as TAGS. Cada tag aparece da seguinte forma: tag:{exemplo}. Assim, com o objetivo de captar o que está dentro das chavetas, criei a seguinte expressão regular: 'tag:{([^}]+)}'. Os parênteses delimitam o grupo de captura, ou seja, só queremos capturar o que está entre { e }, sem capturar esses sinais. [^}]+ quer dizer que captura qualquer classe de carácteres([]) excepto (^) a chaveta(}). O + quer dizer que pode existir 1 ou mais ocorrências desse padrão, ou seja, quaisquer que sejam os caracteres que existam dentro de (), desde que não seja uma chaveta, estes vão ser capturados.
Na linha a seguir abri um dicionário a que chamei de contador. 
Depois fiz um loop para cada tag em tag0co, onde se a tag já estivesse no contador, seria adicionada mais uma unidade, caso contrário esta adquire o valor 1.
Como no resultado final as tags não estavam ordenadas por uma ordem específica, decidi organizar por ordem decrescente através da função sorted().
Depois, criei um ficheiro de output, onde por cada tag em sorted_ocurrences, o código vai imprimir a tag, o número de ocorrências e fazer um parágrafo.
Fora da função atribui a string "tags.txt" (o ficheiro onde quero que o resultado seja impresso) à variável output_file_path, e abaixo invoquei a função tagsOco, onde existem dois argumentos, a variável texto e a variável output_file_path.

## Exercício 4 - Intervalo de datas

- Neste exercício o objetivo era encontrar qual a data mais antiga e a mais recente no ficheiro txt. Este foi o exercício que requiriu mais tempo, pesquisa e ajuda para o conseguir concluir. A maior dificuldade foi conseguir captar e extrair as datas uma vez que grande parte das expressões regulares que utilizei não o estavam a conseguir fazer devido às datas estarem em português. Na impressão, os meses ficaram em letra minúscula ao contrário da versão que está no ficheiro txt original, porém não consegui mudar o código para que ficasse da mesma forma que no ficheiro original.

Comecei por fazer import da classe datetime e o módulo locale.
Uma fez que a classe datetime só funciona com os meses em Inglês, foi necessário criar um dicionário que incluía os meses em português e o seu equivalente em inglês. Para isso foi criada uma função parse_portuguese_date que contém um dicionário (months_pt) onde a chave é o nome do mês em português e o valor o mês em inglês. 
Ainda na mesma função há um loop onde a variável date_srt contém um replace onde "de {pt_month}(mês em português) de" é substituído pelo seu equivalente em inglês. No final é retornada a variável date_str.

A seguir, criei a função intervaloDatas que recebe um texto, o lê com o enconding UTF-8 e fica guardado na variável linhas.
Depois, a variável datas_linhas contém uma lista em compreensão onde é usada a função .strip() para remover todas as linhas que não começam por #DATE. 
Na linha seguinte é encontrado o padrão_datas_pt que começa por #DATE: seguido de  \[\w+\] (neste caso \[ e \] serve para indicar que estes caracteres são literais e não código de expressão regular e \w+ significa pode estar qualquer ocorrência de um ou mais caracteres.), seguido de Redacção F8 e por fim é definido o grupo de captura (entre parênteses) que pode ser um ou mais números \d+, seguido da string "de", depois um dos meses do ano em português, mais uma vez uma string "de", e por fim um número (\d) de quatro dígitos {4}. 
Na linha a seguir é aberta uma lista em branco, a qual é invocada por lista_datas.
Para cada linha em datas_linhas é aplicado o padrão padrao_datas_pt para extrair as datas e se houver uma correspondência, esta é adicionada à lista_datas, e através da função parse_portuguese_date, o grupo de captura 1 (que inclui as datas extraídas) é convertido para inglês. 
Na variável objetos_datas, a informação na lista lista_datas é convertida para a classe datetime para que o código consiga fazer a comparação
Na linha a seguir, o local é definido para Portugal.
Por fim, a data_mais_antiga é o valor mais pequeno encontrado na variável objetos_datas (É usada a função min()), e para obter a data mais recente é utilizada a função max() e é impressa numa f string qual é a data mais antiga, e a mais recente.(Neste caso 21 de setembro de 2014 e 08 de janeiro de 2018 respetivamente.)
Fora da função é invocada a função intervaloDatas com o texto da Folha 8.

## Exercício 5 - Livre

- Para o exercício 5 decidi realizar duas alíneas. Na primeira, é calculado o número de notícias por data, e na segunda, qual o TOP 10 das datas com mais notícias para verificar as datas com maior atividade do jornal Folha 8.

### 5.1 Qual o número de notícias por data?

Criei uma função contagemPublicacoes que contém dois argumentos, o ficheiro de entrada que é o texto e o ficheiro de output, o arquivo_saida.
A função lê o texto dado com o enconding UTF-8 e fica associado à variável conteudo.
É usado um re.findall para captar as datas em conteudo e de seguida é aberto um dicionário que é invocado por contagem_datas.
De seguinda é feito um loop em que para cada data_pub em datas_pub, se esta já se encontrasse lá era adicionada uma unidade, caso contrário passava a assumir o valor 1. 
Por fim é adicionado um loop onde para cada data e contagem nos items de contagem_datas, é impresso num ficheiro de output a string "Dia" seguida da data, um traço (-) e por fim a contagem e \n para fazer um parágrafo no final da linha.
Fora da função é invocado contagemPublicacoes cujo primeiro argumento é o texto e o segundo argumento é arquivo_saida que contém "noticiaspordatas.txt".

### 5.2 Qual o TOP10 dos dias com mais notícias?

O código é quase igual ao anterior, excepto que a função foi nomeada por top10 e após o loop para cada data_pub em datas_pub é a seguir calculado o top_10 através da função sorted().No final da linha é adicionado [:10] para só serem apresentados os 10 primeiros resultados. Ao remover essa lista seria calculada a totalidade do dicionário contagem_datas.
No final do código, é feita a impressão para um txt chamado top10.txt. Na primeira linha é impresso: "Top 10 dos dias com mais publicações:\n e nas linhas seguintes são impressas, através de uma f string, as datas, seguidas da contagem.

