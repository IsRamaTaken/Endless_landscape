from random import randint
from preparation_video import *

#Position initiale de la tete de lecture
lecture = randint(0, nombre_de_frame-1)
indice_proba = 0


""" Initialisation des paramètres de la vitesse de déplacement du cadre """

# Initialisation de l'indice de la vitesse de  déplacement du cadre:

indice_vitesse_x = randint(0, len(vitesse_x)-1)
indice_vitesse_y = randint(0, len(vitesse_y)-1)

# Initialisation des vitesses actuelles et initiales en x et y:
vitesse_actuelle_x = vitesse_x[indice_vitesse_x]
vitesse_actuelle_y = vitesse_y[indice_vitesse_y]
vitesse_initiale_x = vitesse_actuelle_x
vitesse_initiale_y = vitesse_actuelle_y

# Initialisation du temps entre chaque changement de vitesse :
temps_chgmt_indice_x = 0
temps_chgmt_indice_y = 0

# Initialisation des variables de suivi du changement de vitesse
chgmt_vitesse_x_en_cours = False
chgmt_vitesse_y_en_cours = False

# Initialisation des premières frames pour le changement de vitesse
frame_chgmt_x = 0
frame_chgmt_y = 0

# Initialisation des valeurs du nombre de frame toute les combiens il faut incrémenter la valeur de 
# la vitesse de déplacement du cadre lors d'un changement de vitesse (pour un changement progressif)

nb_frame_incrementation_vitesse_x = 1
nb_frame_incrementation_vitesse_y = 1

diff_vitesse_x = 0
diff_vitesse_y = 0

""" Fin de l'initialisation des paramètres de la vitesse de déplacement du cadre """


#Initialisation de la taille de la fenêtre
size_window_x = size_x
size_window_y = size_y

#Choix de la position initiale du cadre selon x:
if limite_up_x - size_window_x + 1 == 0:
    posX = size_window_x//2 + size_window_x%2 -1
elif limite_up_x - size_window_x + 1 < 0:
    print("!!!! Le cadre est trop grand pour la taille de la vidéo originale !!!!")
else:
    posX = randint(size_window_x//2 + size_window_x % 2 - 1, limite_up_x - size_window_x//2)


#Choix de la position initiale du cadre selon y:
if limite_up_y - size_window_y + 1 == 0:
    posY = size_window_y // 2 + size_window_y % 2-1
elif limite_up_y - size_window_y + 1 < 0:
    print("!!!! Le cadre est trop grand pour la taille de la vidéo originale !!!!")
else:
    posY = randint(size_window_y//2 + size_window_y%2 -1 , limite_up_y - size_window_y//2)



#Temps que le cadre va rester sur les bords la premiere fois qu'il les touche:
temps_restant_bord_x = randint(temps_min_x, temps_max_x)
temps_restant_bord_y = randint(temps_min_y, temps_max_y)

if enregistrement:#Création de la vidéo de sortie (l'enregistrement), vide pour le moment, on ajoute les images apres
    codec = cv2.VideoWriter_fourcc(codec[0], codec[1], codec[2], codec[3])
    video_output = cv2.VideoWriter(output_file, codec, framerate, (size_x, size_y))
    if video_output.isOpened():
        print("L'objet vidéo a bien été initialisée")
    else:
        print("!!!! L'objet vidéo n'a pas pu etre initialisé !!!!")

"""
Sens  lecture (ou sens_deplacement) correspond au sens dans lequel la tete de lecture (ou le cadre) va 
effectivement se déplacer tandis que direction_lecture (ou direction_deplacement) indique la direction privilégiée 
de lecture (ou déplacement). Toutes ces valeurs vont etre modifiées tout au long du programme
Ici in procède a l'initiation de ces variables en fonction des positions de la tete de lecture
et du cadre.
"""

if lecture == nombre_de_frame:
    sens_lecture = -1
    direction_lecture = -1
else:
    sens_lecture = 1
    direction_lecture = 1

if posX == limite_up_x - size_window_x//2:
    sens_deplacement_x = -1
    direction_deplacement_x = -1
else:
    sens_deplacement_x = 1
    direction_deplacement_x = 1

if posY == limite_up_y - size_window_y//2:
    sens_deplacement_y = -1
    direction_deplacement_y = -1
else:
    sens_deplacement_y = 1
    direction_deplacement_y = 1

"""postion réelle en float permet d'actualiser plus régulièrement le déplacement pour avoir une vidéo plus fluide"""
pos_x_reel = posX
pos_y_reel = posY

"""permet de savoir si le bord est atteint:"""
bord_atteint_x = posX== size_window_x//2 + size_window_x%2 -1 or posX== limite_up_x - size_window_x//2
bord_atteint_y = posY== size_window_y//2 + size_window_y%2 -1 or posY== limite_up_y - size_window_y//2

"""Variables servant uniquement lors du premier contact en x ou y:"""
bord_atteint_x_debut = True
bord_atteint_y_debut = True


deplacement_automatique = True
compteur_de_frame = 0

#Initialisation des temps:

temps_x_changement=0      #permet de calculer la durée qui s'est écoulé entre de changement de direction de déplacement du cadre selon x

temps_y_changement=0       #permet de calculer la durée qui d'est écoulé entre de changement de direction de déplacement du cadre selon y

debut_bord_x = 0          #Permet de calculer la durée que reste le cadre ur le bord de l'image en x
debut_bord_y = 0          #Permet de calculer la durée que reste le cadre ur le bord de l'image en y
temps_changement_zoom=0   #permet de calculer la durée qui s'est écoulé avant le zoom précédent
temps_debut_zoom=0
temps_changement_proba = 0

# Initialisation de frame_lecture pour le premier changement de sens de t
frame_lecture = 0



#Initialisation Zoom:

zoom_en_cours_Auto = False
zoom_en_cours_manuel = False
zmin = max([size_x/limite_up_x, size_y/limite_up_y])
listZoomAuto = [zmin+k*(zmax-zmin)/9 for k in range(10)]
indiceZoomDefault=0
while listZoomAuto[indiceZoomDefault] < 1:        #placer le zoom 1 dans la liste
    indiceZoomDefault += 1
indiceZoomDefault -= 1
listZoomAuto[indiceZoomDefault] = 1
indice_zoom = indiceZoomDefault
listZoomManuel = [1]+listZoomAuto[:indiceZoomDefault]+listZoomAuto[indiceZoomDefault+1:]
zinit = 1
zf = 1
Zt = zinit
directionZoom = 1

deplacement_automatique = True
compteur_de_frame = 0

arret_x = False
arret_y = False

modes = pygame.display.list_modes()
if sens % 2 == 1:
    accroche_x = (modes[0][0] - size_x) / 2
    accroche_y = (modes[0][1] - size_y) / 2
else:
    accroche_x = (modes[0][0] - size_y) / 2
    accroche_y = (modes[0][1] - size_x) / 2


""" Initialisation des paramètres relatifs au ROI """

indice_point_ds_PI = 0 # indice du point (t, x, y) dans un point d'interet
indice_PI = "PI_0" # indice du point d'interet dans le dictionnaire des PI

premier_passage_point = True
frame_point_ds_PI = 0
direction_ds_PI = 1
sens_ds_PI = 1

amplitude_min = 0
amplitude_max = nombre_de_frame - 1

# temps que l'on reste sur un point d'interet une fois atteint:
temps_ROI = randint(temps_ROI_min, temps_ROI_max - 1)

# numero de la frame a laquelle on a atteint un point d'interet:
temps_ROI_arrive = 0


""" Fin de l'initialisation du ROI"""


"""   Fin de l'initialisation   """
