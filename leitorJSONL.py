import json, csv

print('INICIANDO LEITOR DE JSONL...\n')
busca = input('Digite o caminho completo do arquivo que deseja ler (incluindo a extensao): ')
tipoBusca = input('Digite 1 para buscar por NOME ou 2 para buscar por CPF: ')

with open(busca, 'r') as json_file:
    json_list = list(json_file)

pre_resultado={}
resultado = ()
pos_resultado = []

if (tipoBusca == '1'):
    nome = input('Digite o nome da pessoa que está buscando: ')
    for json_str in json_list:
        pre_resultado = json.loads(json_str)
        if (pre_resultado['nome'] == nome or pre_resultado['nome'] == nome.upper() or pre_resultado['nome'] == nome.lower() or pre_resultado['nome'] == nome[0].upper() +nome[1:]):
            resultado = (pre_resultado['nome'], pre_resultado['cpf'])
            pos_resultado.append(resultado)
    print('Resultado da busca por: ', nome)
    if (len(pos_resultado)==0):
        print('Nenhum resultado encontrado')
    else: 
        print("Resposta (NOME/CPF): ", pos_resultado)
if (tipoBusca == '2'):
    cpf = input('Digite apenas os números do CPF, sem espaços: ')
    for json_str in json_list:
        pre_resultado = json.loads(json_str)
        if (pre_resultado['cpf'] == cpf):
            resultado = (pre_resultado['nome'], pre_resultado['cpf'])
            pos_resultado.append(resultado)
    print('Resultado da busca por: ', cpf)
    if (len(pos_resultado)==0):
        print('Nenhum resultado encontrado')
    else: 
        print("Resposta (NOME/CPF): ", pos_resultado)
else:
    print('Resposta inválida. Digite Nome ou CPF para determinar qual o tipo de busca. Por favor reinicie o programa e tente novamente.')

print('FIM DO PROGRAMA!')






