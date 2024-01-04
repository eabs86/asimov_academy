
import os


carros =[("Nissan Kicks",300),
        ("Toyota Camry",300),
        ("Honda Civic",400),
        ("Hyundai Elantra",400),
        ("Fiat Mobi",200),
        ("Chevrolet Tracker",300)]
alugados =[]

def boas_vindas():
    print("=========")
    print("Seja bem vindo a AluCar!")
    print("=========")

def print_lista_carros(lista_carros):
    for i,car in enumerate(lista_carros):
        print(f"[{i+1}] - {car[0]} - R${car[1]}/dia")

def print_alugados(lista_alugados):
    for i,car in enumerate(lista_alugados):
        print(f"[{i+1}] - {car[0]} - R${car[1]}/dia")

while True:
    os.system("cls")
    boas_vindas()
    print("O que deseja fazer?")
    print("0 - Mostrar Portfólio | 1 - Alugar | 2 - Devolver | 3 - Sair")
    op = int(input("Digite a opção:"))
    while op not in (0, 1, 2, 3):
        print("Opção inválida. Tente novamente.")
        op = int(input("Digite a opção:"))

    if op == 3:
        os.system("cls")
        print("===========================")
        print("Obrigado por usar o AluCar!")
        print("===========================")
        break
    elif op == 0:
        print("Portfólio:")
        print("=====================")
        print("Carros disponíveis:")
        print_lista_carros(carros)
        print("=====================")
        print("Carros alugados:")
        print_alugados(alugados)
    elif op == 1:
        print("Alugar:")
        print_lista_carros(carros)
        print("=====================")
        print("Qual carro deseja alugar?")
        op = int(input("Digite o número:"))

        print("Por quantos dias você deseja alugar?")
        dias = int(input("Digite o número de dias:"))
        
        print(f"Você está alugando o carro {carros[op-1][0]} por {dias} dias. O valor total ficaria em R${carros[op-1][1]*dias}.")
        print("Deseja confirmar o aluguel? 0 - SIM | 1 - NÃO")
        if int(input())==0:
            alugados.append(carros[op-1])
            carros.pop(op-1)
            print("Aluguel efetuado com sucesso!")
            
    elif op == 2:
        if len(alugados)==0:
            print("Nenhum carro alugado. Tente novamente.")
            print("=====================")
        else:
            print("Lista de carros alugados:")
            print_alugados(alugados)
            print("=====================")
            print("Qual carro deseja devolver?")
            op = int(input("Digite o número:"))
            print("Deseja confirmar a devolução? 0 - SIM | 1 - NÃO")
            if int(input())==0:
                carros.append(alugados[op-1])
                alugados.pop(op-1)
                print("Devolução efetuada com sucesso!")

    
    print("")
    print("==============")
    print("0 para continuar | 3 para SAIR")
    if int(input())==3:
        os.system("cls")
        print("===========================")
        print("Obrigado por usar o AluCar!")
        print("===========================")
        break

