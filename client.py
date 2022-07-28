import socket
import time

def client(host = 'localhost', port=8000): 
    data_payload = 2048
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_address = (host, port) 

    print ("Conectado a %s na porta %s" % server_address) 
    sock.connect(server_address) 

    while True: 

        message = input()

        print ("Enviando Requisição...", end=' ') 
        sock.send(message.encode()) 
        time.sleep(1)
        print('Enviado')

        data = sock.recv(data_payload) 
        print ("Resposta: %s\n" % data.decode()) 
    

client()