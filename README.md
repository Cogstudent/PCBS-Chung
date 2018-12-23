# Programing for Cognitive and Brain Science
## Final project

<br>
### Context

<br>
### Problem

<br>
### Algorithm

<br>
### Instructions for use


***

Music cognition
We intend to measure the ability to perceive and reproduce tone sequences that differ with respect to the tone-onset intervals/pulsation/rythm.
Hypothesis: listeners generate an internal clock while listening to a temporal pattern.

Expérience 1
Génération des séquences de son
Présentation d'un stimulus (sélectionné aléatoirement dans une liste) audio en boucle
Lorsque le sujet se sent pret, il appuie sur une touche (par exemple : Entrée) pour arreter la présentation du stimulus.
Le sujet est invité à reproduire quatre fois la séquence : chaque fois qu'il tape, un son similaire à celui de la présentation est émis. Lorsque plus aucun son n'est émis lorsqu'il tape, c'est qu'il a bien reproduit au moins 4 fois.
Possibilité de ré-essayer ou de passer au stimulus suivant.
35 stimuli au total (environ 50min)

Analyse
Nb de présentations du stimulus (= temps de préparation) par catégorie de stimulus


## **Objectif**
Générer 35 séquences de son classés en 7 catégories, les présenter de manière aléatoire au sujet qui peut les ré-écouter autant de fois que possibles. On lui demande ensuite de reproduire le rythme des séquences de son à l'aide du clavier. Le programme compare ensuite les performances des sujets avec les séquences pour mettre en évidence la difficulté à reproduire le rythme selon la catégorie de rythme.

## **Plan**
1. Créer un fichier d'arrays
2. Ecrire une fonction qui transforme les arrays en 35 séquences de sons et les enregistre sous forme de fichiers audio
3. Ecrire une fonction qui présente de manière aléatoire les 35 séquences à un sujet et lui demande de les répéter.