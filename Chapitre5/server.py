import socket

def start_server():
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    serveur.bind(('localhost', 12345))
    
    serveur.listen(1)
    print("Start server")
    
    client_socket, adresse = serveur.accept()
    print(f"Connection with {adresse}")
    
    donnees = client_socket.recv(1024).decode('utf-8')
    print(f"Message reçu : {donnees}")
    
    client_socket.send("Server have a message".encode('utf-8'))
    
    client_socket.close()
    serveur.close()

if __name__ == "__main__":
    start_server()