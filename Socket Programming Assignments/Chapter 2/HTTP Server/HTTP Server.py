from socket import *

print "\n" + gethostbyname(gethostname())

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverSocket.bind((gethostname(), 5432))
serverSocket.listen(1)

while True:
    #Establish the connection
    print '\n\nReady to serve...'
    connectionSocket, address = serverSocket.accept()
    try:
        # Receive HTTP request from browser
        message = connectionSocket.recv(1024)
        print "\n" + message

        # Open file mentioned in the first line of the HTTP request header
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")

        #Send the content of the requested file to the client
        connectionSocket.send(outputdata)
        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n")

        #Close client socket
        connectionSocket.close()

serverSocket.close()