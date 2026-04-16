'''
Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para
 aplicar diferentes taxas de desconto sobre os valores das compras.

Diante deste problema, crie uma closure que gere uma função capaz 
de calcular o preço final com um desconto fixo definido pelo usuário.
'''

desconto = int(input('Digite a porcentagem de desconto: \n'))

valor = int(input('Digite o valor da compra:\n'))


def criar_desconto(desconto):
    def calcular(valor):
        return valor - (valor * desconto / 100)
    return calcular

valor_final = criar_desconto(desconto)
print(valor_final(valor))
