# Author: Benjamin Plamondon
# helpful reference for networking: https://pymotw.com/2/socket/tcp.html
import socket

# create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# enter the ip of the server
ip = raw_input("Enter the IP of server: ")

# connect socket to desired port
server_address = (ip, 5050)
print 'connecting to %s port %s' % server_address
sock.connect(server_address)


try:
    while True:
        amount_received = 0

        while amount_received < 7:
            data = sock.recv(7)
            amount_received += len(data)
            print data

finally:
    print 'closing socket'
    sock.close()