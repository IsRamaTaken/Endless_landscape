from tkinter import Tk, Label,StringVar,Entry,Button
from functools import partial


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




#style


formulaire=Tk()
formulaire.title('Endless landscape')
Titre=Label(formulaire,text='Configuration de la vidéo',bd=10)
Titre.grid(row=0,column=0,columnspan=2)

FPS=FormulaireRemplir("Nombre d'images par seconde",1,formulaire,30)
CadreX=FormulaireRemplir("Largeur du cadre en pixels",2,formulaire,600)
CadreY=FormulaireRemplir("Hauteur du cadre en pixels",3,formulaire,900)
VitesseCadreX=FormulaireRemplir("Vitesse de déplacement selon x en pixels par seconde",4,formulaire,30)
VitesseCadreY=FormulaireRemplir("Vitesse de déplacement selon y en pixels par seconde",5,formulaire,30)

FPS.positionner()
CadreX.positionner()
CadreY.positionner()
VitesseCadreX.positionner()
VitesseCadreY.positionner()



formulaire.mainloop()
