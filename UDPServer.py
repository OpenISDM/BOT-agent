import serial
import socket
import time
FROM_GATEWAY 	= 0
FIRE_ALARM 		= 1
API_VERSION 	= 2
MODE 			= 3
DURATION 		= 4

serialPortName = '/dev/ttyUSB0'
UDPPort = 20001

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip
def alert_operation(mode, duration):
	if(mode == 1):
		conn.write('RS')
		time.sleep(duration)
		conn.write('FQ')
	elif(mode == 2):
		conn.write('1P')
		time.sleep(duration)
		conn.write('FQ')
	elif(mode == 3):
		conn.write('RS1P')
		time.sleep(duration)
		conn.write('FQ')
	else: 
		print('unrecognized mode')

# setup serial port
IP = get_host_ip()

conn = serial.Serial(serialPortName, timeout=.2)
time.sleep(3)
# setup UDP client port
serverAddressPort   = (IP, UDPPort)
bufferSize  = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(serverAddressPort)
print('Start UDP Server Listening at port: {}'.format(serverAddressPort[0]))

while True:
	bytesAddressPair = sock.recvfrom(bufferSize)
	
	# print(bytesAddressPair[0], bytesAddressPair[1])
	message = bytesAddressPair[0]
	address = bytesAddressPair[1]
	API_ver = None
	print('received message: {}, from: {}'.format(message, address))
	splitted_message = message.split(';')
	if(splitted_message[FROM_GATEWAY] != '6'):
		print('Data aren\'t from Gateway')
		continue
	elif(splitted_message[FIRE_ALARM] != '7'):
		print('FIRE_ALARM Error')
		continue
	else:
		API_ver = splitted_message[API_VERSION]
		mode = int(splitted_message[MODE])
		duration = int(splitted_message[DURATION])
		alert_operation(mode, duration)