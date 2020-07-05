import configparser
import os

#On lit le fichier de configuration:
config = configparser.ConfigParser(allow_no_value=True)
config.read(os.path.join(os.path.dirname(__file__), "config.ini"))

#On vérifie que le fichier n'est pas vide
if config.sections() == []:
    print("!!!! Le fichier config.ini n'arrive pas a etre lu ou est vide !!!!")


"""On initialise différentes valeurs à partir du fichier de configuration:"""

#Pour la vidéo d'origine:
limitation_nombre_de_frame = config.getint("input_video", "limitation_nombre_de_frame")
path = config.get("input_video", "video")

#Pour le cadre:
choix_cadre = config.getboolean("cadre", "choix_cadre")
manuel_auto = 0
type_deplacement_cadre = manuel_auto
size_x = config.getint("cadre", "size_x")
size_y = config.getint("cadre", "size_y")

vitesse_x = config.get("cadre", "vitesse_deplacement_x")
vitesse_y = config.get("cadre", "vitesse_deplacement_y")

vitesse_x = vitesse_x.split()
vitesse_y = vitesse_y.split()

for i in range(len(vitesse_x)):
    vitesse_x[i] = float(vitesse_x[i])
for i in range(len(vitesse_y)):
    vitesse_y[i] = float(vitesse_y[i])

temps_min_chgmt_vitesse_x = config.getfloat("cadre", "temps_min_chgmt_vitesse_x")
temps_min_chgmt_vitesse_y = config.getfloat("cadre", "temps_min_chgmt_vitesse_y")

temps_changement_vitesse_x = config.getint("cadre", "temps_changement_vitesse_x")
temps_changement_vitesse_y = config.getint("cadre", "temps_changement_vitesse_y")

temps_min_x = config.getfloat("cadre", "temps_min_x")
temps_max_x = config.getfloat("cadre", "temps_max_x")
temps_min_y = config.getfloat("cadre", "temps_min_y")
temps_max_y = config.getfloat("cadre", "temps_max_y")
probabilite_changement_sens_x = config.getfloat("cadre", "probabilite_changement_sens_x")
probabilite_changement_selon_direction_x = config.getfloat("cadre", "probabilite_changement_selon_direction_x")
temps_min_changement_x = config.getint("cadre", "temps_min_changement_x")
probabilite_changement_sens_y = config.getfloat("cadre", "probabilite_changement_sens_y")
probabilite_changement_selon_direction_y = config.getfloat("cadre", "probabilite_changement_selon_direction_y")
temps_min_changement_y = config.getint("cadre", "temps_min_changement_y")

temps_arret_x = config.getint("cadre", "temps_arret_x")
temps_arret_y = config.getint("cadre", "temps_arret_y")

#ZOOM
choix_zoom_ou_non = config.getboolean("ZOOM", "zoom_ou_non")
type_zoom = manuel_auto
vzoom = config.getfloat("ZOOM", "vitesse de zoom")
attente_min = config.getfloat("ZOOM", "attente_min")
attente_max = config.getfloat("ZOOM", "attente_max")
zmax=config.getfloat("ZOOM", "zoom_max")
probaZoom=config.getfloat("ZOOM", "probaZoom")
probaDezoom=config.getfloat("ZOOM", "probaDezoom")

#Pour la tete de lecture:
liste_proba = config.get("tete_de_lecture", "liste_proba")
liste_proba = liste_proba.split()
for i in range(len(liste_proba)):
    liste_proba[i] = float(liste_proba[i])
temps_entre_changement_proba = config.getfloat("tete_de_lecture", "temps_entre_changement_proba")
choix_t = config.getboolean("tete_de_lecture", "choix_t")
type_deplacement_tete = manuel_auto
probabilite_changement_selon_direction_t = config.getfloat("tete_de_lecture", "probabilite_changement_selon_direction_t")
temps_min_changement_t = config.getfloat("tete_de_lecture", "temps_min_changement_t")

#Pour l'output vidéo:
enregistrement = config.getboolean("output_video", "enregistrement")
output_file = config.get("output_video", "output_file")
codec = config.get("output_video", "codec")
framerate = config.getint("output_video", "framerate")
fullscreen = config.getboolean("output_video", "fullscreen")
sens = config.getint("output_video", "sens")

#mode ROI
ROI = config.getboolean("MODE","ROI")

#Pour les inputs clavier:

key_config = configparser.ConfigParser(allow_no_value=True)
key_config.read(os.path.join(os.path.dirname(__file__), "key.ini"))
input_map = dict(key_config.items("keyboard input"))
for key in input_map:
    input_map[key] = int(input_map[key])

"""  Fin de l'importation de paramètres  """

#Si le chemin n'est pas absolu, on le complète pour qu'il le soit
if not os.path.isabs(path):
    path = os.path.join(os.path.dirname(__file__), path)

# conversion du temps seconde en image

#Pour le cadre:

for i in range(len(vitesse_x)):
    vitesse_x[i] = int( vitesse_x[i] / framerate)
    if vitesse_x[i] <= 0:
        vitesse_x[i] = 1
for i in range(len(vitesse_y)):
    vitesse_y[i] = int( vitesse_y[i] / framerate)
    if vitesse_y[i] <= 0:
        vitesse_y[i] = 1

# On s'assure que les listes soient bien dans un ordre croissant
vitesse_y.sort()
vitesse_x.sort()
temps_changement_vitesse_x = int(temps_changement_vitesse_x * framerate)
temps_changement_vitesse_y = int(temps_changement_vitesse_y * framerate)

temps_min_chgmt_vitesse_x = int( temps_min_chgmt_vitesse_x * framerate)
temps_min_chgmt_vitesse_y = int( temps_min_chgmt_vitesse_y * framerate)
temps_min_x = int(temps_min_x * framerate)
temps_max_x = int(temps_max_x * framerate)
temps_min_y = int(temps_min_y * framerate)
temps_max_y = int(temps_max_y * framerate)
temps_min_changement_x *= framerate
temps_min_changement_y *= framerate

temps_arret_x *=framerate
temps_arret_y *= framerate

#ZOOM

vzoom /=framerate
attente_min *= framerate
attente_max *= framerate

#Pour la tete de lecture:

nb_frame_min_changement_lecture = int(temps_min_changement_t * framerate)


