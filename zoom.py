import time
from numpy.random import uniform

def tirage(probabilite):  # marche aléatoire
    return uniform() <= probabilite


def signe(z):
    if z>=0:
        return(1)
    else:
        return(-1)

def changeDirectionSensCentre(sens_deplacement_x, direction_deplacement_x,sens_deplacement_y,direction_deplacement_y,limit_up_x,limit_up_y,posX,posY):#permet de changer la direction pour que le cadre va vers le centre
    direction_deplacement_x = signe(limit_up_x / 2 - posX)
    sens_deplacement_x = direction_deplacement_x
    direction_deplacement_y = signe(limit_up_y / 2 - posY)
    sens_deplacement_y = direction_deplacement_y
    return sens_deplacement_x, direction_deplacement_x,sens_deplacement_y,direction_deplacement_y

def zoomPossible(zinit,zf,vx,vy,vzoom,posX,posY,size_x,size_y,limit_up_x,limit_up_y):

    if zf>=zinit:
        return True   #ICI on zoom donc pas de problème puisqu'on réduit la taille de la fenêtre

    else:
        nbFrame=abs(zf-zinit)/vzoom  #on calcule le nb de frame pour passer d'un zoom
        newSizeX = int(size_x / zf)   #taille de la fenêtre sur l'image d'origine
        newSizeY = int(size_y / zf)
        deltaX=nbFrame*vx
        deltaY=nbFrame*vy

        return int(posX-(newSizeX/2)-deltaX)>=0 and int(posX+(newSizeX/2)+deltaX)<=limit_up_x and int(posY-(newSizeY/2)-deltaY)>=0 and int(posY+(newSizeY/2)+deltaY)<=limit_up_y

def zoom_automatique(probaZoom,probaDezoom,sens_deplacement_x, direction_deplacement_x,sens_deplacement_y,direction_deplacement_y,Zt,vx, vy, vzoom, posX, posY, size_x, size_y, limit_up_x, limit_up_y,temps_debut_zoom,listZoom,directionZoom,zinit,zf,indice_zoom,zoom_en_cours_auto,temps_changement_zoom,attente_min,attente_max, compteur_de_frame):
    duree_changement = compteur_de_frame - temps_changement_zoom
    if zoom_en_cours_auto :
        Zt+=signe(zf-zinit)*vzoom
        if (Zt>=zf and signe(zf-zinit)==1) or (Zt<=zf and signe(zf-zinit)==-1):
            Zt=zf
            zinit=zf
            zoom_en_cours_auto=False
            temps_changement_zoom=compteur_de_frame

    else:
        attente=uniform(attente_min,attente_max)
        if duree_changement>attente:

            if indice_zoom==9: directionZoom=-1

            elif indice_zoom==0: directionZoom=1

            Zpred=zoomPossible(zinit, listZoom[max(0,indice_zoom-1)], vx, vy, vzoom, posX, posY, size_x, size_y, limit_up_x, limit_up_y)
            Zsuivant=zoomPossible(zinit, listZoom[min(9,indice_zoom+1)], vx, vy, vzoom, posX, posY, size_x, size_y, limit_up_x, limit_up_y)

            if directionZoom==1 :
                if tirage(1-probaZoom): #probaZoom c'est la probabilité de zoomer quand on privilégie le zoom
                    if Zpred and indice_zoom>0 :
                        indice_zoom-=1
                    else:
                        sens_deplacement_x, direction_deplacement_x, sens_deplacement_y, direction_deplacement_y = \
                            changeDirectionSensCentre(sens_deplacement_x, direction_deplacement_x, sens_deplacement_y, \
                                                      direction_deplacement_y, limit_up_x, limit_up_y, posX, posY)       # on veut zoomer mais ce n'est pas possible donc on se deplace vers le centre
                        indice_zoom=+1

                elif Zsuivant:
                        indice_zoom+=1

            elif directionZoom==-1:

                if tirage(probaDezoom):   #probaDezoom c'est la probabilité de dézoomer quand on privilégie le dézoom
                    if Zpred  :
                        indice_zoom-=1
                    else:
                        sens_deplacement_x, direction_deplacement_x, sens_deplacement_y, direction_deplacement_y = \
                            changeDirectionSensCentre(sens_deplacement_x, direction_deplacement_x, sens_deplacement_y, \
                                                      direction_deplacement_y, limit_up_x, limit_up_y, posX, posY)       # on veut zoomer mais ce n'est pas possible donc on se deplace vers le centre
                        indice_zoom=+1

                elif Zsuivant and indice_zoom<9:
                        indice_zoom+=1


            zf=listZoom[indice_zoom]
            zoom_en_cours_auto=True

            temps_debut_zoom=compteur_de_frame
    return probaZoom,probaDezoom,sens_deplacement_x, direction_deplacement_x,sens_deplacement_y,direction_deplacement_y,temps_debut_zoom,directionZoom,zinit,zf,indice_zoom,zoom_en_cours_auto,temps_changement_zoom,Zt


def Zoom_Manuel( Zt,vx, vy, vzoom, posX, posY, size_x, size_y, limit_up_x, limit_up_y,temps_debut_zoom,listZoomManuel,zinit,zf,zoom_en_cours_manuel,indice_zoom, indiceZoomDefault , keys, input_map,compteur_de_frame):

    if zoom_en_cours_manuel :

        Zt+=signe(zf-zinit)*vzoom
        if (Zt>=zf and signe(zf-zinit)==1) or (Zt<=zf and signe(zf-zinit)==-1):
            Zt=zf
            zinit=zf
            zoom_en_cours_manuel=False

    else:
        for i in range(10):
            if keys[input_map["zoom_" + str(i)]] and zoomPossible(zinit, listZoomManuel[i], vx, vy, vzoom, posX, posY, size_x, size_y, limit_up_x, limit_up_y):

                zoom_en_cours_manuel = True
                if i == 0:

                    indice_zoom = indiceZoomDefault
                else:
                    indice_zoom=i

                zf = listZoomManuel[i]
                temps_debut_zoom = compteur_de_frame


    return Zt,indice_zoom,temps_debut_zoom,zinit,zf,zoom_en_cours_manuel



