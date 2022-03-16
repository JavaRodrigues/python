# Ao entrar com a média do aluno, classifica o conceito
media = float(input('Entre com a média do aluno: '))
if media <= 5:
    conceito = str("REGULAR")
elif media < 7:
    conceito = "BOM"
else:
    conceito = "EXCELENTE"
print("Conceito: ",conceito)