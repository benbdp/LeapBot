import serial.tools.list_ports
import serial

ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p[0])
    ser = serial.Serial(p[0], baudrate=9600, timeout=3)



if __name__ == "__main__":
    entry = input("enter: ")
    ser.write((str(entry) + '\r\n').encode())
