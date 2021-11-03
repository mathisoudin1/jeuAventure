"""
Programme réalisé par Oudin, Mathis et Léopold Bouglé 1G4
"""

from math import pi
import random

codePieceSecrete = random.randrange(1000, 9999)
codePieceSecrete = 1234

# La variable informationDesPieces liste toutes les pieces possibles dans le programme (13 pièces différentes). 
# Pour chaque pièce il y a un dictionnaire décrivant le nom de la pièce et les directions possibles ou le personnage peut aller.
informationDesPieces=[""] * 13
informationDesPieces[0] = {
    "description": "l'entrée",
    "directions" : { 'n': 1, 's': 8, 'e': 7, 'o': 10 }
}
informationDesPieces[1] = {
    "description": "le salon",
    "directions" : { 's': 0, 'e': 2}
}
informationDesPieces[2] = {
    "description": "la salle à manger",
    "directions" : { 'n': 3, 's': 7, 'o': 1 }
}
informationDesPieces[3] = {
    "description": "le pallier de l'étage",
    "directions" : { 'n': 4, 's': 2, 'e': 6, 'o': 5 }
}
informationDesPieces[4] = {
    "description": "le grenier",
    "directions" : { 's': 3 }
}
informationDesPieces[5] = {
    "description": "la chambre des parents",
    "directions" : { 'e': 3 }
}
informationDesPieces[6] = {
    "description": "la chambre des enfants",
    "directions" : { 'o': 3 }
}
informationDesPieces[7] = {
    "description": "la cuisine",
    "directions" : { 'n': 2, 'o': 0 }
}
informationDesPieces[8] = {
    "description": "le jardin",
    "directions" : { 'n': 0, 'o': 9 }
}
informationDesPieces[9] = {
    "description": "l'allée",
    "directions" : { 'n': 10, 'e': 8 }
}
informationDesPieces[10] = {
    "description": "le garage",
    "directions" : { 'n': 11, 's': 9, 'e': 0 }
}
informationDesPieces[11] = {
    "description": "la cave",
    "directions" : { 's': 10, 'o': 12 }
}
informationDesPieces[12] = {
    "description": "la pièce secrète",
    "directions" : { 'e': 11 }
}

# Affiche la pièce dans laquelle le personnage se trouve.
def afficherPiece(piece):
    print("Vous êtes dans", informationDesPieces[piece].get('description'))

# Retourne la pièce dans laquelle se trouve le personnage après le déplacement.
def deplacerPersonnage(piece, deplacement):
    directionsPossible = informationDesPieces[piece]['directions']

    if deplacement not in ['q', 'n', 's', 'o', 'e']:
        print(deplacement, "ne fait pas parti des touches possibles")

    elif deplacement in directionsPossible:
        nouvellePiece = directionsPossible.get(deplacement)
        
        if nouvellePiece == 4 and clefTrouvée == False:
            print("Le grenier est vérouillé, il vous faut la clef.")
            return piece
        
        if nouvellePiece == 4:
            print("Vous avez trouvé un papier. Il y est inscrit : Le code de la pièce secrète est", codePieceSecrete)

        if nouvellePiece == 12:
            nouvellePiece = saisirLeCodeSecret()

        return nouvellePiece
    elif deplacement != 'q':
        print("vous ne pouvez pas y aller")
    return piece

# Affiche les directions possibles de la pièce passée en paramètre.
def afficherDirectionPossible(piece):
    directionsPossible = informationDesPieces[piece]['directions']
    if 'n' in directionsPossible:
        print("n : Nord -", informationDesPieces[directionsPossible['n']]['description'])
    if 's' in directionsPossible:
        print("s : Sud -", informationDesPieces[directionsPossible['s']]['description'])
    if 'e' in directionsPossible:
        print("e : Est -", informationDesPieces[directionsPossible['e']]['description'])
    if 'o' in directionsPossible:
        print("o : Ouest -", informationDesPieces[directionsPossible['o']]['description'])

def saisirLeCodeSecret():
    derniereSaisie = ''
    print("Vous vous trouvé devant un clavier numérique, un code vous est demandé.")
    
    while derniereSaisie != 0 and derniereSaisie != codePieceSecrete :
        derniereSaisie = int(input("Saisir le code à 4 chiffres ou 0 pour quitter : "))
        if derniereSaisie != 0 and derniereSaisie != codePieceSecrete :
            print("Code non valide !!!! Accès refusé !!!!!!")
    
    if derniereSaisie == 0:
        return 11
    else:
        print("Code valide !!!!!!!")
        return 12
    

# Programme principal
clefTrouvée = False
pieceDuPersonnage = 0 # Contient la pièce dans laquelle se trouve le personnage.
derniereTouche = '' # Contient la dernière touche saisie au clavier.
while derniereTouche != 'q' and pieceDuPersonnage != 12:
    afficherPiece(pieceDuPersonnage)

    print("Ou désirez-vous aller? -------------------------------------")
    afficherDirectionPossible(pieceDuPersonnage)
    print("q : quitter")
    print("------------------------------------------------------------")

    derniereTouche = input("votre choix ? ")

    pieceDuPersonnage = deplacerPersonnage(pieceDuPersonnage, derniereTouche)
    if pieceDuPersonnage == 5 and clefTrouvée == False:
        clefTrouvée = True
        print("Vous avez trouvé une clef !")
    
    if pieceDuPersonnage == 12:
        print("Bien joué !! Vous êtes arrivé à la fin !")
