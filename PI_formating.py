from fonction import signe
import os



def face_tracking_formating(fichier_input, fichier_output, nb_PI, intervalle=20):
    """ A partir d'un fichier texte résultant du tracking des visages dans une vidéos,
        crée un nouveau fichier contenant les PI sous un format utilisable
        ( Peut etre qu'il serait mieux de faire en sorte  de ne pas créer un nouveau fichier mais de 
        modifier celui  existant)"""
    
    liste_point = []

    f = open(fichier_input, 'r')
    texte = f.readlines()
    prec = -1
    iteration = 0
    for ligne in texte:
        point = []
        ligne = ligne.split(", ")
        
        ligne[0]  = ligne[0][1:]
        ligne[-1] = ligne[-1][:-2]
        
        point.append(int(ligne[0])-1) #  ID
        point.append(iteration * intervalle + 1) # lecture
        point.append(int(float(ligne[1])))  # posX
        point.append(int(float(ligne[2])))  # posY
        point.append(int(float(ligne[3]) * float(ligne[4])))    # size

        if iteration == 0:
            if point[0] != prec + 1:
                liste_ID_PI = selection_PI(liste_point, nb_PI)
                liste_point.sort(key=lambda point:point[0])
                liste_PI = [ [liste_point[i][1:-1]] for i in liste_ID_PI ]

                iteration += 1
            else:
                liste_point.append(point)
                
        elif iteration > 0:
            if point[0] in liste_ID_PI:
                for i in range(len(liste_ID_PI)):
                    if liste_ID_PI[i] == point[0]:
                        liste_PI[i].append(point[1:-1])
            if point[0] != prec + 1:
                iteration += 1

        prec = point[0]

    return liste_PI


def selection_PI(liste_PI, nb_PI):
    """Permet de faire une sélection de PI a partir d'une liste de points
    en fontion de la taille"""

    liste_PI.sort(key=lambda PI:PI[4])
    liste_ID_PI =[]
    for i in range(nb_PI):
        liste_ID_PI.append(liste_PI[-nb_PI+i][0])
    liste_ID_PI.sort()
    return liste_ID_PI


def remplissage_PI(PI):
    """Complete un Point d'interet, c'est a dire une liste de (posX, posY, lecture), dont il
    manque certains points (lecture)"""
    
    lecture = PI[0][0]
    indice = 0
    while lecture != PI[-1][0]:

        nb_ajout = PI[indice+1][0] - PI[indice][0] - 1

        diff_x = PI[indice+1][1] - PI[indice][1]
        diff_y = PI[indice+1][2] - PI[indice][2]

        avancement_x = signe(diff_x) * (abs(diff_x) // nb_ajout)
        avancement_y = signe(diff_y) * (abs(diff_y) // nb_ajout)

        for i in range(nb_ajout):
            PI.append([lecture+i+1, PI[indice][1] + (i+1)*avancement_x, PI[indice][2] + (i+1)*avancement_y])
        PI.sort(key=lambda point:point[0])
        indice += nb_ajout + 1
        lecture = PI[indice][0]

    
    return PI


print(remplissage_PI([[1,0,0],[21,20,20],[41,0,0]]))

print(remplissage_PI(face_tracking_formating("PI.txt", "u", 5)[0]))
