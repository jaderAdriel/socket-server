import socket
import response_routes

def server (host = 'localhost', port = 8001):
    data_payload = 2048
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_adrees = (host, port)

    try:
        print("Começando servidor %s na porta %s" %server_adrees, end='')
        sock.bind(server_adrees)
        sock.listen(5)
    except:
        sock.close()
        print('\nocupado')
        return 
    

    while True:
        print("\nEsperando dados do cliente")
        client, _ = sock.accept()
        try: 
            request = client.recv(data_payload)
            if request: 
                response = response_routes.__init__(request.decode("utf-8")) 
                print('Request: ',request, '\nResponse: ', response.encode("utf-8"))
                client.send(response.encode("utf-8"))
        except:
            print('\nerro')
            sock.close()
            return 




server()



"""

AF_INET => para endereços de rede IPv4

socket.bind => assigns an IP address and a port number to a socket instance

socket.listen(backlog) => Marca o socket referido para ser um passivo, 
        ou seja, um socket que será usado para aceitar conexões de 
        entrada de requests. o argumento backlog  define a largura maxima
        de cada fila de conexões pendentes pode crescer
"""