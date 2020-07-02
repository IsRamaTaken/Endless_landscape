from tkinter import *
import tkinter
from PIL import Image,ImageTk
from initialisation_parametres import *


pygame.quit()

listeFrame2=[] # liste des frame au format image

#on transforme les numpy array en image


def quit():
    global formulaire
    global Validation
    Validation.grid(row=0,column=0,rowspan=7,columnspan=2)



def ajoutElementList(*args):
    global ListeInteret
    if ptinteret.get()=='+':

        OptionList[-1]="Point d'intérêt "+str(len(OptionList))
        ListeInteret[OptionList[-1]]=[]
        OptionList.append('+')
        ptinteret.set(OptionList[-2])
        global opt
        opt.destroy()
        opt = OptionMenu(app, ptinteret, *OptionList)
        opt.config(font=('Helvetica', 12))
        opt.grid(row=0,column=7)


def ajoutPosition(event):
    global ListeInteret
    ListeInteret[ptinteret.get()].append((Frame.get()-1,event.x,event.y))

    Info.configure(text=ptinteret.get() +' : ajout de la position '+ str((Frame.get()-1,event.x,event.y)))



def deplacementLecture (deplacement):
    def deplace (*args):
        Info.configure(text='')
        if  Frame.get()+deplacement<=len(listeFrame2) and Frame.get()+deplacement>=1:
            Frame.set(Frame.get()+deplacement)
            diapo.create_image(0,0,image=listeFrame2[Frame.get()-1],anchor=tkinter.NW)
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


#Création des variables
Frame=IntVar(app)
Frame.set(1)
ptinteret = StringVar(app)
ptinteret.set(OptionList[0])



#Création des affichages

#Diaporama
diapo = Canvas(app, width = limite_up_x//2, height = limite_up_y//2)
diapo.create_image(0,0,image=listeFrame2[Frame.get()-1],anchor=tkinter.NW)

#Menu déroulant
opt = OptionMenu(app, ptinteret, *OptionList)
opt.config(font=('Helvetica', 12))

#Player Video
avanceImage=Button(app,text='>',command=deplacementLecture(1))
avanceImageRapide=Button(app,text='>>',command=deplacementLecture(5))
reculImage=Button(app,text='<',command=deplacementLecture(-1))
reculImageRapide=Button(app,text='<<',command=deplacementLecture(-5))

#Afficheur de message
Info=Label(app)


#Gestion des events

ptinteret.trace("w", ajoutElementList)
diapo.bind('<Button-1>',ajoutPosition)



#Placement des objets
diapo.grid(row=0,column=0,columnspan=6)
opt.grid(row=0,column=7)
avanceImage.grid(row=1,column=4,padx=60)
avanceImageRapide.grid(row=1,column=5,padx=60)
reculImage.grid(row=1,column=2,padx=60)
reculImageRapide.grid(row=1,column=1,padx=60)
Info.grid(row=1,column=3)

app.mainloop()
print(ListeInteret)
