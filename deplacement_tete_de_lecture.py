
from fonction import *
from random import randint



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


