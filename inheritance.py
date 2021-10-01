class vehicle:
    def general_usage(self):
        print("general usage is trasport")

class car(vehicle):
    def __init__(self):
        print("i am car")
        self.wheel=4
        self.roof= True
        self.general_usage()
    def specific_usage(self):
        print("specific usage:commute to work and for vacation")

class motorcycle(vehicle):
    def __init__(self):
        print("i am motorcycle")
        self.wheel=2
        self.roof= False
        self.general_usage()
    def specific_usage(self):
        print("specific usage: for fun travel")

c = car()
m = motorcycle()
#c.general_usage()
c.specific_usage()
#m.general_usage()
m.specific_usage()
print(isinstance(c,car))
print(issubclass(car,vehicle))