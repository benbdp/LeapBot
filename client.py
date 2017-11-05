# Author: Benjamin Plamondon
# helpful reference for networking: https://pymotw.com/2/socket/tcp.html
import socket
import serial


# create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# enter the ip of the server
ip = raw_input("Enter the IP of server: ")

# connect socket to desired port
server_address = (ip, 5050)
print 'connecting to %s port %s' % server_address
sock.connect(server_address)

ser = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=3)

try:
    while True:
        amount_received = 0

        while amount_received < 9:
            data = sock.recv(9)
            amount_received += len(data)
            ser.write((data + '\r\n').encode())

finally:
    print 'closing socket'
    sock.close()