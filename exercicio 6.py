while True:
    print("\n=== CALCULADORA ===")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando o programa...")
        break

    elif opcao in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Digite apenas números válidos.")
            continue

        if opcao == "1":
            resultado = num1 + num2
            print(f"Resultado: {resultado}")

        elif opcao == "2":
            resultado = num1 - num2
            print(f"Resultado: {resultado}")

        elif opcao == "3":
            resultado = num1 * num2
            print(f"Resultado: {resultado}")

        elif opcao == "4":
            if num2 == 0:
                print("Erro: divisão por zero não é permitida.")
            else:
                resultado = num1 / num2
                print(f"Resultado: {resultado}")

    else:
        print("Opção inválida! Tente novamente.")