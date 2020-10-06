# coding: utf-8

"""
Criar um script em python que consiga ler um arquivo de log e consiga identificar semanticamente o conteúdo do arquivo. A saída dessa identificação deve ser em JSONL que possibilite seleções de partes do log por JSON Query. Utilizar o arquivo de log do apache para teste e avaliação.
"""
import json

# nome do arquivo
filename = 'apache.log'

# Abrir o arquivo, utilizando uma variável chamada fp= ``file pointer``
fp = open(filename)

log_parsed = {}

# Iteramos pela lista que contém as linhas do arquivo
for line in fp.readlines():

    # Removemos o caracter de retorno, utilizando o método de <str>.strip()
    line_stripped = line.strip('\n')

    # Identificar semanticamente as partes das linhas do log
    # Retorna uma lista
    li = line_stripped.split(']')
    log_parsed['datetime'] = li[0].strip(' [')
    log_parsed['loglevel'] = li[1].strip(' [')
    log_parsed['message'] = li[2].strip(' [')

    # JSONL do resultada da identificação semântica
    print(json.dumps(log_parsed) + "\n")





