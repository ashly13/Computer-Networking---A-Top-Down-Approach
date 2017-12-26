from socket import *
from datetime import datetime
import time

# Create a client UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Server details
serverIP = gethostbyname(gethostname())
serverPort = 12000

rtts = []
lost = 0

# Send 10 pings to server
for i in range(0, 10):

    # Ping message to be sent
    time_string = datetime.now().isoformat(sep=' ')
    message = "Ping " + str(i+1) + " " + time_string
    print "\n" + message

    # Start time to calculate RTT
    start = time.clock()

    # Send the message
    clientSocket.sendto(message, (serverIP, serverPort))

    try:
        # Set timeout for any response from the Ping server
        clientSocket.settimeout(1)
        response = clientSocket.recv(128)

        # End time to calculate RTT
        end = time.clock()
        rtt = end - start
        rtts.append(rtt)

        # Remove timeout
        print "\t" + response
        print "\tCalculated Round Trip Time = " + str(rtt) + " seconds"
        clientSocket.settimeout(None)

    except timeout:
        # Packet has been lost
        lost += 1
        print "\tRequest timed out"

# Print report
print "\n"
print "Maximum RTT = " + str(max(rtts))
print "Minimum RTT = " + str(min(rtts))
print "Average RTT = " + str(sum(rtts)/float(len(rtts)))
print "Packet Loss Percentage = " + str(float(lost)/10 * 100)