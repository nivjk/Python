
# Créer le 22 mai 2023
# par Nivetha Jeyakumar
# Master IRS P33
# 
# C vs Python


class Sorcier:
    def __init__(self, nom, maison, vole):
        self.nom = nom
        self.maison = maison
        self.vole = vole

    def vol(self):
        print(f"\n{self.nom} a rejoint la maison {self.maison}.")

        if self.vole == 1:
            print(f"{self.nom} peut s'envoler avec son balai magique.")
        else:
            print(f"{self.nom} n'a pas réussi à s'envoler avec son balai magique.")

# Création des instances de sorciers
harry = Sorcier("Rogue", "Serpentard", 1)
ron = Sorcier("Bellatrix", "Serpentard", 1)
nivetha = Sorcier("Nivetha", "Poufsouffle", 0)

# Appel des méthodes pour afficher les informations des sorciers
harry.vol()
ron.vol()
nivetha.vol()