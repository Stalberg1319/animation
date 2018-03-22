##Tiera Lee, lee320
##Instanting 4 cloud objects
from shapes import *
from iceCreamCone import *
time = 0
frame = 0
xPos = -70.0
cloudX = 0
negCloudX = 0
yCamera = -100
xCamera = 0
zCamera = 75

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view

def draw():
    global frame
    frame += 1
    global time
    time += 0.1
    global xPos
    
    backgroundScene()
    cameraControl()
    lightingControl()
       
    ##iceCreamCone
    if (frame > 50):
        pushMatrix()
        if (xPos < 0):
            translate(xPos,2*sin(time/.5),0)
            xPos += 0.45
        scale(0.5,0.5,0.5)
        if(frame > 400 and frame < 500):
            rotateZ(-PI/8)
        if (frame > 425 and frame < 475):
            rotateY(PI/4)
            xPos = 0
        if (frame > 500):
            translate(xPos,2*sin(time/0.25),0)
            if (xPos > -150):
                xPos -= 0.75
        iceCreamCone()
        popMatrix()
    
    ##sun
    if (frame > 200):
        pushMatrix()
        translate(35,-40,0)
        scale(0.35,0.35,0.35)
        rotateY(PI/2)
        rotateX(PI/4)
        rotateZ(time/8)
        sun()
        popMatrix()
        pointLight(255,223,0, 35, -1, 0)
        
    ##fridge
    pushMatrix()
    translate(-250,-10,0)
    rotateY(PI/2)
    fridge()
    popMatrix()
        
    
    #####clouds
    topClouds = -45
    bottomClouds = -35
    #going forwards
    if(frame < 300):
        global cloudX
        cloudX += 0.5
        ##cloud1
        if(-45 +cloudX < 25):
            pushMatrix()
            translate(-45 + cloudX, topClouds+ 1.5*sin(time),0)
            cloud()
            popMatrix()
        else:
            pushMatrix()
            ##cloud 1
            translate(25, topClouds + 1.5*sin(time),0)
            cloud()
            popMatrix()
            
            
        #cloud2
        if(-20+cloudX < 30):
            pushMatrix()
            translate(-20 + cloudX, bottomClouds + 2*cos(time),1.5)
            cloud()
            popMatrix()
        else:
            pushMatrix()
            translate(30, bottomClouds + 2*cos(time),1.5)
            cloud()
            popMatrix()
            
        #cloud3
        if(15+cloudX < 35):
            pushMatrix()
            translate(15 + cloudX, topClouds + 2*sin(time),-1.5)
            cloud()
            popMatrix()
        else:
            pushMatrix()
            translate(35, topClouds + 2*sin(time),-1.5)
            cloud()
            popMatrix()
        
        #cloud4
        pushMatrix()
        translate(40, bottomClouds + 1.5*cos(time),0)
        cloud()
        popMatrix()
    ##going backwards
    else:
         global negCloudX
         negCloudX -= 0.125
         pushMatrix()
         translate(25 + negCloudX, topClouds+ 1.5*sin(time),0)
         cloud()
         popMatrix()
        
         pushMatrix()
         translate(30 + negCloudX, bottomClouds + 2*cos(time),1.5)
         cloud()
         popMatrix()
        
         pushMatrix()
         translate(35 + negCloudX, topClouds + 2*sin(time),-1.5)
         cloud()
         popMatrix()
        
         pushMatrix()
         translate(40 + negCloudX, bottomClouds + 1.5*cos(time),0)
         cloud()
         popMatrix()
         
def backgroundScene():
    background(135,206,235)
    
    ##ground
    fill(124,252,0)
    pushMatrix()
    translate(0,10,0)
    rotateX(PI/2)
    box(800,800,0)
    popMatrix()         

def cameraControl():
    global yCamera
    global xCamera
    global zCamera
    if (frame > 0 and frame < 100):
        camera (xCamera,yCamera,zCamera, 0,0, 0, 0, 1 , 0)  # position the virtual camera
        yCamera +=0.5
        xCamera -= 0.75
        # # zCamera -= 0.5
    if (frame > 200 and frame < 250):
        camera(xCamera,yCamera,zCamera,0,0,0,0,1,0)
        zCamera -= 1
        yCamera += 1.2
    if (frame > 550 and frame <700):
        camera(xCamera,yCamera,zCamera,0,0,0,0,1,0)
        zCamera += 1.5
    if (frame > 700 and frame < 850):
        camera(xCamera,0,zCamera,0,0,0,0,1,0)
        xCamera += 1.2
        zCamera -= 1

def lightingControl():
    ambientLight(50, 50, 50);
    lightSpecular(255, 255,2550)
    directionalLight (100, 100, 100, 0, 1, 0)
    noStroke()
    specular (180, 180, 180)
    shininess (15)
    
    
        
