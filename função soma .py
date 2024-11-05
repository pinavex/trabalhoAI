# Função para soma
def soma(x, y):
    return x + y

# Função para subtração
def subtracao(x, y):
    return x - y

# Função para multiplicação
def multiplicacao(x, y):
    return x * y

# Função para divisão
def divisao(x, y):
    return x // y if y != 0 else "Erro: divisão por zero."

# Função para solicitar um número com validação
def solicitar_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: Digite um número válido.")

# Função principal
def calculadora():
    while True:
        op = input("\nEscolha a operação (soma, sub, mult, div): ")
        if op not in ["soma", "sub", "mult", "div"]:
            print("Digite operação válida")
            continue

        num1 = solicitar_numero("Digite o primeiro número: ")
        num2 = solicitar_numero("Digite o segundo número: ")

        if op == "soma":
            result1 = soma(num1, num2)
            conta = str(num1) + " + " + str(num2) + " = " + str(result1)
            print("Resultado da soma: " + conta)

        elif op == "sub":
            result2 = subtracao(num1, num2)
            conta = str(num1) + " - " + str(num2) + " = " + str(result2)
            print("Resultado da subtração: " + conta)

        elif op == "mult":
            result3 = multiplicacao(num1, num2)
            conta = str(num1) + " * " + str(num2) + " = " + str(result3)
            print("Resultado da multiplicação: " + conta)

        elif op == "div":
            if num2 == 0:
                print("Erro: divisão por zero não permitida.")
            else:
                result4 = divisao(num1, num2)
                conta = str(num1) + " / " + str(num2) + " = " + str(result4)
                print("Resultado da divisão: " + conta)

# Executa a calculadora
calculadora()
            
