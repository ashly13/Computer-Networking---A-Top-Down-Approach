from socket import *
import time

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((gethostbyname(gethostname()), 12000))

# Initialize sequence number
seq = 1

while True:
    # Receive the client packet along with the address it is coming from
    serverSocket.settimeout(3 * 10)   # If server does not receive a heartbeat in 30 seconds, the client is considered dead

    try:
        message, address = serverSocket.recvfrom(1024)
    except timeout:
        print "\n\nThe Client is dead.\n"
        serverSocket.close()
        break

    serverSocket.settimeout(None)

    print "\nHeartbeat " + str(seq)

    # Split the message into 'Ping', sequence number , date and time(in string)
    message = message.split(" ")

    # Sent time
    sent = float(message[2])

    # Received time
    received = time.time()
    print "\t\t" + str(received)

    # Report the time difference between the time of sending (by client) and the time of receiving (by server)
    print "\tTime Difference = " + str(abs(received - sent)) + " seconds"

    # Calculate number of packets lost
    lost = int(message[1]) - seq
    print "\tNumber of packets lost = " + str(lost)
    seq += 1