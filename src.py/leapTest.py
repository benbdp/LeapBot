# https://developer.leapmotion.com/

import os, sys, inspect
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap, sys


class SampleListener(Leap.Listener):

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        if len(frame.hands) == 2:
            for hand in frame.hands:
                if hand.is_left:
                    left = -int((hand.palm_position.z)*1.5)
                else:
                    right = -int((hand.palm_position.z)*1.5)
            try:
                transmit = str(left) + ',' + str(right)
                print transmit

            except:
                pass
        else:
            transmit = '0' + ',' + '0'
            print(transmit)

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
