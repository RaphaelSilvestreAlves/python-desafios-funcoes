'''
Joana está participando de um processo seletivo para uma vaga de desenvolvedora 
e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.

Sua tarefa é criar um programa usando funções lambda que receba dois números
 e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.
'''

soma = lambda x, y: x + y
subtracao = lambda x, y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x, y: x / y if y != 0 else 'Erro: Divisão por zero'

x = int(input('Digite o primeiro número:'))   
y = int(input('Digite o segundo número:'))
operacao = input('Escolha a operação (| + | - | * | / |):  ')

operacoes = {
    '+':soma,
    '-':subtracao,
    '*':multiplicacao,
    '/':divisao
    }

if operacao in operacoes:
    resultado = operacoes[operacao](x,y)
    print(f'O resultado é: {resultado}')
else:
    print('Operação inválida')

# if operacao == '+': 
#     print(f'A soma é {soma(x, y)}')
# elif operacao == '-': 
#     print(f'A subtração é {subtracao(x, y)}')
# elif operacao == '*': 
#     print(f'A multiplicação é {multiplicacao(x, y)}')
# elif operacao == '/': 
#     print(f'A divisão é {divisao(x, y)}')
# else:
#     print('Operação inválida')