def soma_todos(*numeros):
    return sum(numeros)
def exibir_dados(**dados):
    for chave, valor in dados.items():
        print(f'{chave.capitalize()}): {valor}') 
exibir_dados( nome = 'João', idade = '20', cidade = 'Sorocaba')

