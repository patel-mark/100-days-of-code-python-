class toycar:
    
    def __init__(self,color,speed):
        
        self.color=color #attribute
        self.speed=speed #attribute
        
    def drive(self):  #method
        print(f"The {self.color} car moves at a speed of {self.speed}")
        
        
car=toycar('grey','80khm')

car.drive()
