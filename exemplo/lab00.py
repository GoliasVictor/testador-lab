print("Olá Eu sou o Testinho, me diga sua idade")
idade = int(input())
print("Agora me diga, Você já é adulto?")
print("(1) para sim")
print("(2) para não")
digito = int(input())
if(idade >= 18 ):
	if(digito == 1):
		print(f'Você está certo, voce é adulto e tem {idade} anos') # Esse está faltando um acento
	elif(digito == 2):
		print(f'não minta, você tem {idade} anos, maiores 18 já são adultos') # Esse o n é minusculo
else:
	if(digito == 1):
		print(f'Não minta, você é menor de idade ainda, você tem apenas {idade} anos ') # Esse possue um espaço a mais no final
	elif(digito == 2):
		print(f'Isso ai, você tem {idade}, você é menor de idade, epoca de sonhar') # Esse está correto, sem erros


