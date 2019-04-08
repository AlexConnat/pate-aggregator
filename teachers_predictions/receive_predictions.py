#!/usr/bin/python2

import socket
import sys

if len(sys.argv) != 4:
    print("Usage: %s server_ip server_port nb_teachers" % (sys.argv[0])) # MUST BE A VALID IP AND VALID PORT
    exit(1)

CHUNK_SIZE = 8 * 1024
NB_TEACHERS = int(sys.argv[3])
SERVER_IP = sys.argv[1]          # "10.10.55.100"
SERVER_PORT = int(sys.argv[2])   # 1337
MAX_NB_CONNECTIONS = 10

teacher_id = 0
teachers_received = set()

server_socket = socket.socket()
server_socket.bind( (SERVER_IP, SERVER_PORT) )
server_socket.listen(MAX_NB_CONNECTIONS)

print("[*] Listening on port " + str(SERVER_PORT) + "\n")

while (teacher_id+1 <= NB_TEACHERS): # Loop until all NB_TEACHERS predictions are received

	client_socket, (addr, port) = server_socket.accept()

	if addr not in teachers_received:
 		
		teachers_received.add(addr)
		print("Incoming data from Teacher @ " + str(addr))
		
		data = b""
		chunk = client_socket.recv(CHUNK_SIZE)
		data += chunk
		while chunk:
			chunk = client_socket.recv(CHUNK_SIZE)
			data += chunk

		filename = "predictions_teacher_" + str(teacher_id) + ".npy"

		with open(filename, "wb") as f:
			f.write(data)
	
		print("Data saved under '" + filename + "'\n")
		print("==== Received " + str(len(teachers_received)) + "/" + str(NB_TEACHERS) + " Teacher Predictions ====\n")

		teacher_id += 1

	else:

		print("Already received data from Teacher @ " + str(addr) + "\n")

print("[*] Start the aggregator\n")

print("[*] Start training student\n")
