def afficher_plateau(plateau):
    print("  1 2 3")
    for i in range(3):
        row = str(i+1) + " "
        for j in range(3):
            row += plateau[i][j] + " "
        print(row)

def verif_alignement(plateau, joueur):
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2] == joueur:
            return True
        if plateau[0][i] == plateau[1][i] == plateau[2][i] == joueur:
            return True
    if plateau[0][0] == plateau[1][1] == plateau[2][2] == joueur:
        return True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] == joueur:
        return True
    return False

def jouer():
    rejouer = True
    
    joueur1 = input("Entrez le nom du premier joueur : ")
    joueur2 = input("Entrez le nom du deuxième joueur : ")
    symboles = ['X', 'O']
    
    while rejouer:
        plateau = [[" " for i in range(3)] for j in range(3)]
        joueur_courant = joueur1
        symbole_courant = symboles[0]
        nb_tours = 0

        while True:
            afficher_plateau(plateau)
            print(f'C\'est au tour de {joueur_courant} ({symbole_courant})')
            ligne = int(input('Entrez le numéro de ligne (1-3) : '))
            colonne = int(input('Entrez le numéro de colonne (1-3) : '))

            if plateau[ligne-1][colonne-1] != " ":
                print("Cette case est déjà prise. Essayez une autre.")
                continue

            plateau[ligne-1][colonne-1] = symbole_courant
            nb_tours += 1

            if verif_alignement(plateau, symbole_courant):
                afficher_plateau(plateau)
                print(f'{joueur_courant} ({symbole_courant}) a gagné !')
                break
            elif nb_tours == 9:
                afficher_plateau(plateau)
                print('Match nul !')
                break

            joueur_courant = joueur2 if joueur_courant == joueur1 else joueur1
            symbole_courant = symboles[(symboles.index(symbole_courant) + 1) % 2]

        rejouer = input("Voulez-vous rejouer ? (Oui/Non) : ")
        rejouer = True if rejouer.lower() == "oui" else False

    print("Merci d'avoir joué !")

jouer()
