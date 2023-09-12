"""
Exercicio 1: 
Programa para leitura de 2 notas parciais de um aluno.

"""

def media_notas(nota1, nota2):
    media = (float(nota1) + float(nota2))/2
    if media>=7:
        if media==10:
            print("Aprovado com Distinção!")
        else:
            print("Aluno aprovado!")
    elif media<7:
        print("Aluno reprovado!")
    
    return media

media_notas(5, 7)


"""
Exercício 2:

Escrever um script que ler 3 números e mostra o maior e o menor deles

"""

def min_max(num1,num2,num3):
    lista = [num1,num2,num3]
    lista.sort()
    print(f"Menor: {lista[0]}")
    print(f"Maior: {lista[-1]}")

min_max(3,7,2)


"""
Exercício 3:

Nome na vertica e em escada

"""

def nome_escada(nome):
    for i in range(1, len(nome)+1):
        print(nome[:i])
        
nome_escada("Emmanuel")


"""
Exercício 4:

Gerando uma série de Fibonacci

"""

def serie_fibonacci(numero_maximo):
    lista = [0,1]
    while lista[-1] < numero_maximo:
        lista.append(lista[-1] + lista[-2])
    print(lista)
    
serie_fibonacci(100)

"""
Exercício 5:

Validador de informações

"""