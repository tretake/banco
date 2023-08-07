import datetime

Usuarios = [{"idusuario": 0 , "email": "" ,"senha" : "" , "cpf": "" , "nome": "" , "data_nascimento" : ""}]
Contas = [{"numero": 0 , "agencia" : "" ,"id_usuario" : 0 }]
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
     conta = {"numero": 0 , "agencia" : "0001" ,"id_usuario" : p_idusuario }
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

def interface_cadastro_conta(p_Contas , p_Usuarios):
    email = input("porfavor informe o email de seu usuario : ")
    senha = input("porfavor informe a senha do seu usuario : ")
    cpf = input("porfavor informe seu cpf : ")

    usuario_correto = False
    id_usuario = 0
    for usuario in p_Usuarios:
        if (usuario["email"] == email and usuario["senha"] == senha and usuario["cpf"] == cpf ):
            usuario_correto = True
            id_usuario = usuario["idusuario"]
            break
    
    conta = {}
    if(usuario_correto == True):
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

Usuarios.append( cadastrar_usuario("ruanlourencosilva.rj@gmail.com", "umasenha_ai", "19516113737" , "ruan" , "25/06/2001") )
Usuarios.append( cadastrar_usuario("tretakezica@gmail.com", "1234a_melhor_senha_do_mundo", "999999999" , "tretake" , "01/12/2011") )

print(Usuarios)
print(Enderecos)
print(Contas)


interface_de_cadastro(p_Usuarios=Usuarios , p_Enderecos=Enderecos)

print(Usuarios)
print(Enderecos)
print(Contas)

interface_cadastro_conta(Contas,Usuarios)

print(Usuarios)
print(Enderecos)
print(Contas)






menu = """ 
[s] - saque
[d] - deposito
[e] - estrato
[q] - fechar programa
"""

valor = 0.00
limite_saque = 500.00
limite_saques_por_dia = 3
total_conta = 2000.00
extrato = ""

saques_no_dia = 0

while True :
    print( "\n\n\ntotal na conta :" , total_conta)
    escolha = input(menu)
    print("voce escolheu " + escolha)
    if (escolha == 's') :
        valor = float(input("digite o valor que deseja sacar   "))
        
        if(valor > total_conta):
            print("falha ao fazer o saque , saldo insuficiente")
        elif( valor > limite_saque ):
             print(f"erro ao fazer o saque, valor limite por saque = {limite_saque} ")
        elif( saques_no_dia >= limite_saques_por_dia):
             print("falha ao fazer saque , limites de saques diarios execidido . maximo de 3 saques por dia")
        elif( valor <= 0 ):
                    print("valor invalido")
        else:
            print("sacando :" , valor)
            extrato += f"saque de  {valor:.2f} feito as :  {datetime.datetime.now() }\n"
            extrato += f" {total_conta:.2f} ---> {total_conta - valor} \n\n"
            total_conta -= valor
            saques_no_dia += 1                


    elif (escolha == 'd') :
        valor = float(input("digite o valor que deseja depositar   "))
        print("depositando :" , valor)
        extrato += f"deposito de  {valor} feito as :  {datetime.datetime.now() }\n"
        extrato += f" {total_conta:.2f} ---> {total_conta + valor} \n\n"
        
        total_conta += valor
    elif( escolha == 'e') :
        print( "\n\n##################extrato da conta##################\n\n" + extrato + "\n\n##################extrato da conta##################\n\n")
    elif ( escolha == 'q') :
        break
    else :
        print("comando invalido , favor tentar novamente")