'''
Julia é professora e precisa de um programa 
para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. 
Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual 
e retorne à idade correspondente.
'''

def calcula_idade(ano_atual, ano_nascimento):
    return ano_atual - ano_nascimento

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
print(f'A idade é {calcula_idade(ano_atual, ano_nascimento)} anos')



#Usando Lambda
#idade = lambda ano_atual, ano_nascimento: ano_atual - ano_nascimento
#print(f'A idade é {idade(ano_atual, ano_nascimento)}')