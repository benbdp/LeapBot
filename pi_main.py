import serial.tools.list_ports
import serial

ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p[0])
    ser = serial.Serial(p[0], baudrate=9600, timeout=3)

def write(serial,throttle):
    serial.write((str(throttle) + '\r\n').encode())


if __name__ == "__main__":
    entry = input("enter: ")
    write(entry)