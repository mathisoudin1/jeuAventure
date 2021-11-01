"""
Programme réalisé par Oudin, Mathis, 1G4
"""
import random
import pygame
from pygame.constants import RESIZABLE

codePieceSecrete = random.randrange(1000, 9999)

pygame.init()
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 20)

# La variable informationDesPieces liste toutes les pieces possibles dans le programme (13 pièces différentes). 
# Pour chaque pièce il y a un dictionnaire décrivant le nom de la pièce et les directions possibles ou le personnage peut aller.
informationDesPieces=[""] * 13
informationDesPieces[0] = {
    "description": "l'entrée",
    "directions" : { 'n': 1, 's': 8, 'e': 7, 'o': 10 },
    "image" : pygame.image.load("entree.jpg")
}
informationDesPieces[1] = {
    "description": "le salon",
    "directions" : { 's': 0, 'e': 2},
    "image" : pygame.image.load("salon.jpg")
}
informationDesPieces[2] = {
    "description": "la salle à manger",
    "directions" : { 'n': 3, 's': 7, 'o': 1 },
    "image" : pygame.image.load("salle_a_manger.jpg")
}
informationDesPieces[3] = {
    "description": "le pallier de l'étage",
    "directions" : { 'n': 4, 's': 2, 'e': 6, 'o': 5 },
    "image" : pygame.image.load("pallier.jpg")
}
informationDesPieces[4] = {
    "description": "le grenier",
    "directions" : { 's': 3 },
    "image" : pygame.image.load("grenier.jpg")
}
informationDesPieces[5] = {
    "description": "la chambre des parents",
    "directions" : { 'e': 3 },
    "image" : pygame.image.load("chambre1.jpg")
}
informationDesPieces[6] = {
    "description": "la chambre des enfants",
    "directions" : { 'o': 3 },
    "image" : pygame.image.load("chambre2.jpg")
}
informationDesPieces[7] = {
    "description": "la cuisine",
    "directions" : { 'n': 2, 'o': 0 },
    "image" : pygame.image.load("cuisine.jpg")
}
informationDesPieces[8] = {
    "description": "le jardin",
    "directions" : { 'n': 0, 'o': 9 },
    "image" : pygame.image.load("jardin.jpg")
}
informationDesPieces[9] = {
    "description": "l'allée",
    "directions" : { 'n': 10, 'e': 8 },
    "image" : pygame.image.load("allee.jpg")
}
informationDesPieces[10] = {
    "description": "le garage",
    "directions" : { 'n': 11, 's': 9, 'e': 0 },
    "image" : pygame.image.load("garage.jpg")
}
informationDesPieces[11] = {
    "description": "la cave",
    "directions" : { 's': 10, 'o': 12 },
    "image" : pygame.image.load("cave.jpg")
}
informationDesPieces[12] = {
    "description": "la pièce secrète",
    "directions" : { 'e': 11 },
    "image" : pygame.image.load("piece_secrete.jpg")
}

# Affiche la pièce dans laquelle le personnage se trouve.
def mettreAJourAffichage(piece):
    
    fenetre.blit(informationDesPieces[piece].get('image'), (0,0))
    
    texte = font.render("Vous vous trouvé dans " + informationDesPieces[piece].get('description'), True, (0, 0, 0))
    fenetre.blit(texte,(30,450))

    directionsPossible = informationDesPieces[piece]['directions']

    messageCle = font.render(message, True, (0, 180, 180))
    fenetre.blit(messageCle,(30 , 30))
        
    if 'n' in directionsPossible:
        texteDirection = font.render('N', True, (0, 255, 0))
        fenetre.blit(texteDirection, (580, 400))
    else:
        texteDirection = font.render('N', True, (255, 0, 0))
        fenetre.blit(texteDirection, (580, 400))
    if 's' in directionsPossible:
        texteDirection = font.render('S', True, (0, 255, 0))
        fenetre.blit(texteDirection, (580, 450))
    else:
        texteDirection = font.render('S', True, (255, 0, 0))
        fenetre.blit(texteDirection, (580, 450))
    if 'e' in directionsPossible:
        texteDirection = font.render('E', True, (0, 255, 0))
        fenetre.blit(texteDirection, (600, 425))
    else:
        texteDirection = font.render('E', True, (255, 0, 0))
        fenetre.blit(texteDirection, (600, 425))
    if 'o' in directionsPossible:
        texteDirection = font.render('O', True, (0, 255, 0))
        fenetre.blit(texteDirection, (560, 425))
    else:
        texteDirection = font.render('O', True, (255, 0, 0))
        fenetre.blit(texteDirection, (560, 425))

# Retourne la pièce dans laquelle se trouve le personnage après le déplacement.
def deplacerPersonnage(piece, deplacement):
    directionsPossible = informationDesPieces[piece]['directions']

    message = ""

    if deplacement in directionsPossible:
        nouvellePiece = directionsPossible.get(deplacement)
        
        if nouvellePiece == 4 and cleTrouvée1 == False:
            message = 'Le grenier est verrouillé, il vous faut la clé.'
            return (piece, message)
        
        if nouvellePiece == 5:
            message = "Vous venez de trouver une vielle clé."
        
        if nouvellePiece == 4:
            message = "Vous avez trouvé une clé en or !"

        if nouvellePiece == 12 and cleTrouvée2 == False:
            message = "Une clé est nécessaire pour y accéder !"
            return (piece, message)

        if nouvellePiece == 12:
            message = "Vous avez fini le jeu ! "

        return (nouvellePiece, message)
    return (piece, message)
    
# Programme principal
cleTrouvée1 = False
cleTrouvée2 = False
pieceDuPersonnage = 0 # Contient la pièce dans laquelle se trouve le personnage.
message = ""

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
            else:
                (pieceDuPersonnage, message) = deplacerPersonnage(pieceDuPersonnage, event.unicode)
                if pieceDuPersonnage == 5 and cleTrouvée1 == False:
                    cleTrouvée1 = True
                if pieceDuPersonnage == 4 and cleTrouvée2 == False:
                    cleTrouvée2 = True
    mettreAJourAffichage(pieceDuPersonnage)
    pygame.display.flip()
pygame.quit()
