from socket import *
import time

# Create a client UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Server details
serverIP = gethostbyname(gethostname())
serverPort = 12000

# Sequence number
seq = 1

# Send UDP Heartbeats to server to inform the server that the client is alive
while True:

    # Ping message to be sent
    message = "Ping " + str(seq) + " " + str(time.time())

    # Send the message
    clientSocket.sendto(message, (serverIP, serverPort))

    print "\n" + message
    seq += 1

    # Send a UDP Heartbeat packets every 10 seconds
    time.sleep(10)
