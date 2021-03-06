

def deplacement_manuel(arret_x,arret_y, posX, sens_deplacement_x, limite_up_x, size_window_x, vitesse_x,posY, sens_deplacement_y, limite_up_y, size_window_y, vitesse_y, keys, input_map):


    if keys[input_map["move_right"]]:
        sens_deplacement_x = 1
        arret_x=False
    elif keys[input_map["move_left"]]:
        sens_deplacement_x = -1
        arret_x=False
    if keys[input_map["move_up"]]:
        sens_deplacement_y = -1
        arret_y=False
    elif keys[input_map["move_down"]]:
        sens_deplacement_y = 1
        arret_y=False



    posX+=sens_deplacement_x * vitesse_x
    posY+=sens_deplacement_y * vitesse_y

    
    bord_atteint_x = posX == size_window_x // 2 + size_window_x % 2 - 1 or posX == limite_up_x - size_window_x // 2
    bord_atteint_y = posY == size_window_y // 2 + size_window_y % 2 - 1 or posY == limite_up_y - size_window_y // 2
    if posX <= size_window_x // 2 + size_window_x % 2 - 1:
        posX = size_window_x // 2 + size_window_x % 2 - 1
    elif posX >= limite_up_x - size_window_x // 2:
        posX = limite_up_x - size_window_x // 2
    if posY <= size_window_y // 2 + size_window_y % 2 - 1:
        posY = size_window_y // 2 + size_window_y % 2 - 1
    elif posY >= limite_up_y - size_window_y // 2:
        posY = limite_up_y - size_window_y // 2

    return arret_x,arret_y, posX, sens_deplacement_x, bord_atteint_x, posY, sens_deplacement_y, bord_atteint_y



def chgmt_indice_vitesse_manuel(indice_vitesse_x, indice_vitesse_y, vitesse_x, vitesse_y,chgmt_vitesse_x_en_cours, chgmt_vitesse_y_en_cours, keys, input_map, vitesse_initiale_x, vitesse_initiale_y):
    if not chgmt_vitesse_x_en_cours:
        if keys[input_map["vitesse_x_+"]]:
            if indice_vitesse_x != len(vitesse_x) -1:
                vitesse_initiale_x = vitesse_x[indice_vitesse_x]
                indice_vitesse_x += 1
                chgmt_vitesse_x_en_cours = True
        elif keys[input_map["vitesse_x_-"]]:
            if indice_vitesse_x != 0:
                vitesse_initiale_x = vitesse_x[indice_vitesse_x]
                indice_vitesse_x -= 1
                chgmt_vitesse_x_en_cours = True
    
    if not chgmt_vitesse_y_en_cours:
        if keys[input_map["vitesse_y_+"]]:
            if indice_vitesse_y != len(vitesse_y) -1:
                vitesse_initiale_y = vitesse_y[indice_vitesse_y]
                indice_vitesse_y += 1
                chgmt_vitesse_y_en_cours = True
        elif keys[input_map["vitesse_y_-"]]:
            if indice_vitesse_y != 0:
                vitesse_initiale_y = vitesse_y[indice_vitesse_y]
                indice_vitesse_y -= 1
                chgmt_vitesse_y_en_cours = True
    return indice_vitesse_x, indice_vitesse_y, vitesse_initiale_x, vitesse_initiale_y, chgmt_vitesse_x_en_cours, chgmt_vitesse_y_en_cours














































