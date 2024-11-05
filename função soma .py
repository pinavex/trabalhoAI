# Função para soma
def soma(x, y):
    return x + y

# Função para subtração
def subtração(x, y):
    return x - y

# Função para multiplicação
def multiplicação(x, y):
    return x * y

# Função para divisão
def divisão(x, y):
    return x / y

# Função para solicitar um número com validação
def solicitar_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))  # Permite entrada de números decimais
        except ValueError:
            print("Erro: Digite um número válido.")

# Função principal
def calculadora():
    # Lista histórico
    historico = []
    while True:
        op = input("\n soma, sub, mult, div, hist \n Digite operação: ")
        if op not in ["soma", "sub", "mult", "div", "hist"]:
            print("Digite operação válida")
            continue

        if op != "hist":
            num1 = solicitar_numero("Digite o primeiro número: ")
            num2 = solicitar_numero("Digite o segundo número: ")

            if op == "soma":
                result1 = soma(num1, num2)
                conta = str(num1) + " + " + str(num2) + " = " + str(result1)
                historico.append(conta)
                print("Resultado da soma: " + conta)

            elif op == "sub":
                result2 = subtração(num1, num2)
                conta = str(num1) + " - " + str(num2) + " = " + str(result2)
                historico.append(conta)
                print("Resultado da subtração: " + conta)

            elif op == "mult":
                result3 = multiplicação(num1, num2)
                conta = str(num1) + " * " + str(num2) + " = " + str(result3)
                historico.append(conta)
                print("Resultado da multiplicação: " + conta)
                if num1 == num2:
                    print(str(num1) + "^2 = " + str(result3))

            elif op == "div":
                if num2 == 0:
                    print("Erro: divisão por zero não permitida.")
                else:
                    result4 = divisão(num1, num2)
                    conta = str(num1) + " / " + str(num2) + " = " + str(result4)
                    historico.append(conta)
                    print("Resultado da divisão: " + conta)

        if op == "hist":
            print("Histórico: " + str(historico))

# Executa a calculadora
calculadora()
