from socket import *
import time
import base64

print ""

username = raw_input("Enter your mail.com username : ")
password = raw_input("Enter your mail.com password : ")
rec = raw_input("\nEnter the recipient's email address : ")

name = raw_input("\nEnter your name : ")
subject = raw_input("\nEnter the subject for your mail : \n")

# Allow the user to type multi-line messages
print "\nEnter the message you want to send. Press Ctrl-D to stop.\n\n"
message = []
while True:
    try:
        line = raw_input("")
    except EOFError:
        break
    message.append(line + "\r\n")


print ""

endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.mail.com"
mailserverPort = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailserverPort))

resp = clientSocket.recv(1024)
print 'S: ' + resp

# Send EHLO (for Extended SMTP) command and print server response.
heloCommand = 'EHLO Ashara\r\n'
print 'C: ' + heloCommand
clientSocket.send(heloCommand)
resp = clientSocket.recv(1024)
print 'S: ' + resp

# Authentication required for the mail.com server I'm using
command = 'AUTH LOGIN\r\n'
print 'C: ' + command
clientSocket.send(command)
resp = clientSocket.recv(1024)
print 'S: ' + resp

# Send username as Base64 encoded string
command = base64.b64encode(username) + '\r\n'
print 'C: ' + command
clientSocket.send(command)
resp = clientSocket.recv(1024)
print 'S: ' + resp

# Send password as Base64 encoded string
command = base64.b64encode(password) + '\r\n'
print 'C: ' + command
clientSocket.send(command)
resp = clientSocket.recv(1024)
print 'S: ' + resp

# Send MAIL FROM command and print server response.
command = "MAIL FROM: <" + username + ">\r\n"
print 'C: ' + command
clientSocket.send(command)
resp = clientSocket.recv(1024)
print 'S: ' + resp

# Send RCPT TO command and print server response.
command = "RCPT TO: <" + rec + ">\r\n"
print 'C: ' + command
clientSocket.send(command)
resp = clientSocket.recv(1024)
print 'S: ' + resp

# Send DATA command and print server response.
command = "DATA\r\n"
print 'C: ' + command
clientSocket.send(command)
resp = clientSocket.recv(1024)
print 'S: ' + resp

# Send message headers
# Gmail does not accept mail without headers to prevent spam
command = 'From: ' + name + ' <' + username + '>' + '\r\n'
print 'C: ' + command
clientSocket.send(command)
command = 'To: ' + rec + '\r\n'
print 'C: ' + command
clientSocket.send(command)
command = 'Date: ' + time.asctime( time.localtime(time.time()) ) + '\r\n'
print 'C: ' + command
clientSocket.send(command)
command = 'Subject: ' + subject + '\r\n'
print 'C: ' + command
clientSocket.send(command)

# Send message data.
clientSocket.send('\r\n')
for msg in message:
    print 'C: ' + msg
    clientSocket.send(msg)

# Message ends with a single period.
print 'C: ' + endmsg
clientSocket.send(endmsg)

# Send QUIT command and get server response.
command = "QUIT\r\n"
print 'C: ' + command
clientSocket.send(command)
resp = clientSocket.recv(1024)
print 'S: ' + resp
