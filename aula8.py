# re.A >>> ASCII
# re.I >>> IGNORECASE
# re.M >>> Multilinne > ^ $
# re.`S >>> Dotall


import re

texto = '''
    177.539.608-81 ABC
    255.669.678-84 DFG
    152.258.978-54
    358.987.235-12
    '''

print (re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto, flags=re.M))