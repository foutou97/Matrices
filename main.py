import math
import random
import statistics

#création matrice 2x3

matrice1 = [[0] * 3 for _ in range(2)]
matrice2 = [[0] * 3 for _ in range(2)]

#remplissage de la première matrice

for i in range(2):
    for j in range(3):
        matrice1[i][j] = random.randint(1, 100)

#remplissage de la deuxième matrice

for i in range(2):
    for j in range(3):
        nombre_aleatoire = random.randint(1, 100)
        while nombre_aleatoire in [matrice1[x][y] for x in range(2) for y in range(3)]: #La boucle while pour générer un nouveau nombre aléatoire pour la deuxième matrice jusqu' ce qu'il soit différent de tous les nombres présents dans la première matrice. cela garantit que les nombres dans les deux matrice sont différents.
            nombre_aleatoire = random.randint(1, 100)
        matrice2[i][j] = nombre_aleatoire

#affichage de la première matrice

print("Matrice 1:")
for ligne in matrice1:
    print(ligne)

#affichage de la deuxième matrice

print("Matrice 2:")
for ligne in matrice2:
    print(ligne)

#vérification du type de donnés de la matrice
type_donnees = type(matrice1[0][0])

#calcul de la moyenne
moyenne = statistics.mean([element for ligne in matrice1 for element in ligne])

#calcul du mode
elements = [element for ligne in matrice1 for element in ligne]
occurrences = {}
for element in elements:
    occurrences[element] = occurrences.get(element, 0) + 1
max_occurrence = max(occurrences.values())
mode = [element for count in occurrences.items() if count == max_occurrence]

#calcul de la médiane
mediane = statistics.median([element for ligne in matrice1 for element in ligne])

#affichage des résultats
print("Type de données de la premièère matrice :", type_donnees.__name__)
print("Moyenne des données de la premièère matrice :", moyenne)
print("Mode des données la premièère matrice:",mode)
print("Médiane des données la premièère matrice :", mediane)

#addition des deux matrices
resultat = [[0] * 3 for _ in range(2)]

for i in range(2):
    for j in range(3):
        resultat[i][j] = matrice1[i][j] + matrice2[i][j]

#affichage du résultat

print("Résultat de l'addition des matrices :")
for ligne in resultat:
    print(ligne)

# soustraction des deux matrices

resultat = [[0] * 3 for _ in range(2)]

for i in range(2):
    for j in range(3):
        resultat[i][j] = matrice1[i][j] - matrice2[i][j]

# affichage du résultat

print("Résultat de la soustraction des matrices :")
for ligne in resultat:
    print(ligne)

#transposition de la première matrice

transposee = [list(colonne) for colonne in zip(*matrice1)] #zip(*matrice1) pour inverser les lignes et les colonnes de la matrice1. ensuite,les colonnes transposées sont converties en listes à l'aide de la compréhention de liste,[list(colonne) for colonne in zip(*matrice1)]. enfin le résultat de la transposition est affiché en utillisant une boucle for.

#affichage du résultat

print("transposée de la première matrice:")
for ligne in transposee:
    print(ligne)

#mutiplication de la première matrice par un scalaire

scalaire = 2
resultat = [[element * scalaire for element in ligne] for ligne in matrice1]

#affichage du résultat

print("résultat de la multiplication de la première matrice par un scalaire:")
for ligne in resultat:
    print(ligne)

# calcul de l'écart entre les deux matrices

ecart = 0
for i in range(2):
    for j in range(3):
        difference = matrice1[i][j] - matrice2[i][j]
        ecart += difference ** 2
ecart = math.sqrt(ecart)

#affochage du résultat
print("l'écart entre les deux matrice :", ecart)












