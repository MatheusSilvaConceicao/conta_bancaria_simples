# Variáveis globais usadas para armazenar informações da conta
conta = 0  # Saldo inicial da conta
extrato = []  # Lista que armazena o histórico de transações
numero_saques = 0  # Contador de saques realizados
LIMITE_SAQUE = 3  # Quantidade máxima de saques por dia
LIMITE_VALOR_SAQUE = 500.00  # Valor máximo permitido por saque

# Função responsável por realizar depósitos na conta
def deposito_conta(saldo, historico):
    deposito = float(input("QUAL VALOR VOCÊ DESEJA DEPOSITAR : "))  # Solicita o valor do depósito ao usuário
    if deposito > 0:  # Verifica se o valor do depósito é positivo
        saldo += deposito  # Adiciona o valor ao saldo
        historico.append(f"DEPÓSITO: +R$ {deposito:.2f}")  # Registra a operação no extrato
        print(f"DEPÓSITO DE R$ {deposito:.2f} REALIZADO COM SUCESSO!")
    else:
        print("DIGITE UM VALOR POSITIVO")  # Exibe mensagem de erro caso o valor seja inválido
    return saldo, historico  # Retorna o saldo atualizado e o histórico de transações
            
# Função responsável por realizar saques na conta
def saque_conta(saldo, historico, saques_realizados):
    if saques_realizados < LIMITE_SAQUE:  # Verifica se o usuário ainda pode sacar
        saque = float(input("QUAL O VALOR DO SAQUE: "))  # Solicita o valor do saque
        if saque > 0 and saque <= LIMITE_VALOR_SAQUE:  # Garante que o saque esteja dentro do limite permitido
            if saque <= saldo:  # Verifica se há saldo suficiente para o saque
                saldo -= saque  # Deduz o valor do saldo
                historico.append(f"SAQUE: -R$ {saque:.2f}")  # Registra a operação no extrato
                saques_realizados += 1  # Incrementa o contador de saques realizados
                print(f"SAQUE DE R$ {saque:.2f} REALIZADO COM SUCESSO!")
            else:
                print("SALDO INSUFICIENTE!")  # Exibe mensagem de erro caso não haja saldo suficiente
                print(f"SALDO ATUAL: R$ {conta:.2f}")  # Exibe o saldo atual
        else:
            print("LIMITE DE SAQUE: R$ 500,00")  # Mensagem de erro caso o valor do saque ultrapasse o limite
    else:
        print("VOCÊ EXCEDEU O LIMITE DE SAQUES DIÁRIOS")  # Mensagem de erro caso o usuário tente sacar mais do que o permitido
    return saldo, historico, saques_realizados  # Retorna o saldo atualizado, o histórico e o número de saques realizados
        
# Função responsável por exibir o extrato da conta               
def extrato_conta(saldo, historico):
    print("===== EXTRATO =====\n")
    if not historico:  # Verifica se houve movimentação na conta
        print("NENHUMA MOVIMENTAÇÃO")  # Exibe mensagem caso não haja transações registradas
    else:
        for movimento in historico:  # Percorre e exibe todas as transações realizadas
            print(movimento)
        print(f"\n SALDO ATUAL: R$ {conta:.2f}")  # Exibe o saldo atual da conta
    print("====================")           

# Loop principal do programa para interação com o usuário
while True:
    print('''
        
        ==== BEM VINDO ====
        [1] - DEPÓSITO
        [2] - SAQUE
        [3] - EXTRATO
        [0] - SAIR 
        ===================  
        ''')

    opcao = int(input("Digite a opção desejada : "))  # Usuário escolhe uma opção do menu

    # Verifica a opção escolhida e chama a função correspondente
    if opcao == 1:
        conta, extrato = deposito_conta(conta, extrato)  # Chama a função de depósito
    elif opcao == 2:
        conta, extrato, numero_saques = saque_conta(conta, extrato, numero_saques)  # Chama a função de saque
    elif opcao == 3:
        extrato_conta(conta, extrato)  # Chama a função de extrato
    elif opcao == 0:
        break  # Encerra o programa caso o usuário escolha sair
    else:
        print("Digite uma opção válida")  # Exibe mensagem de erro caso a opção seja inválida
