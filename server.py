import socket
import time

def server (host = 'localhost', port = 8000):
    data_payload = 2048
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_adrees = (host, port)

    print("Começando servidor %s na porta %s ... " %server_adrees, end='')
    sock.bind(server_adrees)
    sock.listen(5)
    time.sleep(1)
    print('Pronto')
    

    while True:
        print("Esperando dados do cliente")
        client, address = sock.accept()
        try:
            data = client.recv(data_payload)
            if data:
                print('Requisição : "%s" \nfrom %s' %(data.decode(), address))
                print('Respondendo...', end=' ')
                client.send('OK!'.encode())
                print('Pronto')
        except:
            print('erro')
            sock.close()




server()



"""

AF_INET => para endereços de rede IPv4

socket.bind => assigns an IP address and a port number to a socket instance

socket.listen(backlog) => Marca o socket referido para ser um passivo, 
        ou seja, um socket que será usado para aceitar conexões de 
        entrada de requests. o argumento backlog  define a largura maxima
        de cada fila de conexões pendentes pode crescer
"""