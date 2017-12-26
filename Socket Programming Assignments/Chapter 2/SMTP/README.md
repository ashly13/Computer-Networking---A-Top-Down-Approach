# SMTP Mail Client

This SMTP mail client uses the mail.com SMTP server (**smtp.mail.com**) at **port 587** to send a sample email.

You will need a mail.com account to successfully run this program.

The program will convert your mail.com account username (usually your email address) and password to **Base64** encoding. This is required to authenticate with the mail.com SMTP server.

Enter your email address and the email address where you want this email to be sent (**not in Base64!**) along with your name for the message header.

Run the program. 

If all goes well (this will be indicated by the messages from the mail server), you will find the mail in the Sent folder in your mail.com account.

The messages from the server will be indicated as:
> S: Message from server.

The commands and messages sent from the client will be indicated as:
> C: Commands from client to server.
