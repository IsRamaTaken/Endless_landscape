from numpy.random import uniform
import time
from random import randint

def tirage(probabilite):  # marche aléatoire
        return uniform() <= probabilite


def deplacement_t(frame_lecture, lecture, direction_lecture, nombre_de_frame,
                  sens_lecture, nb_frame_min_changement_lecture, probabilite_direction, liste_proba, indice_proba, compteur_de_frame):

        duree_lecture_changement = compteur_de_frame - frame_lecture
        if lecture >= 0 and lecture <= nombre_de_frame - 1 and \
                duree_lecture_changement > nb_frame_min_changement_lecture:

                # Tirage tête de lecture
                tirage_sens_lecture = tirage(liste_proba[indice_proba])
                tirage_direction_lecture = tirage(probabilite_direction)

                if tirage_sens_lecture:
                        sens_lecture = -sens_lecture
                        frame_lecture = compteur_de_frame

                if tirage_direction_lecture:
                        sens_lecture = direction_lecture
                        frame_lecture = compteur_de_frame

        return lecture, sens_lecture, direction_lecture, frame_lecture


def changement_proba(temps_changement_proba,temps_entre_changement_proba, indice_proba, liste_proba):
    if time.time() - temps_changement_proba > temps_entre_changement_proba:
        temps_changement_proba = time.time()
        indice_proba = randint(0,len(liste_proba)-1)
    return indice_proba, temps_changement_proba







