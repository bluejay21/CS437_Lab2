import socket
import CarController

HOST = "192.168.0.164" # IP address of your Raspberry PI
PORT = 65432          # Port to listen on (non-privileged ports are > 1023)

car_C = CarController.CarController()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    try:
        while 1:
            client, clientInfo = s.accept()
            print("server recv from: ", clientInfo)
            data = client.recv(1024)      # receive 1024 Bytes of message in binary format
            if data != b"":
                print(data)     
                # print("FAIL1")
                cmdHandling = car_C.handleCommand(data)
                # car_C.printHello()
                # print("FAIL2")
                # print(cmdHandling)
                # client.sendall(data) # Echo back to client
                if(data == b"INFO"):
                    print("cmdHandling: " + cmdHandling)
                    client.sendall(cmdHandling.encode())

    except: 
        print("Closing socket")
        client.close()
        s.close()    