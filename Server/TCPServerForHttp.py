import socket,time





server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('172.20.10.3', 9000))
server_socket.listen(128)       #TCP server进行监听

accept_new = server_socket.accept()     #接受消息 收到的消息为一个tuple， 第0位为data，第1位为ip address and port number
print('\nA new client came...Ip address is %s, with the port number %s'% accept_new[1])
client_socket,client_add = accept_new
data = client_socket.recv(1042).decode('utf8')

#传送正式内容之前 要先发送 Response Headers
client_socket.send(('HTTP/1.1 200 OK\n'.encode('utf8')))
client_socket.send(('\n'.encode('utf8')))


with open('pic.png','rb') as file:
    content = file.read()

    file.close()


client_socket.send(content)


server_socket.close()