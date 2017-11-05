# Author: Benjamin Plamondon & Dominic Orlando
# helpful reference for networking: https://pymotw.com/2/socket/tcp.html


# IMPORTS
import socket
import os, sys, inspect
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
import Leap, sys

leftDiff = 0
rightDiff = 0


# DEFINE LEAP
class SampleListener(Leap.Listener):

    def on_frame(self, controller):
        global leftDiff
        global rightDiff
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        if len(frame.hands) == 2:
            for hand in frame.hands:
                if hand.is_left:

                    rawLeft = int(hand.palm_position.z)
                    left = rawLeft+leftDiff
                    leftDiff = left-rawLeft

                    if left <= 30 and left >= -30:
                        left = 0

                else:

                    rawRight = int(hand.palm_position.z)
                    right = rawRight+rightDiff
                    rightDiff = right-rawRight

                    if right <= 30 and right >= -30:
                        right = 0

                try:
                    transmit = str(left) + ',' + str(right)
                    print transmit
                    connection.sendall(transmit)
                except:
                    pass
        else:
            transmit = '0' + ',' + '0'
            connection.sendall(transmit)

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

        listener = SampleListener()
        controller = Leap.Controller()

        controller.add_listener(listener)

        while True:
            try:
                sys.stdin.readline()
            except KeyboardInterrupt:
                pass
            finally:
                # Remove the sample listener when done
                controller.remove_listener(listener)

    finally:
            connection.close()

