from numpy.random import uniform
import time
from random import randint

def tirage(probabilite):  # marche aléatoire
        return uniform() <= probabilite


def deplacement_t(temps_lecture, lecture, direction_lecture, nombre_de_frame,
                  sens_lecture, temps_min_changement_t, probabilite_direction, liste_proba, indice_proba):

        duree_lecture_changement = time.time() - temps_lecture
        if lecture >= 0 and lecture <= nombre_de_frame - 1 and \
                duree_lecture_changement > temps_min_changement_t:

                # Tirage tête de lecture
                tirage_sens_lecture = tirage(liste_proba[indice_proba])
                tirage_direction_lecture = tirage(probabilite_direction)

                if tirage_sens_lecture:
                        sens_lecture = -sens_lecture
                        temps_lecture = time.time()

                if tirage_direction_lecture:
                        sens_lecture = direction_lecture
                        temps_lecture = time.time()

        return lecture, sens_lecture, direction_lecture, temps_lecture


def changement_proba(temps_changement_proba,temps_entre_changement_proba, indice_proba, liste_proba):
    if time.time() - temps_changement_proba > temps_entre_changement_proba:
        temps_changement_proba = time.time()
        indice_proba = randint(0,len(liste_proba)-1)
    return indice_proba, temps_changement_proba







