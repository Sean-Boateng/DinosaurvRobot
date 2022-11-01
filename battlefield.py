


from dino import Dinosaur
from robot import Robot


class Battlefield() :
    def __init__(self):
        self.robot = Robot(input("what is your name?"))
        self.dinosaur = Dinosaur(input("what is your name?"),input("what is your attack power?") )

    def run_game(self):
        pass

    def display_welcome(self):
        print("Welcome to the Battle of the centuty.")
        print("Are you ready "+ self.robot.name + "?")
        print("Are you ready "+ self.dinosaur.name + "?")
        print("Fight!!!")

   

    def battle_phase(self):
        can_continue = False
        while can_continue is False:
            self.dinosaur.health = self.dinosaur.health - self.robot.active_weapon.atck_pwr
            
            self.robot.health= self.robot.health - self.dinosaur.atck_pwr

            
        
            if self.robot.health <= 0 or self.dinosaur.health <= 0:
                can_continue = True
                print("Battle Over")
                break
            else:
                print("Again")
            
            
    

        
        
        
        
        
       

    def display_winner(self):
        if self.robot.health <= 0 and self.dinosaur.health >= 0:
            print(self.dinosaur.name +"Wins!!")
        elif self.dinosaur.health <= 0 and self.robot.health >= 0:
            print(self.robot.name + "Wins!!!")
        


        
