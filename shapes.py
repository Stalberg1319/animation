SCOOPSIZE = .7
SCOOPY = -12
CONESIZE = 13
SCOOPRADIUS = 10
SPRINKLESIZE = 0.5

# cone with radius = 1, z range in [-1,1]
def cone(sides = 64):
     # opening
     beginShape()
     for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
     endShape(CLOSE)
     # vertex
     beginShape()
     for i in range(sides):
         theta = i * 2 * PI / sides
         x = cos(theta)
         y = sin(theta)
         vertex ( x/50,  y/50, 1)
     endShape(CLOSE)
     # sides
     x1 = 1
     y1 = 0
     for i in range(sides):
        if (i % 5 == 0):
            fill(244,164,96)
        else: 
            fill (139, 69, 19)
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1/50, y1/50, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2/50, y2/50, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2
    
def scoop(size):
    scale(SCOOPSIZE*size,SCOOPSIZE*size,SCOOPSIZE*size)
    sphereDetail(30)
    sphere(SCOOPRADIUS)
    sides = 40
    for i in range(sides):
        theta = i * PI/sides
        rotateX(theta)
        pushMatrix()
        translate(0,0,SCOOPRADIUS)
        # fill(255,0,0)
        sprinkle()
        popMatrix()
        rotateY(theta)
        pushMatrix()
        translate(0,0,SCOOPRADIUS)
        fill(255,0,0)
        sprinkle()
        popMatrix()
    

def cherry():
    fill(255,0,0)
    scoop(0.25)
    pushMatrix()
    stem()
    popMatrix()
    
def stem():
    translate(5,-5,0.5)
    scale(1,-5,1)
    rotateZ(-PI/4)
    box(1,7,1)


def sprinkle():
    fill(random(255),random(255),random(255))
    scale(SPRINKLESIZE,SPRINKLESIZE,SPRINKLESIZE)
    box ( 1, 5 , 0)