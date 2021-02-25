class Animal:
    def __init__(self,species,order,sound,age):
        self.species = species
        self.order = order
        self.sound = sound
        self.age = age
    def getSpecies(self):
        return self.species
    def getOrder(self):
        return self.order
    def getSound(self):
        return self.sound
    def getAge(self):
        return self.age
animal1 = Animal ("Snake","Carnivore","Hisses","17")
print(animal1.getSpecies())
print(animal1.getOrder())
print(animal1.getSound())
print(animal1.getAge())