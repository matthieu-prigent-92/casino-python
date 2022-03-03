"""Petit jeu de casino : la roulette"""
# -*-coding:utf-8 -*

# import des modules nécessaires
# fonction permettant de générer un nombre aléatoire
from random import randrange
# fonction permettant d'arrondir au nombre supérieur
from math import ceil
import os

# début du programme
print("Bienvenue à ZCasino !")
print("\nLe jeu de la roulette revisité !!!\n")

mise_totale = int(input("indiquez le montant de votre mise de départ : "))
print("""Vous devez choisir un numéro compris entre 0 et 49, 
ensuite vous choisirez combien vous souhaitez parier.\n
Attention à ne pas parier plus que votre mise totale !\n""")
# début de la boucle
while mise_totale > 0:
    try:
        numero = int(input("\nfaites vos jeux !\nVotre numéro : "))
        assert numero >= 0 and numero < 50
    except ValueError:
        print("Vous n'avez pas saisi de numéro")
        continue
    except AssertionError:
        print("Vous n'avez pas saisi un nombre entre 0 et 49")
        continue

    try:
        mise = int(input("Votre mise : "))
        assert mise <= mise_totale
    except ValueError:
        print("Vous n'avez pas saisi de numéro")
        continue
    except AssertionError:
        print("Vous ne pouvez pas miser autant, vous n'avez que $", mise_totale)
        continue
    #print("\nVous avez parié sur le ", numero)
    roulette = int(randrange(50))
    print("\nLes jeux sont faits ! ... ... Le numéro gagnant est le", roulette)
    #print("... ...")

    #print("Le numéro gagnant est le ", roulette, ".")
    # test du numéro gagnant et du numéro parié
    # test si les 2 numéros sont identiques
    if roulette == numero: 
        # on triple la mise et on l'ajoute à la mise totale
        mise_totale += (3*mise)
        print("\nBravo, vous avez triplé votre mise !")
        print("\nVous gagnez $", mise*3)
        print("\nVotre gain total est de : $",mise_totale)
    # test si les numéros sont pairs ou impairs
    elif (roulette%2) == (numero%2):
        # on ajoute la moitié de la mise à la mise totale
        mise_totale += ceil(mise/2)
        print("\nBravo, vous avez gagné la moitié de votre mise !")
        print("\nVous gagnez $", ceil(mise/2))
        print("\nVotre gain total est de : $",mise_totale)
    # sinon les 2 numéros sont différents
    else: 
        # on retire la mise de la mise totale  
        mise_totale -= mise
        print("\nDésolé, vous avez perdu votre mise !")
        print("\nVous perdez $", mise)
        print("\nVotre gain total est de : $",mise_totale)
# fin de la boucle
print("\nMerci d'avoir joué. A bientôt !")
os.system("pause")