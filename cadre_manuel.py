import time

def deplacement_manuel(temps, posX, sens_deplacement_x, limite_up_x, size_window_x, vitesse_x,
                       posY, sens_deplacement_y, limite_up_y, size_window_y, vitesse_y, pygame, input_map):

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == input_map["move_right"]:
                sens_deplacement_x = 1
            if event.key == input_map["move_left"]:
                sens_deplacement_x = -1
            if event.key == input_map["move_up"]:
                sens_deplacement_y = -1
            if event.key == input_map["move_down"]:
                sens_deplacement_y = 1

    duree = time.time() - temps
    posX += int(sens_deplacement_x * vitesse_x * duree * 2)
    posY += int(sens_deplacement_y * vitesse_y * duree * 2)
    temps = time.time()
    bord_atteint_x = posX == size_window_x // 2 + size_window_x % 2 - 1 or posX == limite_up_x - size_window_x // 2
    bord_atteint_y = posY == size_window_y // 2 + size_window_y % 2 - 1 or posY == limite_up_y - size_window_y // 2
    if posX <= size_window_x // 2 + size_window_x % 2 - 1:
        posX = size_window_x // 2 + size_window_x % 2 - 1
    elif posX >= limite_up_x - size_window_x // 2:
        posX = limite_up_x - size_window_x // 2
    if posY <= size_window_x // 2 + size_window_x % 2 - 1:
        posY = size_window_x // 2 + size_window_x % 2 - 1
    elif posY >= limite_up_y - size_window_y // 2:
        posY = limite_up_y - size_window_y // 2
    pos_x_reel = posX
    pos_y_reel = posY

    return temps, posX, pos_x_reel, sens_deplacement_x, bord_atteint_x, posY, pos_y_reel, sens_deplacement_y, bord_atteint_y
