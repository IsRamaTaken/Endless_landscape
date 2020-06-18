from numpy.random import uniform
from random import randint
from math import *

def signe(z):
    if z>=0:
        return(1)
    else:
        return(-1)

def conversionvitesse(clock,vitesse_x,vitesse_y,vzoom,framerate): # convertit le vitesse en pixel par image ou en niveau de zoom par image
    fps=clock.get_fps()
    if fps<0.5: fps=framerate
    return vitesse_x/fps,vitesse_y/fps,vzoom/fps

def tirage(probabilite):  # marche aléatoire
    return uniform() <= probabilite

def changement_proba(temps_changement_proba,temps_entre_changement_proba, indice_proba, liste_proba,compteur_de_frame):
    if compteur_de_frame - temps_changement_proba > temps_entre_changement_proba:
        temps_changement_proba = compteur_de_frame
        indice_proba = randint(0,len(liste_proba)-1)
    return indice_proba, temps_changement_proba

def saut_image(vitesse_x,vitesse_y,pos_xdebut,pos_ydebut,posx,posy,seuil=0.0001):
    return ( abs(abs(pos_xdebut-posx)-vitesse_x)>seuil )or ( abs(abs(pos_ydebut-posx)-vitesse_y)>seuil )