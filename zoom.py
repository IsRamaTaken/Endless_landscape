import time
from numpy.random import uniform

def tirage(probabilite):  # marche aléatoire
    return uniform() <= probabilite


def signe(z):
    if z>=0:
        return(1)
    else:
        return(-1)


def zoomPossible(zinit,zf,vx,vy,vzoom,posX,posY,size_x,size_y,limit_up_x,limit_up_y,posXfinal,posYfinal):

    if zf>=zinit:
        return True   #ICI on zoom donc pas de problème puisqu'on réduit la taille de la fenêtre
    else:
        nbFrame=int(abs(zf-zinit)/vzoom)  #on calcule le nb de frame pour passer d'un zoom
        for i in range(nbFrame):
            newSizeX = int(size_x / (zinit+signe(zf-zinit)*vzoom*i))   #taille de la fenêtre sur l'image d'origine
            newSizeY = int(size_y / (zinit+signe(zf-zinit)*vzoom*i))
            if int(posX+signe(posXfinal-posX)*i*vx - (newSizeX / 2) ) < 0 and int(posX+signe(posXfinal-posX)*i*vx - (newSizeX / 2) ) > limit_up_x and int(posY+signe(posYfinal-posY)*i*vy - (newSizeY / 2) ) < 0 and int(posY+signe(posYfinal-posY)*i*vy - (newSizeY / 2) ) > limit_up_y :
                return False
        return True

def listeZoomPossible(zinit,vx,vy,vzoom,posX,posY,size_x,size_y,limit_up_x,limit_up_y,listeZoom,posXfinal,posYfinal):
    listeZoomPossible=[]
    for i in range(len(listeZoom)):

        if zoomPossible(zinit,listeZoom[i],vx,vy,vzoom,posX,posY,size_x,size_y,limit_up_x,limit_up_y,posXfinal,posYfinal):
            listeZoomPossible.append(listeZoom[i])

    return listeZoom


def zoom_automatique(probaZoom,probaDezoom,sens_deplacement_x, direction_deplacement_x,sens_deplacement_y,direction_deplacement_y,Zt,vx, vy, vzoom, posX, posY, size_x, size_y, limit_up_x, limit_up_y,temps_debut_zoom,listZoom,directionZoom,zinit,zf,indice_zoom,zoom_en_cours_auto,temps_changement_zoom,attente_min,attente_max, compteur_de_frame):
    duree_changement = compteur_de_frame - temps_changement_zoom
    if zoom_en_cours_auto :
        Zt+=signe(zf-zinit)*vzoom
        if (Zt>=zf and signe(zf-zinit)==1) or (Zt<=zf and signe(zf-zinit)==-1):
            Zt=zf
            zinit=zf
            zoom_en_cours_auto=False
            temps_changement_zoom=compteur_de_frame

            temps_debut_zoom=compteur_de_frame
    return probaZoom,probaDezoom,sens_deplacement_x, direction_deplacement_x,sens_deplacement_y,direction_deplacement_y,temps_debut_zoom,directionZoom,zinit,zf,indice_zoom,zoom_en_cours_auto,temps_changement_zoom,Zt




