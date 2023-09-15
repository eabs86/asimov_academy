print("====== Bem vindo a Calculadora Raiz =====")

def menu():
    print("\nOpções de Operações:")
    print("------------------------")
    print("0 - Soma")
    print("1 - Subtração")
    print("2 - Multiplicação")
    print("3 - Divisão")
    print("4 - Exponenciação")
    print("5 - Raiz Quadrada")
    print("------------------------\n")
    operacao = int(input("Digite a operação desejada:"))

    while operacao not in [0,1,2,3,4,5]:
        operacao = int(input("Operação inválida. Digite a operação desejada:"))
        
    return operacao


sair = "N"


while sair == "N":
    operacao = menu()

    if operacao == 0:
        print("\nVocê escolheu Soma!\n")
        parcela1 = float(input("Digite a primeira parcela:"))
        parcela2 = float(input("Digite a segunda parcela:"))
        resultado = parcela1 + parcela2
        print(f"O resultado é: {resultado}")
        sair = input("\nDigite S para sair ou N para realizar nova operação:")

    elif operacao == 1:
        print("\nVocê escolheu Subtração!\n")
        parcela1 = float(input("Digite a primeira parcela:"))
        parcela2 = float(input("Digite a segunda parcela:"))
        resultado = parcela1 - parcela2
        print(f"O resultado é: {resultado}")
        sair = input("\nDigite S para sair ou N para realizar nova operação:")

    elif operacao == 2:
        print("\nVocê escolheu Multiplicação!\n")
        numero1 = float(input("Digite o primeiro numero:"))
        numero2 = float(input("Digite o segundo numero:"))
        resultado = numero1 * numero2
        print(f"O resultado é: {resultado}")
        sair = input("\nDigite S para sair ou N para realizar nova operação:")

    elif operacao == 3:
        print("\nVocê escolheu Divisão!\n")
        numero1 = float(input("Digite o primeiro numero:"))
        numero2 = float(input("Digite o segundo numero:"))
        resultado = numero1 / numero2
        print(f"O resultado é: {resultado}")
        sair = input("\nDigite S para sair ou N para realizar nova operação:")

    elif operacao == 4:
        print("\nVocê escolheu Exponenciação!\n")
        base = float(input("Digite a base:"))
        expoente = float(input("Digite o expoente:"))
        resultado = base ** expoente
        print(f"O resultado é: {resultado}")
        sair = input("\nDigite S para sair ou N para realizar nova operação:")

    elif operacao == 5:
        print("\nVocê escolheu Raiz Quadrada!\n")
        numero = float(input("Digite o numero:"))
        resultado = numero ** (1/2)
        print(f"O resultado é: {resultado}")
        sair = input("\nDigite S para sair ou N para realizar nova operação:")
