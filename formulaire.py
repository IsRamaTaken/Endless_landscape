from tkinter import *
import tkinter
from PIL import Image,ImageTk
from initialisation_parametres import *
import numpy as np


pygame.quit()

listeFrame2=[] # liste des frame au format image

#on transforme les numpy array en image


def quit():
    global formulaire
    global Validation
    Validation.grid(row=0,column=0,rowspan=7,columnspan=2)
    


def ajout_position(listPos,frame,image):
    for i in range (len(listPos)):
        if listPos[i][0]==frame:
            image[listPos[i][2]-1:listPos[i][2]+2,listPos[i][1]-1:listPos[i][1]+2]=np.array([[[0,0,255],[0,0,255],[0,0,255]],[[0,0,255],[0,0,255],[0,0,255]],[[0,0,255],[0,0,255],[0,0,255]]])
    return image

def supprimerDernierPoint(*args):
    print('salut')
    A=ListeInteret[ptinteret.get()]
    for i in range(len(A)):
        if A[len(A)-1-i][0]==Frame.get():
            ListeInteret.pop(i)
            a = cv2.resize(frame_list[i], (limite_up_x // 2, limite_up_y // 2))
            a = ajout_position(ListeInteret[ptinteret.get()], i, a)
            a = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
            b = Image.fromarray(a)
            b = ImageTk.PhotoImage(b)
            listeFrame2[i] = b
            del a
            del b
            diapo.itemconfig(imagediapo, image=listeFrame2[Frame.get() - 1])
            print('salut')
            return

def ajoutElementList(*args):
    OptionList[-1]="Point d'intérêt "+str(len(OptionList))
    ListeInteret[OptionList[-1]]=[]
    OptionList.append('+')
    ptinteret.set(OptionList[-2])
    global opt
    opt.destroy()
    opt = OptionMenu(app, ptinteret, *OptionList)
    opt.config(font=('Helvetica', 12))
    opt.grid(row=0,column=11)

def changementPtinteret(*args):
    if ptinteret.get()=='+':
        ajoutElementList(*args)
    for i in range(len(frame_list)):
        a = cv2.resize(frame_list[i], (limite_up_x // 2, limite_up_y // 2))
        a = ajout_position(ListeInteret[ptinteret.get()], i, a)
        a = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
        b = Image.fromarray(a)
        b = ImageTk.PhotoImage(b)
        listeFrame2[i]=b
        del a
        del b
    diapo.itemconfig(imagediapo, image=listeFrame2[Frame.get() - 1])






def ajoutPosition(event):
    global ListeInteret
    ListeInteret[ptinteret.get()].append((Frame.get()-1,event.x,event.y))
    A=frame_list[Frame.get()-1]
    A=cv2.resize(A,(limite_up_x//2,limite_up_y//2))
    A=ajout_position(ListeInteret[ptinteret.get()],Frame.get()-1,A)
    A = cv2.cvtColor(A, cv2.COLOR_BGR2RGB)
    listeFrame2[Frame.get()-1]=ImageTk.PhotoImage(Image.fromarray(A))

    diapo.itemconfig(imagediapo,image=listeFrame2[Frame.get()-1])
    del A
    Info.configure(text=ptinteret.get() +' : ajout de la position '+ str((Frame.get()-1,event.x,event.y)))



def deplacementLecture (deplacement):
    def deplace (*args):
        Info.configure(text='')
        if  Frame.get()+deplacement<=len(listeFrame2) and Frame.get()+deplacement>=1:
            Frame.set(Frame.get()+deplacement)
            diapo.itemconfigure(imagediapo,image=listeFrame2[Frame.get()-1])
    return deplace

#Initialisation des paramètres
ListeInteret={}
ListeInteret["Point d'intérêt 1"]=[]

OptionList = [
"Point d'intérêt 1",
'+'
]

app = Tk()


#Conversion des images au format PIL TK pour pouvoir les afficher dans la fenêtre

for i in range(len(frame_list)):

    a=cv2.resize(frame_list[i],(limite_up_x//2,limite_up_y//2))
    a = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    b=Image.fromarray(a)
    b=ImageTk.PhotoImage(b)
    listeFrame2.append(b)
    del a
    del b


#Création des variables
Frame=IntVar(app)
Frame.set(1)
ptinteret = StringVar(app)
ptinteret.set(OptionList[0])



#Création des affichages

#Diaporama
diapo = Canvas(app, width = limite_up_x//2, height = limite_up_y//2)
imagediapo=diapo.create_image(0,0,image=listeFrame2[Frame.get()-1],anchor=tkinter.NW)

#Menu déroulant
opt = OptionMenu(app, ptinteret, *OptionList)
opt.config(font=('Helvetica', 12))

#Player Video
avanceImage=Button(app,text='>',command=deplacementLecture(1),font=('Helvetica', 12))
avanceImageRapide=Button(app,text='>>',command=deplacementLecture(5),font=('Helvetica', 12))
reculImage=Button(app,text='<',command=deplacementLecture(-1),font=('Helvetica', 12))
reculImageRapide=Button(app,text='<<',command=deplacementLecture(-5),font=('Helvetica', 12))

#Afficheur de message
Info=Label(app)

#options
Supprimer=Button(app, text='Supprimer le point d''interet',font=('Helvetica', 12))
Fixer=Button(app, text='Fixer le point d''intérêt',font=('Helvetica', 12))
Chargement=Button(app, text='Charger les points d''intérêts',font=('Helvetica', 12))
Sauvegarder=Button(app, text='Saugarder les points d''intérêts',font=('Helvetica', 12))



#Gestion des events

ptinteret.trace("w", changementPtinteret)
diapo.bind('<Button-1>',ajoutPosition)
Supprimer.configure(command=supprimerDernierPoint)



#Placement des objets
diapo.grid(row=0,column=0,columnspan=10)
opt.grid(row=0,column=11)
avanceImage.grid(row=1,column=8,padx=60)
avanceImageRapide.grid(row=1,column=9,padx=60)
reculImage.grid(row=1,column=1,padx=60)
reculImageRapide.grid(row=1,column=0,padx=60)
#Info.grid(row=1,column=2)
Supprimer.grid(row=2,column=0)
Fixer.grid(row=2,column=1)
Chargement.grid(row=2,column=2)
Sauvegarder.grid(row=2,column=3)

app.mainloop()
del listeFrame2
