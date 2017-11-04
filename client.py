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

    # Send data
    message = 'This is the message.  It will be repeated.'
    print 'sending "%s"' % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print 'received "%s"' % data

finally:
    print 'closing socket'
    sock.close()