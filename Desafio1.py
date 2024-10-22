def menu(): #Formatando o menu
    mensagem = "Menu" 
    print(mensagem.center(34, "="))
    print("=" * 34)
    mensagem2 = "Selecione a opção desejada abaixo"
    print(mensagem2)
    
    print("=" * 34)

    opcoes = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
     """
    
    print(opcoes)



def deposito(novo_saldo):
    m_deposito = "DEPÓSITO" #Mensagem de deposito
    print(m_deposito.center(34, "="))
    print("=" * 34)
    valor = float(input("Insira o valor a ser depositado: R$ "))
    if valor > 0: #Aqui iremos usar uma lista para manipular os valores, por serem mutaveis globais
            novo_saldo[0] += valor #A posição 0 armazena o saldo
            novo_saldo[1] += valor #A posição 1 armazena se houve deposito
            print(f"Deposito realizado com sucesso!\nO novo saldo é de R$ {novo_saldo[1]:.2f}\n")
    
    else: 
        print("Valor invalido!")


def saque(quant_saque, LIMITE_SAQUES, MAX_SAQUE, novo_saldo):

    m_saque = "SAQUE" #Mensagem de saque
    print(m_saque.center(34, "="))
    print("=" * 34)

    valor = float(input("Insira o valor a ser sacado: R$ "))

    quantidade_saques = quant_saque >= LIMITE_SAQUES #Checamos se excedeu a quantidade de saques

    saldo_insuficiente = valor > novo_saldo[0] #Checamos se o saldo é insuficiente que esta na posição 0

    maximo_saque = valor > MAX_SAQUE #Checamos se excedeu o valor a ser sacado
    
    if quantidade_saques:
        print("Limite diário de saque excedido\n\n")
    elif saldo_insuficiente:
        print("Operação falhou! Saldo insuficiente!\n\n")

    elif maximo_saque:
        print("Transação não concluída! Valor de saque acima do permitido!\n\n")

    elif valor > 0:
        print("Sacando... ")
        print(f"Operação bem sucedida, saque de R$ {valor:.2f}, realizado com sucesso!\n")
        novo_saldo[0] -= valor #Atualizamos o valor do saldo na posição 0
        novo_saldo[2] += valor #Adicionamos o valor de saques na posição 2 para o extrato
        quant_saque += 1 #Atualizamos a quantidade de saques

    else:
        print("Valor inserido inválido!\n\n")
    
    return quant_saque

def extrato(novo_saldo):
    m_extrato = "EXTRATO" #Mensagem de extrato
    print(m_extrato.center(34, "="))
    print("=" * 34)
    if novo_saldo[1] == 0.0: #Se não houve deposito que fica na posição 1, então não ha movimentação
        print("Não foram realizadas movimentações!\n\n")
    else:
        print(f"Depósito: R$ {novo_saldo[1]:.2f}\n") #Concatenando a mensagem com o valor do deposito na posição 1
        if novo_saldo[2] != 0.0:
            print(f"Saque: R$ {novo_saldo[2]:.2f}") #Concatenando a mensagem com o valor do saque na posição 2

        print(f"\nSaldo: R$ {novo_saldo[0]:.2f}\n\n") #Concatenando a mensagem com o valor do saldo na posição 0

def main():
    #Declarando variaveis que serão usadas no bloco de código
    LIMITE_SAQUES = 3
    MAX_SAQUE = 500
    quant_saque = 0
    novo_saldo = [0.0, 0.0, 0.0] #Criando a lista que irá armazenar os valores e preenchendo com 0.0 para fazer operações

    while True:
       menu() #Executa o menu, e exibe suas mensagens
       opcao = input("=> ") #Entrada da opção escolhida pelo usuario
       
       match opcao: #match é semelhante ao switch em C ou C++.
        case '1':
            deposito(novo_saldo) #Executa a função de deposito
            
        case '2':
            quant_saque = saque(quant_saque, LIMITE_SAQUES, MAX_SAQUE, novo_saldo) #Executa a função de Saque
            #E armazena atualiza a quantidade de saques com o retorno da função

        case '3':
            extrato(novo_saldo) #Executa a função de Extrato

        case '0':
            print("Obrigado por utilizar nossos serviços\n")
            break #Encerra o programa com o Break

        case _:
            print("Opção inválida. Tente novamente.\n")
            #retorna ao menu normalmente

main()
