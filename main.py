# Sistema Bancário simples

# Implementar 3 operações: depósito, saque(máximo 3 operações diárias, e valor limite de 500,00 reais), extrato(registro de todas as operaç~eos de depósito e saque).

menu = """
[1] Deposito
[2] Saque
[3] Extrato
[4] Sair
"""
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)

  if opcao == '1':
    valor = float(input('informe o valor do depósito: '))

    if valor > 0:
        saldo += valor
        extrato += f'Depósito : R$ {valor:2f}\n'

    else: 
        print('Operação falhou! O valor informado é inválido.')

  elif opcao == '2':
    valor = float(input('informe o valor do saque: '))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print('Operação falhou! Não há saldo sufuciente.')

    elif excedeu_limite:
        print('Operação falhou! O valor do saque excede o limite.')

    elif valor > 0:
        saldo -= valor
        extrato += f'saque: R$ {valor:.2f}\n'
        numero_saques += 1

    else:
        print('Operação falhou! Valor informado inválido.')

  elif opcao == '3':
    print('-------------EXTRATO---------------')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nsaldo: R$ {saldo:.2F}')
    print('-----------------------------------')

  elif opcao == '4':
    break
        
  else:
    print('Operação inválida, selecione novamente o peração: ')