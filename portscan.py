import socket


host = str(input("Enter the host to be scanned: "))   
ip = socket.gethostbyname(host)     

print ("ip = ",ip)
while 1:
	port = int(input("Enter the port: "))	   	
	try:
		sock = socket.socket()			
		res = sock.connect((ip, port))
		print ("Given port is Open")
		sock.close()
	except:
		print ("given port is Closed")
print ("Port Scanning complete")
