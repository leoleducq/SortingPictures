#!/usr/bin/env python3.9
import os, shutil

#Liste de toutes les photos
contenu = os.listdir("Alpha/photos")
#Permet de séparer chaque photos de la liste
contenu=[x.split('/')[-1] for x in contenu if '.jpg' in x.split('/')[-1]]
#Tri par ordre alphanumérique
contenu.sort()

for pic in contenu:
    #Remplace les caractères gênants
    lenpic = pic.replace(".jpg","")
    picname = pic.replace("-","").replace(".","")
    #Prend le 1er caractère de la photo
    directory1 = picname[0]
    #Prend le 2ème caractère de la photo
    directory2 = picname[1]
    try:
        #Si la longueur du nom de la photo est supérieur à 1 (supérieur ou égal à 2)
        if len(lenpic) > 1:
        #Créer un dossier avec le 1er caractère puis un dossier avec le 2ème caractère
            os.makedirs('Alpha/sortphotos/'+directory1+'/'+directory2+'/', exist_ok=True)
            #Prend la photo et la met dans ce dossier
            filePath = shutil.copyfile('Alpha/photos/'+pic, 'Alpha/sortphotos/'+directory1+'/'+directory2+'/'+pic)
        #Si la longueur est égal à 1, crée un dossier uniquement avec le 1er caractère
        else:
            #Créer un dossier avec le 1er caractère
            os.makedirs('Alpha/sortphotos/'+directory1, exist_ok=True)
            #Prend la photo et la met dans ce dossier
            filePath = shutil.copyfile('Alpha/photos/'+pic, 'Alpha/sortphotos/'+directory1+'/'+pic)
    except OSError:
        #Vérifie si le chemin existe et qu'il s'agit d'un dossier, s'il existe -> exception non envoyée
        if not os.path.isdir('Alpha/sortphotos/'+directory2):
            raise
        if not os.path.isdir('Alpha/sortphotos/'+directory1+'/'+directory2):
            raise