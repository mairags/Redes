# Echo client program
from socket import *
from numpy import *
import matplotlib.pyplot as plt
import math
import time

HOST = '127.0.0.1'
PORT = 50007
s = socket(AF_INET, SOCK_STREAM)

s.connect((HOST, PORT))
params = ",0,10,2000,12,0,2"
with s:
    processingTime = 1
    s.sendall(bytes("0" + params, "utf8"))
    time.sleep(processingTime)
    size = s.recv(64)
    print(size.decode())
    data = s.recv(4096).decode()
    # print(data)
    for i in range(1, int(size.decode())):
        s.sendall(bytes(str(i) + params, "utf8"))
        data += s.recv(4096).decode()
        # print(data)
        time.sleep(0.005)
    # print(data)

    dados = repr(data).split("|")
    x = []
    pos = []
    vel = []
    px = []
    py = []
    for d in dados[1: len(dados) - 1]:
        aux_x, aux_pos, aux_vel, aux_px, aux_py = d.split(",")

        x.append(float(aux_x))
        pos.append(float(aux_pos))
        vel.append(float(aux_vel))
        px.append(float(aux_px))
        py.append(float(aux_py))

    for val in px:
        print(val)

    print("----------------------------")

    for val in py:
        print(val)

    print("----------------------------")
    plt.figure(figsize=(12,6))
    plt.subplot(111),plt.plot(x, pos, 'green'),plt.xlabel('Teta (verde) - Omega (vermelho)'),plt.ylabel('vetoriais')
    plt.subplot(111),plt.plot(x, vel, 'red')
    plt.grid(color='black', linestyle='-', linewidth = 0.2)

    plt.figure(figsize=(12,9))
    plt.subplot(312),plt.plot(px, py, 'blue'),plt.xlabel('Rota do pêndulo'),plt.ylabel('pos')

    plt.grid(color='black', linestyle='-', linewidth = 0.2)
    plt.show()



#print('Received', repr(data).split(","))

def format(data):
    return data.split(",")[1]

# x, pos, vel, px, py = format(data)

