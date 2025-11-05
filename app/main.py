class Animal:
    alive = []
    
    def __init__(self, name):
        self.health = 100
        self.name = name
        self.hidden = False
        
        Animal.alive.append(self)
    
    def die(self):
        if self.health <= 0:
            Animal.alive.remove(self)
    
    def __str__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, herbivore):
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            herbivore.die()
                        
