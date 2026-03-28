def calcular_expressao(expr):
    try:
        # Substitui vírgula por ponto (caso o usuário use)
        expr = expr.replace(",", ".")
        
        resultado = eval(expr, {"__builtins__": None}, {})

        return resultado

    except ZeroDivisionError:
        return "Erro: divisão por zero."
    except Exception:
        return "Erro: expressão inválida."


while True:
    print("\n=== CALCULADORA POR EXPRESSÃO ===")
    print("Digite uma expressão (ou 'sair' para encerrar)")
    
    entrada = input(">>> ").strip().lower()

    if entrada == "sair":
        print("Encerrando...")
        break

    resultado = calcular_expressao(entrada)
    print("Resultado:", resultado)
