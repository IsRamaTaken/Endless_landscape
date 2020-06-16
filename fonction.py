from numpy.random import uniform


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
