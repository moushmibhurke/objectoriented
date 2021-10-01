class father():
    def skills(self):
        print("computers and cooking")

class mother():
    def skills(self):
        print("gardening and home decorating")

class child(father,mother):
    def skills(self):
        father.skills(self)
        mother.skills(self)
        print("sports")

c=child()
c.skills()
