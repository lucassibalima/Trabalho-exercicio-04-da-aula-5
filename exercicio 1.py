while True:
    nota = float(input("Digite a nota (0 a 10): "))
    
    if nota >= 0 and nota <= 10:
        print("Nota válida!")
        break
    else:
        print("Nota inválida. Tente novamente.")