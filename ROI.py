

def signe(z):
    if z>=0:
        return(1)
    else:
        return(-1)

def deplacementvers(posinit,posfinal):  # donne la direction à prendre pour aller vers la position finale
    return signe(posfinal-posinit)
