import socket

print ("INICIANDO SCAN de PORTAS")
#Mensagem inicial para user
#RM97436 - Ronan Braga

saida=""
while saida!="Sair":
    host = input("Digite o IP que deseja verificar: ")
        #Solicitação de IP que deseja realizar a verificação
         
    for i in range ( 0 , 1023):
        ##Range de portas que serão verificadas da porta 1 ate 1023 
        obj_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        obj_socket.settimeout(1)
        if obj_socket.connect_ex((host, i)):
            print("Porta ", i,"está fechada.")
            #Mensagem que sera imprimida quando a porta estiver fechada
        else:
            print("Porta ", i,"está aberta.")
            #Mensagem que sera imprimida quando a porta estiver aberta
    saida=input("Digite <Sair> para sair: ").upper()