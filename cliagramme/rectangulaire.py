#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python 3.6.2
# ----------------------------------------------------------------------------

"""Diagramme rectangulaire.

┌──────────────────┐
│▓▓▓▓▓▒▒▒▒▓▓▓▒▒▒▓▓▓│
├──────────────────┘
│ - Pomme (25%)
│ - Poire (25%)
│ - Fraise (16%)
│ - Tomate (16%)
│ - Mangue, Cassis, Mandarine (16%)

"""


try: import colorama
except ImportError as exception:
    EXEPTION_COLORAMA = exception
else:
    EXEPTION_COLORAMA = None


CARACS = ['▒', '▓']

COULEURS = (
    '\033[32m',
    '\033[92m'
)
COULEUR_MAZ = '\033[39m'

def rectangulaire(*,
        titre:str = None, valeurs:dict or list, legende:bool = True,
        longueur:int = 50, largeur:int = 3,
        couleur:bool = True, return_diagramme:bool = False
    ) -> None or str:

    # Si valeurs est une serie.
    if valeurs.__class__ == list:

        valeurs__ = {}

        for valeur in valeurs:

            if valeur in valeurs__:
                valeurs__[valeur] += 1
            else:
                valeurs__[valeur] = 1

        valeurs = valeurs__


    total:int = sum(valeurs.values())

    valeurs:list = sorted(
        valeurs.items(), 
        key=lambda valeur: valeur[1],
        reverse=True
    )

    min_valeur = total / longueur

    valeurs__ = []

    for item, valeur in valeurs:

        if min_valeur > valeur:
            valeurs__[-1][0] += f', {item}'
            valeurs__[-1][1] += valeur

        else:
            valeurs__.append([str(item), valeur])

    valeurs = valeurs__

    longueur_bord = sum(
        round(longueur * valeur / total) for item, valeur in valeurs
    )

    diagramme = (
        (
            titre + '\n\n' if titre
            else
                ''
        )

        + '┌' + '─' * longueur_bord + '┐'

        + '\n│'
        + '│\n│'.join(
            [
                ''.join(
                    COULEURS[index % 2] 
                    + CARACS[index % 2] * round(longueur * valeur / total)
                    + COULEUR_MAZ
                    for index, (item, valeur) in enumerate(valeurs, 1)
                )
            ] * largeur
        )
        + '│'

        + ('\n├' if legende else '\n└') + '─' * longueur_bord + '┘'

        + (
            '' if not legende
            else
                '\n│ - ' 
                + '\n│ - '.join(
                    COULEURS[index % 2] 
                    + str(item) 
                    + ' (' + str(round(100 * valeur / total)) + '%)'
                    + COULEUR_MAZ
                    for index, (item, valeur) in enumerate(valeurs, 1)
                )
        )
    )


    if return_diagramme:
        return diagramme


    if couleur:
        if EXEPTION_COLORAMA:
            raise EXEPTION_COLORAMA
        colorama.init()

    print(diagramme)

    if couleur:
        colorama.deinit()