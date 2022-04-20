class Car(object):
    def init(self,model,color,company,speedlimit):
        self.color=color
        self.company=company
        self.model=model
        self.speedlimit=speedlimit
    
    def start(self):
        print("Started")
    def stop(self):
        print("Stopped")
    def accelarate(self):
        print("Accelerating")
    def changegear(self,geartype):
        print("Gear Changed")
