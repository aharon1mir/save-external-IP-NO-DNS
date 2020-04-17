#!/usr/bin/python3

"""

@author: Aharon 

"""


import smtplib, ssl, requests

def get_ip():
    try:
        r = requests.get('https://ipinfo.io/ip')
        IP = r.content
    except Exception:
        r = requests.get('https://ipecho.net/plain')
        IP = r.content[:-1]
    return IP

def check_ip(Ip):
    File = open('/home/user/scripts/data/IP') # set here your lovely path ...
    s = File.read()
    Ip = str(Ip)
    Ip = Ip[:-3]
    Ip = Ip[2:]
    if Ip in s:
        exit()
    save_ip(Ip)
    send_ip(Ip)
    
def save_ip(IP):
    print (IP)
    File = open('/home/user/scripts/data/IP','w')#set the path here
    File.write(IP)
    File.flush()
    File.close()
    
def send_ip(IP):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "sender@gmail.com" #your sender mail here
    password = 'password'
    
    receiver_email = "reciever@gmail.com" #receiver mail here
    message = """\
    Subject: ip address

    my current IP address is:{}""".format(IP)

    print (message)
    
    # Send email here
    # Create a secure SSL context
    context = ssl.create_default_context()
    
    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 

def main():
    check_ip(get_ip())
    
if __name__ == '__main__':
    main()
