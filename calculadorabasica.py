# Programa simples de calculadora

# Pedir dois números ao utilizador
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Pedir a operação
operacao = input("Digite a operação (+, -, *, /): ")

match operacao:
    case '+':
        print("Resultado:", num1 + num2)
    case '-':
        print("Resultado:", num1 - num2)
    case '*':
        print("Resultado:", num1 * num2)
    case '/':
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Erro: divisão por zero não é permitida.")
    case _:
        print("Operação inválida!")
        
