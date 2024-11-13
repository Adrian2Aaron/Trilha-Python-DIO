def menu(): #Formatando o menu
    mensagem = "Menu" 
    print(mensagem.center(39, "="))
    print("=" * 39)
    mensagem2 = "Selecione a opção desejada abaixo"
    print(mensagem2)
    
    print("=" * 39)

    opcoes = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar Novo Usuário
    [5] Cadastrar Nova Conta Bancária
    [6] Listar contas
    [0] Sair
     """
    
    print(opcoes)


def deposito(saldo, extrato, /):
    m_deposito = "DEPÓSITO" #Mensagem de deposito
    print(m_deposito.center(39, "="))
    print("=" * 39)

    valor = float(input("Insira o valor a ser depositado: R$ "))
    if valor > 0:
            saldo += valor #A variavel saldo é acrescida pelo valor inserido pelo usuario caso seja positivo
            extrato += f"Depósito R$\t{valor:.2f}\n" #E a variavel Extrato recebe yma mensagem com o valor do depósito.
            print(f"=== Deposito realizado com sucesso!\nO novo saldo é de R$ {saldo:.2f} ===\n")
    
    else: 
        print("### Operação falhou! O valor informado é inválido. ###") #Mensagem para caso o valor seja negativo ou 0
    return saldo, extrato #Retorna as variaveis alteradas


def saque(*, quant_saque, LIMITE_SAQUES, MAX_SAQUE, saldo, extrato):

    m_saque = "SAQUE" #Mensagem de saque
    print(m_saque.center(39, "="))
    print("=" * 39)

    valor = float(input("Insira o valor a ser sacado: R$ "))

    quantidade_saques = quant_saque >= LIMITE_SAQUES #Checamos se excedeu a quantidade de saques

    saldo_insuficiente = valor > saldo #Checamos se o saldo é insuficiente que esta na posição 0

    maximo_saque = valor > MAX_SAQUE #Checamos se excedeu o valor a ser sacado
    
    if quantidade_saques:
        print("### Limite diário de saques excedido. Tente novamente amanhã. ###\n\n")
    elif saldo_insuficiente:
        print("### Operação falhou! Saldo insuficiente. ###\n\n")

    elif maximo_saque:
        print("### Operação falhou! O valor do saque excede o limite permitido. ###\n\n")

    elif valor > 0:
        print("Sacando... ")
        print(f"=== Operação bem sucedida, saque de R$ {valor:.2f}, realizado com sucesso! ===\n")
        saldo -= valor #Atualizamos o valor do saldo subtraindo o valor do saque
        extrato += f"Saque R$\t{valor:.2f}\n" #Adicionamos mais uma mensagem em Extrato, detalhando o saque
        quant_saque += 1 #Atualizamos a quantidade de saques

    else:
        print("### Operação falhou! Valor de saque inválido. ###\n\n") #Mensagem para valores negativos ou iguais a 0
    
    return saldo, extrato, quant_saque #Retorna as variaveis alteradas

def exibe_extrato(saldo, / ,*, extrato): 
    m_extrato = "EXTRATO" #Mensagem de extrato
    print(m_extrato.center(39, "="))
    print("=" * 39)

    print("Não foram realizadas movimentações.\n\n" if not extrato else extrato) #Uma string vazia é considerada False
    #Se não ouver extrato exibe a mensagem acima, caso contrário exibe o extrato e a mensagem abaixo
    print(f"Saldo: R$\t{saldo:.2f}\n") #Concatenando a mensagem com o valor do saldo na posição 0

def usuario_existente(clientes, cpf):
    for usuario in clientes: #Um for que percorre a lista de clientes e compara os cpf para verificar se o cliente existe
        if usuario["cpf"] == cpf:
            return True
    return False #Caso não exista usuário com aquele cpf retorna False


def Cadastra_usuario(cliente):
    m_cliente = "CADASTRO" #Mensagem de Cadastro
    print(m_cliente.center(39, "="))
    print("=" * 39)

    print("Seja bem vindo ao cadastro de clientes!\n")
    cpf = input("Insira o CPF do usuário (Somente Números): ")
    if usuario_existente(cliente, cpf): #Verifica se o cpf já esta cadastrado
        print("### Operação encerrada. Esse CPF já está cadastrado.### \n")
        print("=" * 39)
        return #se já houver conta com esse cpf retorna ao menu

    else:
        nome = input("Insira seu nome completo: ")
        data_nasc = input("Insira sua data de nascimento no formato (dd-mm-aaaa): ")
        endereco = input("Insira seu endereço no formato(logradouro, nº - bairro - cidade/sigla  do estado): ")

    cliente.append({"nome": nome, "data_nascimento": data_nasc, "cpf": cpf, "endereco": endereco}) #Adiciona os dados na lista em forma de dicionario. Nessa versão do código não verifica se os dados batem em seus formatos, mas isso pode ser alterado em versões futuras
    print("Obrigado por seu tempo!") #Mensagem de Cadastro bem sucedido
    print(f"=== Usuário cadastrado com sucesso! Bem-vindo, {nome}. ===\n")
    print("=" * 39)
    print("\n")

def Nova_conta(AGENCIA, nro_conta, cliente):
    m_conta = "NOVA CONTA" #Mensagem de nova conta
    s_conta = "Conta cadastrada com Sucesso!" #Mensagem de Sucesso
    print(m_conta.center(39, "="))
    print("=" * 39)
    print("Seja bem vindo ao cadastro de contas!\n")

    cpf = input("Insira o CPF do usuário: ")
    for clientes in cliente: 
        if usuario_existente(cliente, cpf): #Verifica se já existe cliente com esse cpf
            print(s_conta.center(39, "="))#Mensagem de sucesso na criação de conta
            print("\n")
            return {"agencia": AGENCIA, "nro_conta": nro_conta, "usuario": clientes} #Retorna os dados da conta
    
    print("### Cliente não encontrado! Tente Novamente!### \n") #Mensagem caso não encontre usuário com aquele CPF
    print("=" * 39)
        
def Listar_contas(contas):
    m_listar = "CONTAS" #Mensagem de para as Contas
    print(m_listar.center(39, "="))
    print("=" * 39)

    print("Aqui estão as contas cadastradas!\n")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['nro_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 39)
        print(linha)

def main():
    #Declarando variaveis que serão usadas no bloco de código
    LIMITE_SAQUES = 3
    MAX_SAQUE = 500
    AGENCIA = "0001"
    quant_saque = 0
    numero_saques = 0
    extrato = ""
    cliente = []
    contas = []
    saldo = 0


    while True:
       menu() #Executa o menu, e exibe suas mensagens
       opcao = input("=> ") #Entrada da opção escolhida pelo usuario
       
       match opcao: #match é semelhante ao switch em C ou C++.
        case '1': #Depósito
            saldo, extrato = deposito(saldo, extrato) #Executa a função de deposito, e atualiza variaveis com o retorno
            
        case '2': #Saque
            saldo, extrato, quant_saque = saque(quant_saque = quant_saque, LIMITE_SAQUES = LIMITE_SAQUES, MAX_SAQUE = MAX_SAQUE, saldo = saldo, extrato = extrato) #Executa a função de Saque
            #E armazena atualiza a quantidade de saques com o retorno da função

        case '3': #Extrato
            exibe_extrato(saldo, extrato=extrato) #Executa a função de Extrato
        
        case '4': #Cadastrar novo usuario.
               Cadastra_usuario(cliente) #Executa o cadastro de Clientes e atualiza a lista de clientes
        
        case '5': #Criar novas Contas.
               nro_conta = len(contas) + 1  #Atualiza o numero das contas
               conta = Nova_conta(AGENCIA, nro_conta, cliente) #Atualiza conta com a função nova conta

               if conta: #Variavel vazia é igual a False, então criar uma conta com sucesso adiciona a lista de dicionarios na lista Conta
                   contas.append(conta)
        
        case '6': #Listar contas existentes.
               Listar_contas(contas)

        case '0':
            print("Obrigado por utilizar nossos serviços\n")
            break #Encerra o programa com o Break

        case _:
            print("Opção inválida. Tente novamente.\n")
            #retorna ao menu normalmente

main()

