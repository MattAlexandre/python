# nome = input("Entre com o seu nome: ")
# print(nome)

# num = int(input("Entre com um numero: "))
# print(num)

# altura = float(input("Entre com a sua altura: "))
# print(altura)

#===========================================================

# antecessor de um numero
# catando number
# number = int(input('digite um numero:  '))

# #função antecessor 
# def  ant(a):
#     ant_new = a - 1
#     print(f' o antecessor de {a} é {ant_new} ')
    
# # paassando parametros =>
# ant(number)


# --------------------------------------------------------------
# area de um retangulo

# grand = [0,0]

# x = 0
# while( x <= 1 ):
#     grand[x] = int(input(" digite as grandezas na sequencia: base  e altura:  "))
#     x += 1
    
# def area(a,b):
#     area = a * b
#     print(f' a area do retangulo com base {grand[0]} , e altura {grand[1]} é : {area}  ')

# area(grand[0],grand[1])


#-----------

# reajuste salarial

# func = [0,0]

# x = 0 
# while( x <= 1):
#     func = int(input(' digite na sequencia a seu salario e o percentual de reajuste: '))
#     x += 1
    
# def porc(a,b):
#     sal_new = a + ((a * b) / 100)
#     print(f' com o percentual de {b}% o novo salario fica: {sal_new}')
    
# porc(func[0],func[1])


#--------------------------------

# area do triangulo 

# grand = [0,0]

# x = 0 
# while( x <= 1):
#     grand[x] = int(input(' digite a base e a altura do triangulo na sequencia: '))
#     x +=1
    
# def area(a,b):
#     cal = (a * b) / 2
#     print(f' a area do triangulo com base {a} e altura {b}, é {cal}')
    
# area(grand[0],grand[1])

# --------------------------

# o produto da dos valores

# numbers = [0,0]

# while x <= 1:
#     numbers[x] = int(input(' digite um numero: '))
#     x += 1

# def prod(a,b)
#     new_prod = a * b
#     print(' a produto dos numeros {a} e {b} é: {new_prod}')


# prod(numbers[0],numbers[1])

#-------------------------------------------------

# Elabore um programa em Python que leia três notas de um aluno, calcule e
# escreva a média final deste aluno. Considerar que se trata de uma "média
# ponderada" e que os pesos das notas são 2, 3 e 5. A fórmula para o cálculo da
# média ponderada final é:

# grades = [0,0,0]

# x = 0
# while x <= 2:
#     grades[x] = int(input('digite suas notas em sequencia:  '))
#     x += 1

# def average(a,b,c):
#     average_final = ( (a * 2) + (b * 3) + (c * 5) )  / 10
#     print(f' com as notas, {a},{b}e{c}, sua nota final é: {average_final}')

# average(grades[0],grades[1],grades[2])

#-------------------------------------------------------------------

# a) Obtenha (leia) o valor para a variável HT (horas trabalhadas no mês);
# b) Obtenha o valor para a variável VH (valor hora trabalhada):
# c) Obtenha o valor para a variável PD (percentual de desconto);
# d) Calcule o salário bruto => SB = HT * VH;
# e) Calcule o total de desconto => TD = (PD/100)*SB;
# f) Calcule o salário líquido => SL = SB – TD;
# g) Apresente os valores de: Horas Trabalhadas, Salário Bruto, Total de
# Desconto e Salário Líquido.

# list[ horas trabalhadas,valor horas,porcentual]

# colaboration = [0,0,0,]
# new_salary = 0
# new_discount = 0
# new_liquid = 0

# #entrada de dados
# x = 0
# while x <= 2:
#     if(x == 0):
#         colaboration[x] = int(input('digite suas horas trabalhadas: '))
        
#     elif(x == 1):
#         colaboration[x] = int(input('digite o valor das suas  horas trabalhadas no mes: '))
        
#     else:
#        colaboration[x] = int(input('digite o valor do percentual:  '))
    
#     x += 1

# #calculo

# def salary_gross(a,b):
#     global new_salary
#     new_salary =  a * b
#     print(f' o salario bruto é: {new_salary}')

# salary_gross(colaboration[0],colaboration[1])

# #-------------

# def discount(a,b):
#     global new_discount
#     new_discount = (a / 100) * b
#     print(f' o percentual do salario  é: {new_discount}')

# discount(colaboration[2],new_salary)

# #--------------------
# def salary_liquid(a,b):
#     global new_liquid
#     new_liquid = a - b
#     print(f' o salario liquido é: {new_liquid}')

# salary_liquid(new_salary,new_discount)

# #----------------------------------------------------------------

# print('-------------------------------------------------------------------------------------------')
# print(f' vossa beldade deteve exatas  {colaboration[0]} horas trabalhadas, com total de {new_salary}R$ de salario bruto, com o desconto de {new_discount}R$ e com o salario liquido de {new_liquid}R$')


#------------------------------------------------

# Escreva um programa em Python para ler uma temperatura em graus
# Fahrenheit, calcular e visualizar o valor correspondente em graus Celsius
# (baseado na fórmula abaixo)



# temp_c = int(input('digite a temperatura em celcius:  '))


 # transform = ((9 * temp_c)/ 5) + 32


# print(' a conversão de %dº é,  %dF =>'%(temp_c,transform))


#----------------------------------------------------

# Faça um algoritmo que leia dois valores inteiros (a e b) e apresente o resultado
# do quadrado da soma dos valores lidos.


# numbers = [0,0]

# x = 0 
# while x <= 1:

#     if(x == 0):
#         numbers[x] = int(input('digite o valor de a: '))
#     else:
#         numbers[x] = int(input('digite o valor de b: '))
#     x += 1

# def cal(a,b):
#     new_cal =  (a*a) + ((a*a) + (b*b)) + (b*b)
#     print(f' o resultado da soma do quadrado de {a}  e {b} é {new_cal} =>')

# cal(numbers[0],numbers[1])

