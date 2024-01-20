import imp
import socket
import time
import random
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '192.168.2.115'
s.connect((ip,1337))

canvas_size = 512

def clearcanvas():
    for i in range(canvas_size):
        for j in range(canvas_size):
            placepixel(i,j,0,0,0)

def placepixel(xpix, ypix, r, g, b):
    global s
    if xpix < 0 or ypix < 0:
        return
    lucasbiccoce = bytes("P", 'utf-8') + xpix.to_bytes(2, 'little') + ypix.to_bytes(2, 'little') + r.to_bytes(1, 'little') + g.to_bytes(1, 'little') + b.to_bytes(1, 'little')
    try:
        #print(lucasbiccoce)
        s.send(lucasbiccoce)
    except:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,1337))

def experiment(xstart,ystart,r,g,b,length):
    placepixel(xstart,ystart,r,g,b)
    currentlen = 0
    currentx = xstart
    currenty = ystart
    while currentlen < length:
        randvalue = 25*random.random()
        if randvalue < 1:
            currenty -= 1
            placepixel(currentx,currenty,r,g,b)
            currentlen += 1
        if 1 < randvalue < 3:
            currentx -= 1
            currenty -= 1
            placepixel(currentx,currenty,r,g,b)
            currentlen += 1
        if 3 < randvalue < 5:
            currentx += 1
            currenty -= 1
            placepixel(currentx,currenty,r,g,b)
            currentlen += 1
        if 5 < randvalue < 8:
            currentx -= 1
            placepixel(currentx,currenty,r,g,b)
            currentlen += 1
        if 8 < randvalue < 11:
            currentx += 1
            placepixel(currentx,currenty,r,g,b)
            currentlen += 1
        if 11 < randvalue < 15:
            currentx -= 1
            currenty += 1
            placepixel(currentx,currenty,r,g,b)
            currentlen += 1
        if 15 < randvalue < 19:
            currentx += 1
            currenty += 1
            placepixel(currentx,currenty,r,g,b)
            currentlen += 1
        if 19 < randvalue < 25:
            currenty += 1
            placepixel(currentx,currenty,r,g,b)
            currentlen += 1

def experiment2(xstart,ystart,r,g,b,length):
    placepixel(xstart,ystart,r,g,b)
    currentlen = 0
    currentx = xstart
    currenty = ystart
    while currentlen < length:
        randvalue = 8*random.random()
        if randvalue < 1:
            currenty -= 1
            placepixel(currentx,currenty,r,g,b)
            currentlen += 1
        if 1 < randvalue < 2:
            currentx -= 1
            currenty -= 1
            placepixel(currentx,currenty,r,g,b)
            currentlen += 1
        if 2 < randvalue < 3:
            currentx += 1
            currenty -= 1
            placepixel(currentx,currenty,r,g,b)
            currentlen += 1
        if 3 < randvalue < 4:
            currentx -= 1
            placepixel(currentx,currenty,r,g,b)
            currentlen += 1
        if 4 < randvalue < 5:
            currentx += 1
            placepixel(currentx,currenty,r,g,b)
            currentlen += 1
        if 5 < randvalue < 6:
            currentx -= 1
            currenty += 1
            placepixel(currentx,currenty,r,g,b)
            currentlen += 1
        if 6 < randvalue < 7:
            currentx += 1
            currenty += 1
            placepixel(currentx,currenty,r,g,b)
            currentlen += 1
        if 7 < randvalue < 8:
            currenty += 1
            placepixel(currentx,currenty,r,g,b)
            currentlen += 1

grey_values = list(range(255))
grey_values_reverse = list(range(255,0,-1))
c_values_1 = grey_values + grey_values_reverse
c_values_2 = 1000 * c_values_1
print(len(c_values_2))

def experiment3(xstart,ystart,length):
    placepixel(xstart,ystart,0,0,0)
    currentlen = 0
    currentx = xstart
    currenty = ystart
    while currentlen < length:
        c = c_values_2[currentlen]
        randvalue = 8*random.random()
        if randvalue < 1:
            currenty -= 1
            placepixel(currentx,currenty,c,0,c)
            currentlen += 1
        if 1 < randvalue < 2:
            currentx -= 1
            currenty -= 1
            placepixel(currentx,currenty,0,c,c)
            currentlen += 1
        if 2 < randvalue < 3:
            currentx += 1
            currenty -= 1
            placepixel(currentx,currenty,c,0,c)
            currentlen += 1
        if 3 < randvalue < 4:
            currentx -= 1
            placepixel(currentx,currenty,c,0,c)
            currentlen += 1
        if 4 < randvalue < 5:
            currentx += 1
            placepixel(currentx,currenty,c,c,c)
            currentlen += 1
        if 5 < randvalue < 6:
            currentx -= 1
            currenty += 1
            placepixel(currentx,currenty,c,c,c)
            currentlen += 1
        if 6 < randvalue < 7:
            currentx += 1
            currenty += 1
            placepixel(currentx,currenty,c,0,c)
            currentlen += 1
        if 7 < randvalue < 8:
            currenty += 1
            placepixel(currentx,currenty,c,c,c)
            currentlen += 1


def square(top,bottom,left,right,r,g,b):
    for i in range(top,bottom):
        for j in range(left,right):
            placepixel(i,j,r,g,b)

#placepixel(400,400,255,0,0)
#square(100,300,100,300,0,255,0)
clearcanvas()
#experiment2(128,128,255,255,255,1000000)
experiment3(0,0,500000)
experiment3(128,128,500000)
experiment3(256,256,500000)
