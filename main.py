import numpy as np
from deplacement_tete_de_lecture import deplacement_t, changement_proba
from cadre_manuel import deplacement_manuel, chgmt_indice_vitesse_manuel
from cadre_automatique import deplacement_automatique_x_y
from random import choice
from zoom import *

from initialisation_parametres import *
from keyboard_config_file_update import assignment_menu
from fonction import *
from deplacement_souris import *
from ROI import *


if sens % 2 == 0:
    screen = pygame.display.set_mode((size_y, size_x))
elif sens % 2 == 1:
    screen = pygame.display.set_mode((size_x, size_y))


if fullscreen:
    pygame.display.set_mode(modes[0], pygame.FULLSCREEN)

    # On déplace la souris de telle maniere a ne plus la voir:
    deplacement_souris()

pygame.key.set_repeat(100, 100)

running = True


"""   Début de la boucle infini de choix d'image et d'affichage   """

clock = pygame.time.Clock()
tempsDureeMouvement=0
compteurAttente=1
compteur_de_frame=1
tchangement=0
posXatteint=True
posYatteint=True


while running:



    clock.tick(framerate)


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_F1:
                input_map = assignment_menu(input_map, screen)
                screen.fill((0, 0, 0))

    if posXatteint and posYatteint:
        compteurAttente+=1

    if compteurAttente>=tempsDureeMouvement:
        tempsDureeMouvement=uniform(tmin,tmax)
        VzoomPossible=[]
        size_window_x = int(size_x / Zt)
        size_window_y = int(size_y / Zt)
        vitesse_actuelle_x=choice(vitesse_x)
        vitesse_actuelle_y=choice(vitesse_y)
        #selection position
        posXmin= size_window_x //2 + 2 - size_x % 2
        posXmax=int(limite_up_x-1-size_window_x/2)-1
        posYmin =  size_window_y // 2+2
        posYmax = limite_up_y-1-size_window_y//2-1

        posXfinal=int(uniform(posXmin,posXmax))
        print(posYmin,posYmax)
        posYfinal = int(uniform(posYmin, posYmax))
        tchangement=compteur_de_frame
        compteurAttente=0




        if not type_zoom:
            # ZOOM AUTO

            probaZoom,probaDezoom,sens_deplacement_x, direction_deplacement_x,sens_deplacement_y,direction_deplacement_y,temps_debut_zoom, directionZoom, zinit, zf, indice_zoom, zoom_en_cours_Auto, temps_changement_zoom, Zt \
                    = zoom_automatique(probaZoom,probaDezoom,sens_deplacement_x, direction_deplacement_x,sens_deplacement_y,direction_deplacement_y,Zt, vitesse_actuelle_x, vitesse_actuelle_y, vzoom, posX, posY, size_x, size_y, limite_up_x,
                                       limite_up_y, temps_debut_zoom,listZoomAuto, directionZoom, zinit, zf, indice_zoom, zoom_en_cours_Auto,\
                                       temps_changement_zoom, attente_min, attente_max,compteur_de_frame)

    size_window_x=int(size_x/Zt)
    size_window_y=int(size_y/Zt)





    if lecture <= 0:
            lecture = 0
            sens_lecture = 1
            direction_lecture = 1
    elif lecture >= nombre_de_frame - 1:
            lecture = nombre_de_frame - 1
            sens_lecture = -1
            direction_lecture = -1

    print(posXatteint,posYatteint)



    # Déplacement de la tete de lecture et du cadre dans le cas du déplacement vers les points d'interets:


        
    if not posXatteint:
        posX += deplacement_vers(posX,posXfinal) * vitesse_actuelle_x
        if abs(posX - posXfinal) <= vitesse_actuelle_x:
            posX = posXfinal
        posXatteint = (posX == posXfinal)

    if not posYatteint:
        posY += deplacement_vers(posY, posYfinal) * vitesse_actuelle_y
        if abs(posY - posYfinal) <= vitesse_actuelle_y:
            posY = posYfinal

        posYatteint = (posY == posYfinal)



    posXatteint = (posX == posXfinal)
    posYatteint = (posY == posYfinal)







    img = frame_list[lecture]
    img = img[posY - size_window_y //2 + 1 - size_y % 2 :posY + size_window_y // 2, posX - size_window_x //2 +1 -size_x%2:posX + size_window_x //2 ]

    img = cv2.resize(img, (size_x, size_y))
    
    """On ajoute l'image a la vidéo enregistrée si on a choisit de le faire"""
    if enregistrement:
        video_output.write(img)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    frame = np.rot90(img, sens)
    frame = pygame.surfarray.make_surface(frame)
    frame = pygame.transform.flip(frame, True, False)
    frame_rect=frame.get_rect()

    if fullscreen:
        screen.blit(frame, (accroche_x, accroche_y))
    else:
        screen.blit(frame, (0, 0))

    pygame.display.update()
    compteur_de_frame+=1


cv2.destroyAllWindows()
pygame.quit()

