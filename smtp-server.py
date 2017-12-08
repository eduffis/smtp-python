#!/usr/bin/env python
"""
Autor: Erick Duffis, 
email: erickduffis@gmail.com
hello everyone, this code I did to solve a problem that had been dragging 
for years in my company. Whenever they sent emails we ended up involved 
in blacklists, such as barracuda, dnsbl.spfbl.net and others.
you just have to have an account in gmail and remember to configure 
the security of the account to accept unsafe applications connections, 
otherwise it will not work. Happy hacking
"""
import os,sys,re
import smtpd
import asyncore
import smtplib
import email
import email.header
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

EGMAIL = "gmailacount@gmail.com"
SERVER = "192.168.0.16"
SMTP_PORT = 3025
PASSWD = "yourPassword"

#Send the respons to the user and the attachment file				
def sendSMTPFile(in_from,in_file,toaddr,body,subject):	
	fromaddr = in_from
	msg = MIMEMultipart()	
	msg.add_header('reply-to', in_from)
	msg['From'] = in_from + ' <' + EGMAIL + '>' # peacefully valid
	msg['To'] = str(toaddr).strip('[').strip(']').strip("'")
	msg['Subject'] = subject		

	#Email Body		
	msg.attach(MIMEText(body, 'plain'))
	
		
	#Email Attachment
	local_files = []
	for item in in_file:
		filename = item
		local_files.append(item)
		attachment = open(filename, "rb")
		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename=%s" % filename)
		msg.attach(part)
		os.system("rm -rf " + item) #Delete file
	
	#Send mesagges process	
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(EGMAIL, PASSWD)
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
		
		
class CustomSMTPServer(smtpd.SMTPServer):
    
	def process_message(self, peer, mailfrom, rcpttos, data):		
		print 'Ip Address:', peer
		print 'Messages length:', len(data)		
		
		#geting email from string
		msg = email.message_from_string(data)
		decode = email.header.decode_header(msg['Subject'])[0]	
		subject = decode[0]
		
		#text body information				
		if msg.is_multipart():
			for part in msg.walk():
				ctype = part.get_content_type()
				cdispo = str(part.get('Content-Disposition'))

				# skip any text/plain (txt) attachments
				if ctype == 'text/plain' and 'attachment' not in cdispo:
					body = part.get_payload(decode=True)  # decode
					break					
		else:
			body = msg.get_payload(decode=True)
		
		#Geting attachment files
		in_file = []
		for part in msg.walk():
			if part.get_content_maintype() == 'multipart':
				continue
			if part.get('Content-Disposition') is None:
				continue	
			
			# Replace Special Caracters from filename
			filename = re.sub('[^A-Za-z0-9]+', '', part.get_filename().split('.')[0]) + "." + part.get_filename().split('.')[1]  
			trash = re.sub('[^A-Za-z0-9]+', '', part.get_filename())
			in_file.append(filename)
			if filename is not None:
				sv_path = os.path.join(".", filename)
				if not os.path.isfile(sv_path):
					print sv_path       
					fp = open(sv_path, 'wb')
					fp.write(part.get_payload(decode=True))
					fp.close()
			
			#Cleen up trash files
			os.system("rm -rf " + trash)
			
		sendSMTPFile(mailfrom,in_file,rcpttos,body,subject)		
		return
	
	

server = CustomSMTPServer((SERVER, SMTP_PORT), None)

asyncore.loop()
