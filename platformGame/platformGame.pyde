class player(object):
    def __init__(self):
        self.x =300
        self.y =300
        self.up =0
        self.down =0
        self.left =0
        self.right =0
        self.speed=3
        self.speed2=8
        
    def show(self):
        fill(0)
        #rect(self.x,self.y,20,20)
       # img = loadImage("Android_robot.png")
       # image(img,self.x,self.y)
        img = loadImage("Character_Creator_Trial_Hub.exe")
        image(img,self.x,self.y)
       
    def update(self):
        self.x = self.x +(self.right- self.left)*self.speed
        self.y = self.y +(self.down - self.up)*self.speed2
      #  if self.speed2 
def setup():
    size (922,615)
    img = loadImage("level1-house.jpg")
    image(img, 0, 0)

    global p
    p=player()
    
  
      
def draw():
   # background(100)
    img = loadImage("level1-house.jpg")
    image(img, 0, 0)
    p.show()
    p.update()
    
def keyPressed():
    if keyCode == UP:
        p.up =1
    if keyCode == DOWN:
        p.down =1
    if keyCode == LEFT:
        p.left =1
    if keyCode == RIGHT:
        p.right =1
        
def keyReleased():
    if keyCode == UP:
        p.up =0
    if keyCode == DOWN:
        p.down =0
    if keyCode == LEFT:
        p.left =0
    if keyCode == RIGHT:
        p.right =0
