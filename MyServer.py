import socket,time


class MyServer:

    def __init__(self, Ip, Port):
        self.Ip = Ip
        self.Port = Port
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((Ip,Port))
        self.socket.listen(128)

    def getClientServerStatus(self):                        #To obtain users status i.e. Ip addres, OS status


        print('A connection with %s has been satisfied on port %s. '%self.add )

        print(self.content.decode('utf8'))


    def setResponceHeader(self):                            #Set responce headers before sending back
        responceHeader = 'HTTP/1.1 200 OK\n'
        responceHeader+= '\n'
        return responceHeader

        #self.client_socket.send(responceHeader.encode('utf8'))


    #def sendResponce(self,responceHeader, responceBody):

    def send(self):
        self.client_socket, self.add = self.socket.accept()
        self.content = self.client_socket.recv(1024)
        self.client_socket.send(self.setResponceHeader().encode('utf8'))               #send the responce headers before sending the body part
        requestHeader = self.content.decode('utf8')  # TAKE THE REQUEST HEADER FROM THE CLIENT (WEB USER)

        if requestHeader:
            path = requestHeader.splitlines()[0].split(' ')[1]  # Using split() to find the exact request i.e /login, /home they usually on the first line of the request headers
            if (path == '/home'):
                self.client_socket.send('Welcom To My Page...'.encode('utf8'))
            elif(path == '/logo'):
                self.client_socket.send((self.displayLogo()))
            elif(path == '/register'):
                self.client_socket.send('Registing...'.encode('utf8'))

        else:
            print('NO RESPONCE ACCEPTED')
        self.socket.close()

    def displayLogo(self):

        with open('pic.png','rb') as p:
            content = p.read()
            p.close()
            return content


ms = MyServer('0.0.0.0',9090)
print('finished')
ms.send()
print('finished')




