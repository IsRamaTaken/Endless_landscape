
from fonction import *


def deplacement_automatique_x_y( pos, sens_deplacement, direction_deplacement,
                                vitesse, limite_up, size, bord_atteint, bord_atteint_debut, debut_bord,
                                temps_restant_bord, temps_min, temps_max, temps_min_changement,
                                probabilite_changement_sens, probabilite_changement_selon_direction,
                                temps_changement, compteur_frame):
    if not bord_atteint:
        duree_changement = compteur_frame - temps_changement
        if duree_changement > temps_min_changement:
            tirage_sens = tirage(probabilite_changement_sens)
            tirage_direction = tirage(probabilite_changement_selon_direction)
            if tirage_sens:
                sens_deplacement = - sens_deplacement
                temps_changement = compteur_frame
            if tirage_direction:
                sens_deplacement = direction_deplacement
                temps_changement = compteur_frame

        pos += sens_deplacement * vitesse

        bord_atteint = pos<= size//2 + size%2 -1 or pos>= limite_up - size//2
    else:
        if bord_atteint_debut:
            debut_bord = compteur_frame
            bord_atteint_debut = False
            direction_deplacement = - direction_deplacement
        duree_bord_atteint = compteur_frame - debut_bord
        if duree_bord_atteint > temps_restant_bord:
            if pos == size//2 +size%2 -1:
                sens_deplacement = 1
            elif pos == limite_up - size//2:
                sens_deplacement = -1
            bord_atteint = False
            bord_atteint_debut = True
            temps_restant_bord = randint(temps_min, temps_max)

    if pos <= size//2 + size % 2 - 1:
        pos = size//2 + size % 2 - 1
    elif pos > limite_up - size//2:
        pos = limite_up - size//2
    return pos, sens_deplacement, direction_deplacement,\
           bord_atteint, bord_atteint_debut, temps_restant_bord, debut_bord, temps_changement
