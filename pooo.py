# les class

class Chienf:
    pass

## un objet, une instance

mon_chien = Chienf()

type(mon_chien)  # <class '__main__.Chien'>


### les attributs, information propre à chaque objet

class Chien:
    def __init__(self, nom, race):
        self.nom = nom
        self.race = race
    def aboyer(self):
        print(f"{self.nom} dit Woaf Woaf!")

Chiens = Chien("pipo", "Berger Allemand")

rex = Chien("Rex", "Labrador")

print(rex.aboyer())  # Rex dit Woaf Woaf!



## les methodes, fonctions propres à une classe, les fonctions des objets