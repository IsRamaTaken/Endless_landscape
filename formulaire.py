from tkinter import Tk, Label,StringVar,Entry,Button,font,Checkbutton, BooleanVar



def quit():
    global formulaire
    global Validation
    Validation.grid(row=0,column=0,rowspan=7,columnspan=2)


class FormulaireSelect:

    def __init__(self,texte,position,fenetre,action,selectDefault):
        self.position=position
        self.texte=texte
        self.fenetre=fenetre
        self.action=action
        self.selectDefault = selectDefault
        is_checked=BooleanVar(self.fenetre,str(selectDefault))
        self.descip=Label(self.fenetre,text=self.texte)
        self.select=Checkbutton(self.fenetre,variable=is_checked,command=self.action)


    def postionner(self):
        self.select.grid(row=self.position,column=2)
        self.descip.grid(row=self.position,column=3)

class TitrePartie:
    def __init__(self,texte,position,fenetre):
        self.texte=texte
        self.position=position
        self.fenetre=fenetre
        self.titre=Label(self.fenetre,text=texte)

    def positionner(self):
        self.titre.grid(row=self.position,column=0)


class FormulaireRemplir:

    def __init__(self,texte,position,fenetre,variableDefault):
        self.texte=texte
        self.position=position
        self.fenetre=fenetre
        self.variableDefault=variableDefault
        self.descrip=Label(fenetre,text=self.texte,pady=5,padx=5)
        text = StringVar(self.fenetre)
        text.set(str(self.variableDefault))
        self.rempli=Entry(fenetre, textvariable=text)


    def positionner(self):
        self.descrip.grid(row=self.position,column=0)
        self.rempli.grid(row=self.position,column=1)

    def getVar(self):
        return self.rempli.get()



#style


formulaire=Tk()
formulaire.title('Endless landscape')
Titre=Label(formulaire,text='Configuration de la vidéo',bd=10)
Titre.grid(row=0,column=0,columnspan=2)

VideoTitre=TitrePartie("Paramètres Vidéo",1,formulaire)
Video=FormulaireRemplir("Video",2,formulaire,'Manif.mp4')
FPS=FormulaireRemplir("Nombre d'images par seconde",2,formulaire,30)
CadreX=FormulaireRemplir("Largeur du cadre en pixels",3,formulaire,600)
CadreY=FormulaireRemplir("Hauteur du cadre en pixels",4,formulaire,900)
VitesseCadreX=FormulaireRemplir("Vitesse de déplacement selon x en pixels par seconde",5,formulaire,30)
VitesseCadreY=FormulaireRemplir("Vitesse de déplacement selon y en pixels par seconde",6,formulaire,30)

VideoTitre.positionner()
Video.positionner()
FPS.positionner()
CadreX.positionner()
CadreY.positionner()
VitesseCadreX.positionner()
VitesseCadreY.positionner()


AffichageProb=Label(formulaire,textvariable='')
AffichageProb.grid(row=7,column=0,columnspan=2)
Enter= Button(formulaire,text='Enter',command=quit)
Enter.grid(row=8,column=0,columnspan=2)
Validation=Label(formulaire,text='Merci')

formulaire.mainloop()
