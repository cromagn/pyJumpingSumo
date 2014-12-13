import socket
import zmq
PUB_IP = '127.0.0.1'
PUB_PORT = 5000

SUB_IP = '127.0.0.1'
SUB_PORT = 5001

TCP_IP = '127.0.0.1'
TCP_PORT = 5000

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

BUFFER_SIZE = 1024
print ("ZMQ Subsystem")
print ("  Init ZMQ system with version: %s" %zmq.pyzmq_version())
context = zmq.Context()
print ("  ZMQ context created ")

print ("  Init ZMQ PUB")
socketPub = context.socket(zmq.PUB)
socketPub.bind("tcp://%s:%s" % (PUB_IP,PUB_PORT))
print ("  Created ZMQ PUB on tcp://%s:%s" % (PUB_IP,PUB_PORT))

print ("  Init ZMQ SUB")
socketSub = context.socket(zmq.SUB)
socketSub.bind("tcp://%s:%s" % (SUB_IP, SUB_PORT))
print ("  Created ZMQ SUB on tcp://%s:%s" % (SUB_IP, SUB_PORT))


MESSAGE = "{ \"controller_name\" : \"Python_rulez\", \"controller_type\": \"PC\", \"d2c_port\": 54321 }\")" 
print ("Handshake")
print ("  Init TCP Handshake on IP %s:%s with message : %s"%(TCP_IP,TCP_PORT, MESSAGE))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
print ("  End TCP Handshake with message : %s"%data)


MESSAGE = "Hello, World!"
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


#socket.send("%d %d" % (topic, messagedata)) #Invio su coda