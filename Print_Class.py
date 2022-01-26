from Robot_Class import *

class Affichage :
    """
    Initialize
    """
    def __init__(self, robotImport, arenaImport) :
        self.robotSaved:Robot = robotImport
        self.arenaSaved:Arena = arenaImport

    def afficher(self) :
        res = " " + "-" * self.arenaSaved.xMax + "\n"
        for yi in range(self.arenaSaved.yMax-1,-1,-1) :
            res += str(yi)
            for xi in range(self.arenaSaved.xMax) :
                if (xi <= self.robotSaved.x and xi+1 > self.robotSaved.x and yi <= self.robotSaved.y and yi+1 > self.robotSaved.y) :
                    res += "O"
                else :
                    res += " "
            res += "|\n"
        res += " " + "-" * self.arenaSaved.xMax
        return res

robot0 = Robot(5,5,4)
arena0 = Arena(50, 10)

affichage0 = Affichage(robot0, arena0)

print(affichage0.afficher())

robot0.speed_up(1.5)
robot0.move_forward()
robot0.move_forward()
robot0.move_forward()

print(affichage0.afficher())
robot0.rotate_left(45)
robot0.move_forward()
robot0.move_forward()
robot0.move_forward()
print(affichage0.afficher())
