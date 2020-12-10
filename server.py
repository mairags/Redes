# Echo server program
from socket import * 
from numpy import *
import matplotlib.pyplot as plt
import math

HOST = '127.0.0.1'
PORT = 50007
s = None

def formatParam(param):
    p = param.split(',')
    a, b, N, teta, omega, l = int(p[0]), int(p[1]), int(p[2]), pi/int(p[3]), int(p[4]), int(p[5])
    return a, b, N, teta, omega, l

def rungeKutta(a = 0, b = 10, N = 2000, teta = pi/12, omega = 0, l = 4):
    data = "|"
    pos = ""
    vel = ""
    x = ""
    px = ""
    py = ""
    g = 9.81
    cnt = 0
    h = (b-a)/N

    for i in range(1, N):
        data = data + str(cnt) + ", " + str(teta) + ", " + str(omega) + ", " + str(l*sin(teta)) + ", " + str(-l*cos(teta)) + "|"
        x = x + str(cnt) + ", "
        pos = pos + str(teta) + ", "
        vel = vel + str(omega) + ", "

        px = px + str(l*sin(teta)) + ", " + str(-l*cos(teta)) + " - "
        py = py + str(-l*cos(teta)) + ", "
        
        v1 = h*(-g/l*sin(teta))
        p1 = h*omega
        
        v2 = h*(-g/l*sin(teta + v1/2))
        p2 = h*(omega + p1/2)

        v3 = h*(-g/l*sin(teta + v2/2))
        p3 = h*(omega + p2/2)

        v4 = h*(-g/l*sin(teta + v3))
        p4 = h*(omega + p3)

        omega = omega + (v1 + 2*v2 + 2*v3 + v4)/6
        teta = teta + (p1 + 2*p2 + 2*p3 + p4)/6
        cnt = i*h
    return bytes(data, "utf8")


# create an INET, STREAMing socket
serversocket = socket(AF_INET, SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind((HOST, 50007))
# become a server socket
serversocket.listen(5)

while True:
    # accept connections from outside
    (clientsocket, address) = serversocket.accept()
    param = clientsocket.recv(64000) 
    a, b, N, teta, omega, l = formatParam(param.decode())
    data = rungeKutta(a, b, N, teta, omega, l)
    clientsocket.send(data)
    break
    # now do something with the clientsocket
    # in this case, we'll pretend this is a threaded server
    # ct = client_thread(clientsocket)
    # ct.run()
