class Person:
    def __init__(self,initialAge):
        self.initialAge = initialAge
        if initialAge < 0:
            return ( "Age not valid and set to 0")
            self.age = 0
        else:
            self.age = initialAge
    
    def amIOld(self):
        if self.age < 13:
            return "you are old"
        elif self.age < 18:
            return "You are young"
        else:
            return "You are old"

    def yearPasses(self):
        self.age += 1

p = Person(8)
print(p.amIOld())
