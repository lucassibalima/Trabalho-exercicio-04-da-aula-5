n = int(input("Digite um número N: "))

soma = 0
for i in range(1, n + 1):
    soma += i

print(f"Soma dos {n} primeiros números: {soma}")