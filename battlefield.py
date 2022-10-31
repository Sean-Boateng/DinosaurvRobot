

from os import name
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
        print("Are you ready "+ self.robot.name)
        print("Are you ready "+ self.dinosaur.name)
        print("Fight!!!")

        

    def battle_phase(self):
        # robo_move = self.robot.attack(self.dinosaur)
        Robot.attack(self, dinosaur="")
        Dinosaur.attack(self , robot="")
        
        
        
       

    def display_winner(self):
        if self.robot.robot_attack <= 0 and self.dinosaur.dino_attack >= 0:
            print(self.robot.name +"Wins!!")
        elif self.dinosaur.dino_attack <= 0 and self.robot.robot_attack >= 0:
            print(self.dinosaur.name + "Wins!!!")
        else:
            Battlefield.battle_phase(self)
        
