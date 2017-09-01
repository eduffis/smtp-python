# smtp-python
smtp server that uses a gmail account with any other .com domain, using a mail client (Thunder Bird / Outlook express or any other).
when the end user answers your email it is returned/replay to your domain.com INBOX, not to gmail. The process is transparent to the Client

This code saves your life with the problem of email and blacklists. Because I could not find any program on the internet that made the client's (Thunder Bird/OutLook) teams work transparently without having to do any installation in each one. I decided to develop this program that generates an SMTP server, receives all the requests of the clients in a specific port and transfers them to a GMAIL account, in this way I do not have to use my public IP that every month appears in a new blacklist

This application  was tested on a Python 2.7 and Ubuntu server 12.4
To put it to work you do not need experience in python just put to run the program and you're done.
Before running it, edit the smtp-server.py file:
Edit row 23, EGMAIL = "gmailacount@gmail.com" and enter your gmail account, then edit row 24, SERVER = "192.168.0.16", enter the ip number of the linux server, row 25 , SMTP_PORT = 3025, you can leave this way or place some port of preference, row 26, PASSWD = "yourPassword", the password of the GMAIL account.

Execution:
After editing the file, you are ready to do your work.
First you have to give permissions as executable to the program:
chmod a + x smtp-server.py
and then run:
./smtp-server.py

For users or customers, the test was run under the ThunderBird program under Windows, but it can certainly work in any other mail client because almost all are configured in the same way

Cliente computer config:
For client computers, it was tested with the program ThunderBird under Windows, but surely it will work in any other mail client because almost all are configured in the same way.

In the Tools menu, choose Email accounts, SMTP outgoing server, Add new account.
In the description you can place any name. In the name of the server placed the same IP number that was configured, in my case 192.168.0.16
the port number is also the same that we put in file 3025.

In connection security select the option that says (none), and in the method of identification, password transmitted in an insecure way.

can check the JPG goat to get a better idea.

Warning:
I do not recommend running the code on a server that has a public IP, because we are not using any method of encryption, you must be sure that it is a machine with private address.

Finishing:
This program was made with the intention of helping those who, like me, suffer from the blacklist problem, we as system administrators know that it is a headache or a kick in the buttock. I am not responsible if it is used improperly and maliciously.
