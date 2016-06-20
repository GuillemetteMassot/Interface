from tkinter import *
from tkinter.filedialog import *
from PIL.Image import *
import sys

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#Initialisation des variables globales
x=0
y=0
rouge=0
vert=0
bleu=0

#Création d'une fenetre 
fenetre = Tk()
fenetre.title('Braille pour grimpeur')

#Ouverture de l'image
filepath = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
photo = PhotoImage(file=filepath)
canvas = Canvas(fenetre, width=photo.width(), height=photo.height(), bg="yellow")
canvas.create_image(0, 0, anchor=NW, image=photo)
 
def pointeur(event):
   global x
   global y
   chaine.configure(text="Clic détecté en X = "+str(event.x)+", Y = "+str(event.y))
   x,y=event.x,event.y

def appuie(x,y,filepath):
   " sauvegarde l'image traitée une fois que le bouton 'Ok' est appuyé"
   global rouge
   global vert
   global bleu
   im=open(filepath)
   (rouge,vert,bleu) = im.getpixel((x,y)) #Donne les couleurs correspondants au pixel de coordonnées (x,y) (coordonnées séléctionnées par l'utilisateur)
   p = fromarray(selection_voie(rouge,vert,bleu,60,filepath)) #Crée une image de la matrice retournée par la fonction 'selection_voie'
   p.save('image_traitee.png')
   sys.exit()


def selection_voie(R,V,B,intervalle,filepath):
    
    im=open(filepath)
    img=np.array(im)       #Matrice de l'image sélectionnée
    s1,s2 = img.shape[:2]  #Dimensions de la matrice de l'image  

    #Définition des intervalles de couleur du pixel séléctionné 
    seuilR1=R-intervalle
    seuilR2=R+intervalle
    seuilV1=V-intervalle
    seuilV2=V+intervalle
    seuilB1=B-intervalle
    seuilB2=B+intervalle

    
    for i in range(0,s1): #Parcourt les lignes de la matrice
        for j in range(0,s2): #Parcourt les colonnes de la matrice
            if img[i,j][0] in range(seuilR1,seuilR2): #Si la valeur de la couleur rouge du pixel est comprise dans l'intervalle
                if img[i,j][1] in range(seuilV1,seuilV2): #Si la valeur de la couleur verte du pixel est comprise dans l'intervalle
                    if img[i,j][2] in range(seuilB1,seuilB2): #Si la valeur de la couleur bleue du pixel est comprise dans l'intervalle
                       pass  #On garde la couleur des pixels
                    else :
                       #On met remplace le pixel par un pixel noir
                        img[i,j][0]=0
                        img[i,j][1]=0
                        img[i,j][2]=0
                else :
                  #On met remplace le pixel par un pixel noir
                    img[i,j][0]=0
                    img[i,j][1]=0
                    img[i,j][2]=0
            else :
                #On met remplace le pixel par un pixel noir
                img[i,j][0]=0
                img[i,j][1]=0
                img[i,j][2]=0

    for i in range(0,3):
       for j in range(0,s2):
          img[i,j][0]=R
          img[i,j][1]=V
          img[i,j][2]=B
          
    return img

   
canvas.focus_set()
canvas.bind("<Button-1>", pointeur) #ecrit les coordonnées x et y lorsqu'on clique sur l'image
canvas.pack()
chaine=Label(fenetre)

#Affichage du bouton
B=Button(fenetre, text ='ok', command = lambda : appuie(x,y,filepath))
B.pack(side=LEFT, padx=5, pady=5)

#Execution de la fenetre générale
chaine.pack()
fenetre.mainloop()



