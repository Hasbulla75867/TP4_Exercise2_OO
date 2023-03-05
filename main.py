"""
Programme fait par Raul Mic Nicolas
TP4 : Introduction à la programmation OO
Écrire une classe Rectangle qui reçoit la largeur ainsi que la longueur comme paramètre dans la méthode __init__.
Écrire une méthode calcul_aire qui permet de calculer l’aire du rectangle (elle n’affiche rien à l’écran).
Écrire aussi une méthode afficher_infos qui permet d’afficher les caractéristiques du rectangle (largeur,longueur,aire).
"""


class Rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur
        self.aire = 0

    def calculer_aire(self):
        self.aire = self.largeur * self.longueur
        return self.aire

    def afficher_infos(self):
        self.aire = self.calculer_aire()
        print(f"L'aire du rectangle avec une longueur de {self.longueur} et une largeur de {self.largeur} "
              f"est égale à {self.aire}")


rectangle = Rectangle(524, 750)
rectangle.afficher_infos()
