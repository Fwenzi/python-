import socket,threading,time
# tcp
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('127.0.0.1',9999))
# s.listen(5)
# print('wait....')

# def tcplink(sock,addr):
# 	print('Accept new connection from %s:%s...' % addr)
# 	sock.send(b'welcome')
# 	while True:
# 		data = sock.recv(1024)
# 		time.sleep(1)
# 		if not data or data.decode('utf-8') == 'exit':
# 			break
# 		sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
# 	sock.close()
# 	print('%s:%s'%addr)

# while True:
# 	sock,addr = s.accept()

# 	t = threading.Thread(target=tcplink, args=(sock,addr))
# 	t.start()

# udp
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))

print('wait udp')
while True:
	data,addr = s.recvfrom(1024)
	print('from %s:%s'%addr)
	s.sendto(b'hello,%s'% data,addr)