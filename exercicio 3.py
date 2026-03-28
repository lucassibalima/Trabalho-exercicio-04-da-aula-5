soma = 0
quantidade = 0

while True:
    numero = float(input("Digite um número (-1 para sair): "))
    
    if numero == -1:
        break
    
    soma += numero
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"Média: {media}")
else:
    print("Nenhum número válido foi digitado.")