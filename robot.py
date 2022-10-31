

from weapon import Weapon


class Robot :
    def __init__(self, name):
        
        self.name = name
        self.health = 100
        self.active_weapon = Weapon(input("What is your weapon?"))

    def attack(self,dinosaur): 
        # robot attack power value minus from dinosaur health
        self.robot_attack = self.dinosaur.health - self.robot.active_weapon.atck_pwr
        return self.robot_attack
        

    
        
