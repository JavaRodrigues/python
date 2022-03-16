# Entra com um número e verifica se este número é par ou impar
vResultado = ""
vNum = int(input('Entre com um número: '))
if vNum % 2 == 0:
    vResultado = "PAR"
else:
    vResultado = "IMPAR"
print("O número é: ",vResultado) #Apresenta o resultado