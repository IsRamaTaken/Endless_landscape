import pyautogui
import platform
import subprocess

pyautogui.FAILSAFE = False


def get_res_linux():
    texte = subprocess.run(['xrandr'], capture_output=True, text=True)
    texte = texte.stdout
    i = 0
    while texte[i : i + 8] != 'current ':
        i+=1
    debut = i + 8
    l = texte[debut:debut+15].split('x')
    return int(l[0][:-1]), int(l[1][1:].split(',')[0])


def get_res_windows():
    return (0, 0)


def deplacement_souris():
    sys = platform.system()

    if sys == 'Linux':
        res = get_res_linux()
        pyautogui.moveTo(res)

    if sys == 'Windows':
        res = get_res_windows()
        pyautogui.moveTo(res)
    print(res)

