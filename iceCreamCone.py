# Animation Example
from shapes import *
DETAILS = 25
def iceCreamCone():
    # brown cone
    # fill (139, 69, 19)
    pushMatrix()
    rotateX(-PI/2)
    scale (CONESIZE, CONESIZE, CONESIZE)
    cone()
    popMatrix()
    
    
    #ice cream scoops
    fill (255,255,0)
    pushMatrix()
    translate(13,SCOOPY,0)
    scoop(1)
    popMatrix()
    
    fill (255,105,180)
    pushMatrix()
    translate(-13,SCOOPY,0)
    scoop(1)
    popMatrix()
    

    fill (135,206,250)
    pushMatrix()
    translate(5,SCOOPY,10)
    scoop(1)
    popMatrix()
    

    fill (153,50,204)
    pushMatrix()
    translate(-5,SCOOPY,-10)
    scoop(1)
    popMatrix()
    
    
    fill (255,127,80)
    pushMatrix()
    translate(-8,SCOOPY,10)
    scoop(1)
    popMatrix()
    
    fill (199,21,133)
    pushMatrix()
    translate(8,SCOOPY,-10)
    scoop(1)
    popMatrix()
    
    # top scoop
    fill (0,255,127)
    pushMatrix()
    translate(0,SCOOPY-9,0)
    scoop(1.5)
    popMatrix()
    
    #cherry
    fill (0, 250, 0)
    pushMatrix()
    translate(9,SCOOPY-17,-0.5)
    cherry()
    popMatrix()
def sun():
    ##body
    fill(255,223,0)
    pushMatrix()
    sphereDetail(25)
    rotateX(PI/2)
    sphere(10)
    ## rays
    sides = 8
    for i in range(sides):
        theta = (PI/4)
        rotateY(theta)
        pushMatrix()
        translate(0,0,15)
        rotateX(PI/2)
        box(5,10,1)
        popMatrix()
    popMatrix()
    
def cloud():
    fill(255,255,255)
    ##central puff
    pushMatrix()
    sphereDetail(DETAILS)
    scale(1.5,1,1)
    sphere(6)
    popMatrix()
    
    ##left puff
    pushMatrix()
    sphereDetail(DETAILS)
    translate(-7,0,0)
    scale(2,1.25,1.5)
    sphere(3)
    popMatrix()
    
    ##right Puff
    pushMatrix()
    sphereDetail(DETAILS)
    translate(7,0,0)
    scale(2,1.25,1.5)
    sphere(3)
    popMatrix()

def fridge():
    fill(255,255,255)
    pushMatrix()
    scale(2,2,2)
    box(10,20,5)
    ##opening
    pushMatrix()
    fill(0,0,0)
    translate(0,-6,2.5)
    box(10,8,0)
    popMatrix()
    ##door
    pushMatrix()
    fill(255,255,255)
    rotateY(-PI/2)
    translate(7,-6,4.5)
    box(9,8,1)
    ##handle
    pushMatrix()
    fill(0,0,0)
    translate(3,1,0.7)
    box(1,5,0)
    popMatrix()
    popMatrix()
    fill(0,0,0)
    translate(4,2,2.7)
    box(1,5,0)
    popMatrix()