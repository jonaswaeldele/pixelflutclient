import imp
import socket
import time
import random
import numpy as np



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '192.168.2.115'
s.connect((ip,1337))

canvas_size = 512

#comment or something it soedhen hurht


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
            placepixel(currentx,currenty,0,0,0)
            currentlen += 1
        if 1 < randvalue < 2:
            currentx -= 1
            currenty -= 1
            placepixel(currentx,currenty,0,0,0)
            currentlen += 1
        if 2 < randvalue < 3:
            currentx += 1
            currenty -= 1
            placepixel(currentx,currenty,0,0,0)
            currentlen += 1
        if 3 < randvalue < 4:
            currentx -= 1
            placepixel(currentx,currenty,0,0,0)
            currentlen += 1
        if 4 < randvalue < 5:
            currentx += 1
            placepixel(currentx,currenty,0,0,0)
            currentlen += 1
        if 5 < randvalue < 6:
            currentx -= 1
            currenty += 1
            placepixel(currentx,currenty,0,0,0)
            currentlen += 1
        if 6 < randvalue < 7:
            currentx += 1
            currenty += 1
            placepixel(currentx,currenty,0,0,0)
            currentlen += 1
        if 7 < randvalue < 8:
            currenty += 1
            placepixel(currentx,currenty,0,0,0)
            currentlen += 1


def square(top,bottom,left,right,r,g,b):
    for i in range(top,bottom):
        for j in range(left,right):
            placepixel(i,j,r,g,b)


def squareWithCenter(xcenter,ycenter,diameter,r,g,b):
    placepixel(xcenter,ycenter,r,g,b)
    xrange = range(xcenter-int((diameter-1)/2),xcenter+int((diameter-1)/2))
    yrange = range(ycenter-int((diameter-1)/2),ycenter+int((diameter-1)/2))
    for i in xrange:
        for j in yrange:
            placepixel(i,j,r,g,b)

def horizontalThickLineSlice(xpix,ypix,thickness,r,g,b):
    yrange = range(ypix-int((thickness-1)/2),ypix+int((thickness-1)/2))
    for i in yrange:
        placepixel(xpix,i,r,g,b)

def verticalThickLineSlice(xpix,ypix,thickness,r,g,b):
    xrange = range(xpix-int((thickness-1)/2),xpix+int((thickness-1)/2))
    for i in xrange:
        placepixel(i,ypix,r,g,b)

def distancefunc(xcoord,ycoord,pixlist):
    distances = []
    for entry in pixlist:
        dist = int(np.sqrt((xcoord-entry[0])**2 + (ycoord-entry[1])**2))
        distances.append(dist)
    mindist = min(distances)
    return mindist


def randomThickLine(xstart,ystart,thickness,turnlength,maxlength,r,g,b):
    directions = ['left','right','up','down']
    directionsh = ['left','right']
    directionsv = ['up','down']
    onCanvas = True
    pixelsDirections = []
    lastx = xstart
    lasty = ystart
    totallength = 0
    inputDirection = random.choice(directions)
    while onCanvas:
        if inputDirection == 'left' or inputDirection == 'right':
            currentDirection = random.choice(directionsv)
        if inputDirection == 'up' or inputDirection == 'down':
            currentDirection = random.choice(directionsh)
        #print(currentDirection)
        pixelsToTurn = random.choice(range(2*thickness,turnlength))
        totallength += pixelsToTurn
        if currentDirection == 'left':
            for x in range(lastx,lastx-pixelsToTurn,-1):
                pixelsDirections.append((x,lasty))
            lastx -= pixelsToTurn
        if currentDirection == 'right':
            for x in range(lastx,lastx+pixelsToTurn):
                pixelsDirections.append((x,lasty))
            lastx += pixelsToTurn
        if currentDirection == 'up':
            for y in range(lasty,lasty-pixelsToTurn,-1):
                pixelsDirections.append((lastx,y))
            lasty -= pixelsToTurn
        if currentDirection == 'down':
            for y in range(lasty,lasty+pixelsToTurn):
                pixelsDirections.append((lastx,y))
            lasty += pixelsToTurn
        inputDirection = currentDirection
        if lastx < 0 or lastx > 512 or lasty < 0 or lasty > 512:
            onCanvas = False
        if totallength > maxlength:
            break
    for entry in pixelsDirections:
        squareWithCenter(entry[0],entry[1],thickness,r,g,b)

def clearcanvasfun():
    for diameter in range(0,550,20):
        squareWithCenter(265,256,diameter,0,0,0)

canvassize = 512

def clearcanvasfun2():
    pixellist = []
    for i in range(25,canvassize-25,25):
        pixellist.append((25,i))
        pixellist.append((i,canvassize-25))
    for i in range(canvassize-25,25,-25):
        pixellist.append((canvassize-25,i))
        pixellist.append((i,25))
    for i in range(75,canvassize-75,25):
        pixellist.append((75,i))
        pixellist.append((i,canvassize-75))
    for i in range(canvassize-75,75,-25):
        pixellist.append((canvassize-75,i))
        pixellist.append((i,75))
    for i in range(125,canvassize-125,25):
        pixellist.append((125,i))
        pixellist.append((i,canvassize-125))
    for i in range(canvassize-125,125,-25):
        pixellist.append((canvassize-125,i))
        pixellist.append((i,125))
    for i in range(175,canvassize-175,25):
        pixellist.append((175,i))
        pixellist.append((i,canvassize-175))
    for i in range(canvassize-175,175,-25):
        pixellist.append((canvassize-175,i))
        pixellist.append((i,175))
    for i in range(225,canvassize-225,25):
        pixellist.append((225,i))
        pixellist.append((i,canvassize-225))
    for i in range(canvassize-225,225,-25):
        pixellist.append((canvassize-225,i))
        pixellist.append((i,225))
    pixellist.append((256,256))
    for entry in pixellist:
        squareWithCenter(entry[0],entry[1],53,0,0,0)
    
def circlecontour(centerx,centery,radius,thickness,r,g,b):
    pixels = []
    for i in range(centerx-radius,centerx+radius):
        for j in range(centery-radius,centery+radius):
            if (i-centerx)**2 + (j-centery)**2 < radius**2:
                disttocenter = int(np.sqrt((i-centerx)**2 + (j-centery)**2))
                if disttocenter > radius-thickness:
                    placepixel(i,j,r,g,b)


def star_size_small(xcoord,ycoord,r,g,b):
    placepixel(xcoord,ycoord,r,g,b)
    placepixel(xcoord+1,ycoord,r,g,b)
    placepixel(xcoord,ycoord+1,r,g,b)
    placepixel(xcoord-1,ycoord,r,g,b)
    placepixel(xcoord,ycoord-1,r,g,b)

def star_size_medium(xcoord,ycoord,r,g,b):
    placepixel(xcoord,ycoord,r,g,b)
    placepixel(xcoord+1,ycoord,r,g,b)
    placepixel(xcoord,ycoord+1,r,g,b)
    placepixel(xcoord-1,ycoord,r,g,b)
    placepixel(xcoord,ycoord-1,r,g,b)
    placepixel(xcoord+2,ycoord,r,g,b)
    placepixel(xcoord,ycoord+2,r,g,b)
    placepixel(xcoord-2,ycoord,r,g,b)
    placepixel(xcoord,ycoord-2,r,g,b)
    


def nightsky(amount):
    i = 0
    j = 0
    k = 0
    while i < amount:
        xcoord = random.randrange(0,512)
        ycoord = random.randrange(0,512)
        damp = random.randrange(0,200)
        placepixel(xcoord,ycoord,255-damp,255-damp,255-damp)
        i+=1
    while j < amount:
        x = random.randrange(0,512)
        y = random.randrange(0,512)
        star_size_small(x,y,245,230,144)
        j+=70
    while k < amount:
        x = random.randrange(0,512)
        y = random.randrange(0,512)
        star_size_medium(x,y,250, 179, 97)
        k+=120



#placepixel(400,400,255,0,0)
#square(100,300,100,300,0,255,0)
#clearcanvas()
#experiment2(128,128,255,255,255,1000000)
clearcanvasfun2()
#verticalThickLineSlice(200,200,15,0,0,255)
#horizontalThickLineSlice(300,300,29,0,255,0)
#experiment3(300,300,100000)
#randomThickLine(256,256,3,100,5000,255,255,255)
#randomThickLine(256,256,5,100,5000,200,200,200)
#randomThickLine(256,256,7,100,5000,150,150,150)
#randomThickLine(256,256,9,100,5000,100,100,100)
#randomThickLine(256,256,11,100,5000,50,50,50)


#randomThickLine(256,256,5,40,10000,200,0,100)



nightsky(8000)
experiment3(100,100,100000)
experiment3(100,200,100000)
experiment3(300,300,100000)
experiment3(200,100,100000)
experiment3(300,300,100000)
experiment3(100,100,100000)
experiment3(100,200,100000)
experiment3(300,300,100000)
experiment3(200,100,100000)
experiment3(300,300,100000)

