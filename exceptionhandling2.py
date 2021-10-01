class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
    def handle(self):
        print("exception occured")

try:
    raise Accident("car crash between two cars")
except Accident as e:
    e.handle()