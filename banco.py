import datetime

Usuarios = [{"idusuario": 0 , "email": "" ,"senha" : "" , "cpf": "" , "nome": "" , "data_nascimento" : ""}]
Contas = [{"numero": 0 , "agencia" : "" ,"saldo" : 0 , "limite_saque" : 500 , "extrato" : "","id_usuario" : 0 }]
Enderecos = [{"idendereco": 0 ,"rua": "" , "numero": "" , "bairro": "" , "cidade": "" , "estado" : ""  , "id_usuario" : 0 }]


def cadastrar_usuario(p_email,p_senha,p_cpf,p_nome,p_data_nascimento ,/,*,p_tabela ):
    Usuario = {"idusuario": 0 ,"email": p_email ,"senha": p_senha , "cpf": p_cpf , "nome": p_nome , "data_nascimento" : p_data_nascimento}
    Usuario["idusuario"] = p_tabela[-1]["idusuario"] + 1
    return Usuario
def cadastrar_endereco(p_rua,p_numero,p_bairro,p_cidade,p_estado,p_id_usuario ,/,*,p_tabela):
    endereco = {"idendereco": 0 ,"rua": p_rua , "numero": p_numero , "bairro": p_bairro , "cidade": p_cidade , "estado" : p_estado  , "id_usuario" : p_id_usuario }
    endereco["idendereco"] = p_tabela[-1]["idendereco"] + 1
    return endereco
def cadastrar_conta(p_idusuario ,/,*,p_tabela):
     conta = {"numero": 0 , "agencia" : "0001" ,"saldo" : 0 , "limite_saque" : 500 , "extrato" : "","id_usuario" : p_idusuario }
     conta["numero"] = p_tabela[-1]["numero"] + 1
     return conta


def interface_de_cadastro(*, p_Usuarios , p_Enderecos):

    
    email_invalido = True
    cpf_invalido = True

    nome = input("insira seu nome : ")

    while (email_invalido == True) :
        email = input("insira um email : ")
        
        email_invalido = False
        for usuario in p_Usuarios:
            if(usuario["email"] == email):
                email_invalido = True
                print("email ja utilizado , porfavor tente novamente com outro email")
                break
    
    senha = input("escolha uma senha : ")

    while (cpf_invalido == True):
        cpf = input("insira seu cpf : ")

        cpf_invalido = False
        for usuario in p_Usuarios:
            if(usuario["cpf"] == cpf):
                cpf_invalido = True
                print("cpf ja utilizado , porfavor tente novamente com outo cpf")
                break

    data_nascimento = input("insira sua data de nascimento no modelo dd/mm/aaaa : ")

    p_Usuarios.append(cadastrar_usuario(email,senha,cpf,nome,data_nascimento , p_tabela = p_Usuarios))


    print("informe seu local de residencia")
    rua = input("rua: ")
    numero = input("numero: ")
    bairro = input("bairro: ")
    cidade = input("cidade: ")
    estado = input("estado: ")
    p_Enderecos.append(cadastrar_endereco (rua,numero,bairro,cidade,estado, p_Usuarios[-1]["idusuario"] , p_tabela = p_Enderecos))

def logar(p_Usuarios):
    id_usuario = 0
    email = input("porfavor informe o email de seu usuario : ")
    senha = input("porfavor informe a senha do seu usuario : ")
    cpf = input("porfavor informe seu cpf : ")

    usuario_correto = False

    for usuario in p_Usuarios:
        if (usuario["email"] == email and usuario["senha"] == senha and usuario["cpf"] == cpf ):
            usuario_correto = True
            id_usuario = usuario["idusuario"]
            break
    
    if (usuario_correto == True):
        return id_usuario
    else:
        print ("#login incorreto\n")
        return 0
def selecionar_conta(p_id_usuario, tabela_Contas):
    usuario_contas = []
    for conta in tabela_Contas:
        if(conta["id_usuario"] == p_id_usuario):
            usuario_contas.append(conta)
    
    i = 0
    for conta in usuario_contas:
        i += 1
        print(f"{i} - numero: {conta['numero']} agencia: {conta['agencia']}  saldo: {conta['saldo']}")
  
    escolha = -1
    while escolha > i or escolha <= 0 :
        escolha = int(input(" escolha uma das contas\n"))


    print(f" selecionado - > {escolha} - numero: {usuario_contas[escolha - 1]['numero']} agencia: {usuario_contas[escolha - 1]['agencia']}  saldo: {usuario_contas[escolha - 1]['saldo']}")

    return usuario_contas[escolha - 1]["numero"]



def interface_cadastro_conta(p_Contas , p_Usuarios):
    id_usuario = 0
    id_usuario = logar(p_Usuarios)
    
    conta = {}
    if(id_usuario != 0):
        print("informaçoes de usuario corretas")
        print("criando conta...")
        conta = cadastrar_conta(id_usuario, p_tabela = p_Contas)
        p_Contas.append(conta)
        print("conta criada com sucesso")
        print( 
            f"""numero da conta: {conta['numero']} ,agencia: {conta['agencia']}.
proprietario da conta : {p_Usuarios[conta['id_usuario']]['nome']} , cpf : {p_Usuarios[conta['id_usuario']]['cpf']}, email : {p_Usuarios[conta['id_usuario']]['email']} """)
    else:
        print("informaçoes de usuario incorretas , porfavor tente novamente ")


Usuarios.append( cadastrar_usuario("ruanlourencosilva.rj@gmail.com", "umasenha_ai", "19516113737" , "ruan" , "25/06/2001" , p_tabela= Usuarios) )
Usuarios.append( cadastrar_usuario("tretakezica@gmail.com", "1234a_melhor_senha_do_mundo", "999999999" , "tretake" , "01/12/2011" , p_tabela= Usuarios) )





#adicionar conta["extrato"] , conta["saldo"] e conta["limite_saque"]

def saque(conta):
    saques_no_dia = 0
    valor = float(input("digite o valor que deseja sacar   "))
        
    if(valor > conta["saldo"]):
        print("falha ao fazer o saque , saldo insuficiente")
    elif( valor > conta["limite_saque"] ):
         print(f"erro ao fazer o saque, valor limite por saque = {conta['limite_saque']} ")
    elif( saques_no_dia >= limite_saques_por_dia):  #resolver como sera feito os saques_no_dia em contas diferentes
         print("falha ao fazer saque , limites de saques diarios execidido . maximo de 3 saques por dia")
    elif( valor <= 0 ):
                print("valor invalido")
    else:
        print("sacando :" , valor)
        conta["extrato"] += f"saque de  {valor:.2f} feito as :  {datetime.datetime.now() }\n"
        conta["extrato"] += f" {conta['saldo']:.2f} ---> {conta['saldo'] - valor} \n\n"
        conta["saldo"] -= valor
        saques_no_dia += 1                

def deposito(conta):
    valor = float(input("digite o valor que deseja depositar : "))
    print(f"depositando :  {valor} \n")
    if(valor > 0):
        conta["extrato"] += f"deposito de  {valor} feito as :  {datetime.datetime.now() }\n"
        conta["extrato"] += f" {conta['saldo']:.2f} ---> {conta['saldo'] + valor} \n\n"
        conta["saldo"] += valor
        print("valor depositado com sucesso\n")
    else:
        print ("valor invalido , por favor tente novamente\n")

def mostrar_extrato(conta):
    print("\n\n##################extrato da conta##################\n\n" + conta["extrato"] + "\n\n##################extrato da conta##################\n\n")

login_menu = """
[l] - logar
[c] - criar usuario
[q] - sair

"""

usuario_menu = """
[s] - selecionar uma conta corrente
[c] - criar conta corrente
[q] - deslogar

"""
conta_menu = """ 
[s] - saque
[d] - deposito
[e] - estrato
[c] - criar conta corrente
[q] - deslogar

"""


limite_saques_por_dia = 3
saques_no_dia = 0

id_usuario_em_uso = 0
id_conta_em_uso = 0

rodando = True

while rodando:

    while id_usuario_em_uso == 0:
        escolha = input(login_menu)
        if(escolha == 'l'):
            id_usuario_em_uso = logar(Usuarios)
        elif( escolha == 'c'):
            interface_de_cadastro(p_Usuarios = Usuarios ,p_Enderecos= Enderecos)
        elif ( escolha == 'q'):
            rodando = False

    if rodando == False:
        break

    #programar funcao de escolha de conta 

    while id_conta_em_uso == 0:
        escolha = input(usuario_menu)

        if (escolha == 's'):
            id_conta_em_uso = selecionar_conta(id_usuario_em_uso,Contas)
        elif ( escolha == 'c') :
            interface_cadastro_conta(Contas,Usuarios)


    while id_usuario_em_uso != 0 :
        print( f"conta em uso: email {Usuarios[id_usuario_em_uso]['email']} , nome : {Usuarios[id_usuario_em_uso]['nome']}")
    #nenhuma conta selecionada        print( "\n\n\ntotal na conta :" , Usuarios[id_conta_em_uso]["saldo"])
        escolha = input(conta_menu)

        if (escolha == 's') :
            saque(Contas[id_conta_em_uso])

        elif (escolha == 'd') :
            deposito(Contas[id_conta_em_uso])

        elif( escolha == 'e') :
            mostrar_extrato(Contas[id_conta_em_uso])
        elif ( escolha == 'q') :
            id_usuario_em_uso = 0
            id_conta_em_uso = 0
        elif ( escolha == 'c') :
            interface_cadastro_conta(Contas,Usuarios)
        else :
            print("comando invalido , favor tentar novamente")