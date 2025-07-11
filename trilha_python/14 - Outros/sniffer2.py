import socket
 
host = "192.168.0.14"
 
sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP) # considerando só o protocolo IP
 
sniffer.bind((host,0))
 
sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1) # captura o cabeçalho IP dos cabeçalhos
 
sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON) # Para Windows
 
while True:
   dados = sniffer.recvfrom(10000) # recebe o IP do pacote
   print (dados)