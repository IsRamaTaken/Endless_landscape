from fonction import *

def deplacement_vers(pos_init, pos_final):
    # Donne la direction a prendre  pour aller la position finale
    return signe(pos_final - pos_init)
