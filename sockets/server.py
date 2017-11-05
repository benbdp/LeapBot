# Author: Benjamin Plamondon
# helpful reference for networking: https://pymotw.com/2/socket/tcp.html
import socket

# find the local ip address of the server
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

# create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect socket to desired port
server_address = (ip, 5050)
print 'starting up on %s port %s' % server_address
sock.bind(server_address)

# listen for connections
sock.listen(1)

while True:
    # Wait for a connection
    print 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print 'connection from', client_address

        while True:
            left = raw_input("Enter right: ")
            right = raw_input("Enter left: ")
            transmit = left+','+right
            print len(transmit)
            connection.sendall(transmit)

    finally:
        # close connection
        connection.close()