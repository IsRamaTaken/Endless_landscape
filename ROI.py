from fonction import *

def deplacement_vers(pos_init, pos_final):
    # Donne la direction a prendre  pour aller la position finale
    return signe(pos_final - pos_init)


def changement_cible(liste_cible, temps_ROI, temps_ROI_min, temps_ROI_max, compteur_de_frame):

    # On initialise a nouveau les variables pour le prochain changement
    temps_ROI_arrive = compteur_de_frame
    temps_ROI = randint(temps_ROI_min, temps_ROI_max - 1)
    ROI_en_attente = True
    indice = randint(0, len(liste_cible) - 1)
    posXcible, posYcible, lecture_cible = liste_cible[indice]
    
    return posXcible, posYcible, lecture_cible, temps_ROI_arrive, temps_ROI, ROI_en_attente
