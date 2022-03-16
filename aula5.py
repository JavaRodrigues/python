# Meta caracteres
# \w >>> pega todos os caracteres de um texto.
# utilizando a flag re.A pega todos as letras e numeros sem acentuação
# ^ >> começa com
# $ >> termina com 
# [^a-z] >> negação
# \d >> [0-9]
# \D >> [^0-9]
# \s >> [ \r\n\f\n\t]
# \S >> [^\r\n\f\n\t]
# \b >> borda
# \B >> não borda



import re

texto = '''
Joao trouxe flores para Maria

'''


cpf = "a 177.539.608-81 "

print(re.findall(r'^((/?:[0-9]{3}\.){2}[0-9]{3}-`[0-9]{2})', cpf))

print(re.findall(r'[^a-z]+', cpf))

print(re.findall(r'\w+', texto))
