## Exercícios #1 - Estruturas de dados

### Exercício 1
# Utilizando o built-in method input(), crie um programa que receba a altura e o peso de uma pessoa e imprima na tela o IMC da mesma.

peso = input("Digite o seu peso (em kg e separado por '.'):")
altura = input("Digite a sua altura (em cm):")

peso_float = float(peso)
altura_float = float(altura)

imc = peso_float/(altura_float/100)**2

print(f'Seu IMC é de {imc}')

### Exercício 2 
# Escreva um programa que pergunte o nome completo do usuário e cumprimente o mesmo pelo primeiro nome.

nome = input("Escreva seu nome completo separado por espaços:")

nome_separados = nome.split()
primeiro_nome = nome_separados[0];
print(f"Seja bem vindo {primeiro_nome}!")


# ### Exercício 3
# Desenho um código que extraia o domínio de um e-mail informado.

email = input("Digite o seu email:")

email_separado = email.split("@")
dominio_separado = email_separado[1].split(".")
dominio = dominio_separado[0]

print(f'O domínio do seu email é: {dominio}')

### Exercício 4 
# Faça um programa para uma loja de tintas. 
# A pessoa informa a área em m2 que deseja pintar,
# e o script calculará a quantidade de latas de tinta que a pessoa deve comprar e o valor. 
# Considere que cada litro de tinta pinta 3m2,
# que cada lata contém 18L e que custa R$ 80.

from math import ceil 

area = input("Informe a área em m2 que você deseja pintar:")
FATOR_LITRO_TINTA = 3
qtdade_litros = float(area)/FATOR_LITRO_TINTA
VOLUME_LATA = 18
qtdade_latas = ceil(qtdade_litros/VOLUME_LATA)
PRECO_LATA_18L = 80

custo = qtdade_latas*PRECO_LATA_18L

print(f'Para pintar uma área de {area} m2 você precisará de {qtdade_latas} latas, que custara R${custo}')

# ### Exercício 5
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# 1. Salário bruto.
# 2. Quanto pagou ao INSS.
# 3. Quanto pagou ao sindicato.
# 4. O salário líquido.

salario_bruto = input("Informe o seu salário bruto em reais:")
salario_base = float(salario_bruto)
irpf = salario_base*(0.11)
inss = salario_base*(0.08)
sindicato = salario_base*(0.05)
salario_liquido = salario_base - irpf - inss - sindicato

print('Demonstrativo do seu salário:')
print(f'Salário Bruto:\t\t R${salario_base}')
print(f'Desconto do IRPF (11%):\t - R${irpf}')
print(f'Desconto do INSS (8%):\t - R${inss}')
print(f'Desconto do sindicato (5%):\t -R${sindicato}')
print("                     ____________________")
print(f"Seu salário liquido: \t R${salario_liquido}")
