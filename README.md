# Sistema Bancário Simples em Python

Este projeto implementa um **sistema bancário simples** utilizando a linguagem de programação **Python**. O sistema permite que o usuário realize operações básicas, como **depósitos**, **saques** e consulte o **extrato** da sua conta bancária. Além disso, o sistema controla o número de saques diários e o valor máximo permitido por transação.

## Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação utilizada no desenvolvimento do sistema.

## Estrutura do Código

O código está estruturado da seguinte forma:

- **Variáveis Globais**:
  - `conta`: Armazena o saldo atual da conta bancária.
  - `extrato`: Lista que mantém o histórico de transações realizadas.
  - `numero_saques`: Contabiliza o número de saques realizados no dia.
  - `LIMITE_SAQUE`: Define o número máximo de saques permitidos por dia.
  - `LIMITE_VALOR_SAQUE`: Estabelece o valor máximo permitido por transação de saque.

- **Funções**:
  - `deposito_conta(saldo, historico)`: Solicita ao usuário um valor para depósito, valida a entrada e atualiza o saldo e o histórico de transações.
  - `saque_conta(saldo, historico, saques_realizados)`: Permite ao usuário realizar um saque, verificando limites diários e valores máximos, e atualiza o saldo, histórico e contador de saques.
  - `extrato_conta(saldo, historico)`: Exibe o histórico completo de transações e o saldo atual da conta.

- **Loop Principal**:
  - Apresenta um menu de opções ao usuário e direciona para a função correspondente com base na escolha.

## Funcionalidades do Sistema

- **Depósito**:
  - Permite ao usuário adicionar um valor positivo ao saldo da conta.
  - Valida se o valor informado é positivo antes de realizar a operação.
  - Registra a transação no histórico com a descrição "DEPÓSITO".

- **Saque**:
  - Permite ao usuário retirar um valor do saldo, respeitando o limite diário de saques e o valor máximo por transação.
  - Verifica se o número de saques diários não foi excedido.
  - Confirma se o saldo é suficiente para cobrir o valor do saque.
  - Registra a transação no histórico com a descrição "SAQUE".

- **Extrato**:
  - Exibe todas as transações realizadas, incluindo depósitos e saques.
  - Mostra o saldo atual da conta após todas as operações.
  - Informa se não houve movimentações na conta.

## Exemplo de Uso

Ao executar o sistema, o usuário será apresentado ao seguinte menu:

```
==== BEM VINDO ====
[1] - DEPOSITO
[2] - SAQUE
[3] - EXTRATO
[0] - SAIR
==================
```

- **Para realizar um depósito**:
  - Selecione a opção `[1] - DEPOSITO`.
  - Informe o valor que deseja depositar.
  - O sistema confirmará o depósito e atualizará o saldo.

- **Para realizar um saque**:
  - Selecione a opção `[2] - SAQUE`.
  - Informe o valor que deseja sacar.
  - O sistema verificará se o saque é permitido e, em caso afirmativo, processará a transação.

- **Para consultar o extrato**:
  - Selecione a opção `[3] - EXTRATO`.
  - O sistema exibirá o histórico de transações e o saldo atual.

- **Para encerrar o sistema**:
  - Selecione a opção `[0] - SAIR`.

## Exemplo de Execução

```
==== BEM VINDO ====
[1] - DEPOSITO
[2] - SAQUE
[3] - EXTRATO
[0] - SAIR
==================
Digite a opção desejada : 1
QUAL VALOR VOCÊ DESEJA DEPOSITAR : 100
DEPÓSITO DE R$ 100.00 REALIZADO COM SUCESSO!

==== BEM VINDO ====
[1] - DEPOSITO
[2] - SAQUE
[3] - EXTRATO
[0] - SAIR
==================
Digite a opção desejada : 2
QUAL O VALOR DO SAQUE: 50
SAQUE DE R$ 50.00 REALIZADO COM SUCESSO!

==== BEM VINDO ====
[1] - DEPOSITO
[2] - SAQUE
[3] - EXTRATO
[0] - SAIR
==================
Digite a opção desejada : 3
===== EXTRATO =====

DEPÓSITO: +R$ 100.00
SAQUE: -R$ 50.00

SALDO ATUAL: R$ 50.00
====================
```
