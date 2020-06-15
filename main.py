import numpy as np
from deplacement_tete_de_lecture import deplacement_t, changement_proba
from cadre_manuel import deplacement_manuel
from cadre_automatique import deplacement_automatique_x_y

from zoom import *

from initialisation_parametres import *
from keyboard_config_file_update import assignment_menu
from matplotlib import pyplot as plt
from deplacement_souris import *

listposX=[]
listposY=[]
listtemps=[]

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

while running:

    clock.tick(framerate)


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_F1:
                input_map = assignment_menu(input_map, screen)
                screen.fill((0, 0, 0))



    keys = pygame.key.get_pressed()

    # condition de fermeture

    if keys[input_map["mode_automatique"]]:
        manuel_auto = 0
        type_deplacement_cadre = 0
        type_deplacement_tete = 0
        type_zoom = 0
        temps_x, temps_y = time.time(), time.time()


    elif keys[input_map["mode_manuel"]]:
        manuel_auto = 1
        type_deplacement_cadre = 1
        type_deplacement_tete = 1
        type_zoom = 1
        temps_x,temps_y=time.time(),time.time()


    if keys[input_map["stop_cadre_x"]]:
        sens_deplacement_x = 0
        arret_x = True

    if keys[input_map["stop_cadre_y"]]:
        sens_deplacement_y = 0
        arret_y = True

    posX_debut=posX

    #ZOOM
    if choix_zoom_ou_non:
        if not type_zoom:
            # ZOOM AUTO
            if zoom_en_cours_manuel:
                Zt, indice_zoom, temps_debut_zoom, zinit, zf, zoom_en_cours_manuel = \
                    Zoom_Manuel(Zt, vitesse_x, vitesse_y, vzoom, posX, posY, size_x, size_y, limite_up_x, limite_up_y,
                                temps_debut_zoom, listZoomManuel, \
                                zinit, zf, zoom_en_cours_manuel, indice_zoom, indiceZoomDefault, keys, input_map)

            else:
                sens_deplacement_x, direction_deplacement_x,sens_deplacement_y,direction_deplacement_y,temps_debut_zoom, directionZoom, zinit, zf, indice_zoom, zoom_en_cours_Auto, temps_changement_zoom, Zt \
                    = zoom_automatique(sens_deplacement_x, direction_deplacement_x,sens_deplacement_y,direction_deplacement_y,Zt, vitesse_x, vitesse_y, vzoom, posX, posY, size_x, size_y, limite_up_x,
                                       limite_up_y, temps_debut_zoom,listZoomAuto, directionZoom, zinit, zf, indice_zoom, zoom_en_cours_Auto,\
                                       temps_changement_zoom, attente_min, attente_max)


         #ZOOM MANUEL
        else:
            if zoom_en_cours_Auto:
                sens_deplacement_x, direction_deplacement_x, sens_deplacement_y, direction_deplacement_y, temps_debut_zoom, directionZoom, zinit, zf, indice_zoom, zoom_en_cours_Auto, temps_changement_zoom, Zt \
                    = zoom_automatique(sens_deplacement_x, direction_deplacement_x, sens_deplacement_y,
                                       direction_deplacement_y, Zt, vitesse_x, vitesse_y, vzoom, posX, posY, size_x,
                                       size_y, limite_up_x,
                                       limite_up_y, temps_debut_zoom, listZoomAuto, directionZoom, zinit, zf,
                                       indice_zoom, zoom_en_cours_Auto, \
                                       temps_changement_zoom, attente_min, attente_max)
            else:

                Zt, indice_zoom, temps_debut_zoom, zinit, zf, zoom_en_cours_manuel = \
                    Zoom_Manuel(Zt, vitesse_x, vitesse_y, vzoom, posX, posY, size_x, size_y, limite_up_x, limite_up_y,
                                temps_debut_zoom,listZoomManuel,\
                                zinit, zf, zoom_en_cours_manuel, indice_zoom, indiceZoomDefault, keys, input_map)




    size_window_x=int(size_x/Zt)
    size_window_y=int(size_y/Zt)

    if posX!=posX_debut:
        print('salut')
    #deplacement cadre:
    if choix_cadre:
        if type_deplacement_cadre:
            arret_x,arret_y,temps_x, temps_y, posX, pos_x_reel, sens_deplacement_x, bord_atteint_x, posY, pos_y_reel, sens_deplacement_y, bord_atteint_y= \
                deplacement_manuel(arret_x,arret_y,temps_x,temps_y, posX, sens_deplacement_x, limite_up_x, size_window_x, vitesse_x, posY,
                                   sens_deplacement_y, limite_up_y, size_window_y, vitesse_y, pos_x_reel, pos_y_reel, keys,
                                   input_map)

        else:
            if not arret_x:
                posX, pos_x_reel, temps_x, sens_deplacement_x, direction_deplacement_x, bord_atteint_x, \
                bord_atteint_x_debut, temps_restant_bord_x, debut_bord_x, temps_x_changement = deplacement_automatique_x_y(
                    temps_x, posX, pos_x_reel, sens_deplacement_x, direction_deplacement_x, vitesse_x, limite_up_x,
                    size_window_x, bord_atteint_x, bord_atteint_x_debut, debut_bord_x, temps_restant_bord_x,
                    temps_min_x, temps_max_x, temps_min_changement_x, probabilite_changement_sens_x,
                    probabilite_changement_selon_direction_x, temps_x_changement)

            if not arret_y:
                posY, pos_y_reel, temps_y, sens_deplacement_y, direction_deplacement_y, bord_atteint_y, \
                bord_atteint_y_debut, temps_restant_bord_y, debut_bord_y, temps_y_changement = deplacement_automatique_x_y(
                    temps_y, posY, pos_y_reel, sens_deplacement_y, direction_deplacement_y, vitesse_y, limite_up_y,
                    size_window_y, bord_atteint_y, bord_atteint_y_debut, debut_bord_y, temps_restant_bord_y,
                    temps_min_y, temps_max_y, temps_min_changement_y, probabilite_changement_sens_y,
                    probabilite_changement_selon_direction_y, temps_y_changement)

    if choix_t:
        if not type_deplacement_tete:
            lecture, sens_lecture, direction_lecture, temps_lecture = deplacement_t(
                    temps_lecture, lecture, direction_lecture, nombre_de_frame, sens_lecture, temps_min_changement_t, probabilite_changement_selon_direction_t, liste_proba, indice_proba)
            indice_proba, temps_changement_proba = changement_proba(
                temps_changement_proba, temps_entre_changement_proba, indice_proba, liste_proba)


        if keys[input_map["changement_lecture"]]:
            sens_lecture=-sens_lecture
        
        lecture += sens_lecture
        if lecture <= 0:
            lecture = 0
            sens_lecture = 1
            direction_lecture = 1
        elif lecture >= nombre_de_frame - 1:
            lecture = nombre_de_frame - 1
            sens_lecture = -1
            direction_lecture = -1
        

    for i in range(10):
        if keys[input_map["zoom_" + str(i)]]:
            print(zoomPossible(zinit, listZoomManuel[i], vitesse_x, vitesse_y, vzoom, posX, posY, size_x, size_y, limite_up_x, limite_up_y))

    
    listposX.append(posX)
    listposY.append(posY)
    listtemps.append(temps_x)
    if temps_x!=temps_y:
        print(temps_x-temps_y)


    img = frame_list[lecture]
    img = img[posY - size_window_y //2 + 1 - size_y % 2 :posY + size_window_y // 2, posX - size_window_x //2 +1 -size_x%2:posX + size_window_x //2 ]

    img = cv2.resize(img, (size_x, size_y))

    compteur_de_frame += 1
    
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









    """Si on affiche les images trop vite par rapport au framerate voulu, on fait une pause"""
    temps_fin_calcul_fps_continu = time.time()

    temps_debut_calcul_fps_continu = time.time()


#plt.plot(listposX,listposY,'-v')
#plt.show()
cv2.destroyAllWindows()
pygame.quit()
print(clock.get_fps())
