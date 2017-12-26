from socket import *
from threading import Thread


def serviceRequest(connectionSocket):
    try:
        # Receive HTTP request from browser
        message = connectionSocket.recv(1024)

        # Open file mentioned in the first line of the HTTP request header
        filename = message.split()[1]
        print '\n\n-------------------------------------------------'
        print "Request for file " + filename[1:]
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
    except IndexError:
        # Close client socket
        connectionSocket.close()



serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverSocket.bind((gethostname(), 5432))
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

print "\nServer has been started at IP = " + gethostbyname(gethostname()) + " and port = 5432"
threads = []

while True:
    serverSocket.listen(40)

    #Establish the connection
    connectionSocket, address = serverSocket.accept()

    # Create a thread to service the received request
    newThread = Thread(target=serviceRequest, args=(connectionSocket,))
    newThread.start()
    threads.append(newThread)

serverSocket.close()