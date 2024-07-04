import serial
import serial.tools.list_ports
 

def get_serial_port():
    ports_list = list(serial.tools.list_ports.comports())
    if len(ports_list) <= 0:
        return None
    else:
        return list(ports_list[0])[0]
    
if __name__ == '__main__':
    print(get_serial_port())
