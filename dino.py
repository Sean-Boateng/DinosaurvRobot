

class Dinosaur :
    def __init__(self, name, attack_power):
        
        self.name = name
        self.health = 100
        self.atck_pwr = int(attack_power)

    def attack(self, robot):
        self.dino_attack = self.robot.health - self.dinosaur.atck_pwr
        return self.dino_attack
