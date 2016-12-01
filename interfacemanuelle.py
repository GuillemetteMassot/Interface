# Copyright (c) 2016 Guillemette Massot <guillemette.massot@telecom-bretagne.eu>
#                    Elisa Blanchard <elisa.blanchard@telecom-bretagne.eu>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


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
#Ouverture de l'image de départ
filepath = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
photo = PhotoImage(file=filepath)
canvas = Canvas(fenetre, width=photo.width(), height=photo.height(), bg="white")
canvas.create_image(0, 0, anchor=NW, image=photo)

#Ouverture de l'image traitée
filepath2 = askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('all files','.*')])
photo2 = PhotoImage(file=filepath2)
canvas2 = Canvas(fenetre, width=photo2.width(), height=photo2.height(), bg="white")
canvas2.create_image(0, 0, anchor=NW, image = photo2)



def pointeur(event):
   global x
   global y
   chaine.configure(text="Clic détecté en X = "+str(event.x)+", Y = "+str(event.y))
   x,y=event.x,event.y


def select_manuelle(x,y,filepath,R,V,B):
	im=open(filepath)
	img=np.array(im)
	s1,s2 = img.shape[:2]
	n=int(s1/28)
	if y-n>0 and y+n<s2:
	       if x-n <0:
                        for i in range(x,x+n):
                              for j in range(y-n,y+n):
                                       img[i,j][0]=R
                                       img[i,j][1]=V
                                       img[i,j][2]=B
	       if x+n >s1:
                        for i in range(x-n,x):
                              for j in range(y-n,y+n):
                                       img[i,j][0]=R
                                       img[i,j][1]=V
                                       img[i,j][2]=B
	       if x+n >0:
                        for i in range(x-n,x+n):
                              for j in range(y-n,y+n):
                                       img[i,j][0]=R
                                       img[i,j][1]=V
                                       img[i,j][2]=B
	       if x+n <s1:
                        for i in range(x-n,x+n):
                              for j in range(y-n,y+n):
                                       img[i,j][0]=R
                                       img[i,j][1]=V
                                       img[i,j][2]=B
	if x-n>0 and x+n<s1:
               if y-n <0:
                        for i in range(x-n,x+n):
                              for j in range(y,y+n):
                                       img[i,j][0]=R
                                       img[i,j][1]=V
                                       img[i,j][2]=B
               if y+n >s2:
                        for i in range(x-n,x+n):
                              for j in range(y-n,y):
                                       img[i,j][0]=R
                                       img[i,j][1]=V
                                       img[i,j][2]=B
        
	if x-n < 0:
	       if y-n <0:
                        for i in range(x,x+n):
                              for j in range(y,y+n):
                                       img[i,j][0]=R
                                       img[i,j][1]=V
                                       img[i,j][2]=B
                                       
	       if y-n >0:
                        for i in range(x,x+n):
                              for j in range(y-n,y+n):
                                       img[i,j][0]=R
                                       img[i,j][1]=V
                                       img[i,j][2]=B
	       if y+n >s2:
                        for i in range(x,x+n):
                              for j in range(y-n,y):
                                       img[i,j][0]=R
                                       img[i,j][1]=V
                                       img[i,j][2]=B
	       if y+n <s2:
                        for i in range(x,x+n):
                              for j in range(y-n,y+n):
                                       img[i,j][0]=R
                                       img[i,j][1]=V
                                       img[i,j][2]=B
	if x+n > s1:
               if y-n <0:
                        for i in range(x-n,x):
                              for j in range(y,y+n):
                                       img[i,j][0]=R
                                       img[i,j][1]=V
                                       img[i,j][2]=B
               if y-n >0:
                        for i in range(x-n,x):
                              for j in range(y-n,y+n):
                                       img[i,j][0]=R
                                       img[i,j][1]=V
                                       img[i,j][2]=B
               if y+n >s2:
                        for i in range(x-n,x):
                              for j in range(y-n,y):
                                       img[i,j][0]=R
                                       img[i,j][1]=V
                                       img[i,j][2]=B
               if y+n <s2:
                        for i in range(x-n,x):
                              for j in range(y-n,y+n):
                                       img[i,j][0]=R
                                       img[i,j][1]=V
                                       img[i,j][2]=B
	
	
	return img


def appuiemanuelle_ajouter(x,y,filepath,filepath2):
   global rouge
   global vert
   global bleu
   im=open(filepath)
   (rouge,vert,bleu) = im.getpixel((x,y))  #Donne les couleurs correspondants au pixel de coordonnées (x,y) (coordonnées séléctionnées par l'utilisateur) 
   p = fromarray(select_manuelle(y,x,filepath2,rouge,vert,bleu)) #Crée une image de la matrice retournée par la fonction 'select_manuelle'
   p.save('image_traitee_modifiee.png')
   sys.exit()


def appuiemanuelle_supprimer(x,y,filepath,filepath2):
   global rouge
   global vert
   global bleu
   im=open(filepath)
   (rouge,vert,bleu) = im.getpixel((x,y))  #Donne les couleurs correspondants au pixel de coordonnées (x,y) (coordonnées séléctionnées par l'utilisateur) 
   p = fromarray(select_manuelle(y,x,filepath2,0,0,0)) #Crée une image de la matrice retournée par la fonction 'select_manuelle'
   p.save('image_traitee_modifiee.png')
   sys.exit()



canvas.focus_set()
canvas.bind("<Button-1>", pointeur) #ecrit les coordonnées x et y lorsqu'on clique sur l'image
canvas.pack()
canvas2.pack()
chaine=Label(fenetre)

#Affichage du bouton
B=Button(fenetre, text ='ajouter une prise', command = lambda : appuiemanuelle_ajouter(x,y,filepath,filepath2))
B.pack(side=LEFT, padx=5, pady=5)

Butt=Button(fenetre, text ='supprimer une prise', command = lambda : appuiemanuelle_supprimer(x,y,filepath,filepath2))
Butt.pack(side=LEFT, padx=5, pady=5)

#Execution de la fenetre générale
chaine.pack()
fenetre.mainloop()

