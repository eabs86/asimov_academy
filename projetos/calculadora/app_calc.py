import os

print("=========")

operacoes ={
    "+": "Soma",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão",
    "^": "Exponenciação",
    "r": "Raiz Quadrada"       
}
sair = "N"
while True:
    os.system('cls')
    print("=========")
    for op,name in operacoes.items():
        print(f"{op} - {name}")
    print("Q - Sair")
    operacao = input("Digite a operação desejada: ")
    if (operacao == "Q"):
        break

    while operacao not in operacoes:
        operacao = input("Operação inválida. Digite a operação desejada:")
    if operacao=="+":
        print("Você escolheu Soma!")
        parcela1 = float(input("Digite a primeira parcela: "))
        parcela2 = float(input("Digite a segunda parcela: "))
        resultado = parcela1 + parcela2
        print(f"O resultado é: {resultado}")
        print("\n --------------------------")
        sair = input("\nDeseja Realizar outra operação? Digite Q para Sair ou N para nova operação: ")
        if sair =="Q" or sair =='q':
            break
    elif operacao=="-":
        print("Você escolheu Subtração!")
        parcela1 = float(input("Digite a primeira parcela: "))
        parcela2 = float(input("Digite a segunda parcela: "))
        resultado = parcela1 - parcela2
        print(f"O resultado é: {resultado}")
        sair = input("\nDeseja Realizar outra operação? Digite Q para Sair ou N para nova operação: ")
        if sair =="Q" or sair =='q':
            break
    elif operacao=="*":
        print("Você escolheu Multiplicação!")
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))
        resultado = numero1 * numero2
        print(f"O resultado é: {resultado}")
        sair = input("\nDeseja Realizar outra operação? Digite Q para Sair ou N para nova operação: ")
        if sair =="Q" or sair =='q':
            break
    elif operacao=="/":
        print("Você escolheu Divisão!")
        numero1 = float(input("Digite o primeiro numero: "))
        numero2 = float(input("Digite o segundo numero: "))
        resultado = numero1 / numero2
        print(f"O resultado é: {resultado}")
        sair = input("\nDeseja Realizar outra operação? Digite Q para Sair ou N para nova operação: ")
        if sair =="Q" or sair =='q':
            break
    elif operacao=="^":
        print("Você escolheu Exponenciação!")
        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))
        resultado = base ** expoente
        print(f"O resultado é: {resultado}")
        sair = input("\nDeseja Realizar outra operação? Digite Q para Sair ou N para nova operação: ")
        if sair =="Q" or sair =='q':
            break
    elif operacao=="r":
        print("Você escolheu Raiz Quadrada!")
        numero = float(input("Digite o numero: "))
        resultado = numero ** (1/2)
        print(f"O resultado é: {resultado}")
        sair = input("\nDeseja Realizar outra operação? Digite Q para Sair ou N para nova operação: ")
        if sair =="Q" or sair =='q':
            break
        