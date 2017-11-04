from socket import *
network = '192.168.1.'
def is_up(addr):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(0.01)    ## set a timeout of 0.01 sec
    if not s.connect_ex((addr,135)):    # connect to the remote host on port 135
        s.close()                       ## (port 135 is always open on Windows machines, AFAIK)
        return 1
    else:
        s.close()

def run():
    print  ' '
    for ip in xrange(1,256):    ## 'ping' addresses 192.168.1.1 to .1.255
        addr = network + str(ip)
        if is_up(addr):
            print '%s \t- %s' %(addr, getfqdn(addr))    ## the function 'getfqdn' returns the remote hostname
    print    ## just print a blank line

if __name__ == '__main__':
    print '''I'm scanning the local network for connected Windows machines (and others with samba server running).
Also, I'll try to resolve the hostnames.
This might take some time, depending on the number of the PC's found. Please wait...'''

run()
raw_input('Done')

# import socket
# import sys
#
# # Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#
#
# # Connect the socket to the port where the server is listening
# server_address = ('192.168.43.29', 10000)
# print >>sys.stderr, 'connecting to %s port %s' % server_address
# sock.connect(server_address)
# try:
#
#     # Send data
#     message = 'This is the message.  It will be repeated.'
#     print >> sys.stderr, 'sending "%s"' % message
#     sock.sendall(message)
#
#     # Look for the response
#     amount_received = 0
#     amount_expected = len(message)
#
#     while amount_received < amount_expected:
#         data = sock.recv(16)
#         amount_received += len(data)
#         print >> sys.stderr, 'received "%s"' % data
#
# finally:
#     print >> sys.stderr, 'closing socket'
#     sock.close()