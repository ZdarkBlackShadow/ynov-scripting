import socket

def demarrer_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect(('localhost', 12345))
        
        message = "Hello World!"
        client.send(message.encode('utf-8'))
        
        reponse = client.recv(1024).decode('utf-8')
        print(f"Answer : {reponse}")
        
    except ConnectionRefusedError:
        print("Error")
    finally:
        client.close()

if __name__ == "__main__":
    demarrer_client()
