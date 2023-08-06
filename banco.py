import datetime

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