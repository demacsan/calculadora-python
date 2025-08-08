def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: divisão por zero não é permitida."
    return a / b

def main():
    print("Calculadora básica")
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("Digite o número da operação: ")

    if escolha not in ['1', '2', '3', '4']:  # erro simples: falta ':' no final desta linha
        print("Opção inválida.")
        return

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:  # erro simples: falta ':' no final desta linha
        print("Por favor, digite um número válido.")
        return

    if escolha == '1':
        print(f"Resultado: {soma(num1, num2)}")
    elif escolha == '2':
        print(f"Resultado: {subtrai(num1, num2)}")
    elif escolha == '3':
        print(f"Resultado: {multiplica(num1, num2)}")
    elif escolha == '4':
        print(f"Resultado: {divide(num1, num2)}")

if __name__ == "__main__":
    main()