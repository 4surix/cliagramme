#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python 3.6.2
# ----------------------------------------------------------------------------

"""Diagramme en bâton.

   │
 40│ ▐
   │ ▐     ▐
 20│ ▐  ▐  ▐     ▐
   │ ▐  ▐  ▐  ▐  ▐  ▐  ▐
  0└─────────────────────
     2  4  6  8  10 12 14

{
    2: 40,
    4: 20,
    6: 30,
    8: 10,
    10: 20,
    12: 10,
    14: 10
}

"""

import sys

try: import colorama
except ImportError as exception:
    EXEPTION_COLORAMA = exception
else:
    EXEPTION_COLORAMA = None


COULEURS = (
    '\033[31m',
    '\033[32m',
    '\033[33m',
    '\033[34m',
    '\033[35m',
    '\033[36m',
    '\033[37m'
)
COULEUR_MAZ = '\033[39m' 


CARAC_BARRE_Y = '│'
CARAC_BARRE_X = '─'
CARAC_BARRE_H_INF = '_'
CARAC_BARRE_H_EGA = '▄'
CARAC_BARRE_H_SUP = '█'

CARAC_BARRE_H_INF_COULEUR = [
    couleur + CARAC_BARRE_H_INF + COULEUR_MAZ 
    for couleur in COULEURS
]
CARAC_BARRE_H_EGA_COULEUR = [
    couleur + CARAC_BARRE_H_EGA + COULEUR_MAZ 
    for couleur in COULEURS
]
CARAC_BARRE_H_SUP_COULEUR = [
    couleur + CARAC_BARRE_H_SUP + COULEUR_MAZ 
    for couleur in COULEURS
]


def baton(*, 
        titre:str = None, valeurs:dict or list, legende:list = None,
        max_valeurs_y:int = 10, min_y_nul:bool = True, 
        saut_valeur_y:int = 1,
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

    # Vérification du type des valeurs
    #   et détermination de la taille max des valeurs y et x.

    min_valeur_y = sys.maxsize
    max_valeur_y = 0

    taille_max_valeurs_x = taille_max_valeurs_y = 0
    taille_baton = 0

    __valeurs = {}
    
    for valeur_x, valeur_y in valeurs.items():

        if isinstance(valeur_y, (tuple, list)):
            nombre_baton = len(valeur_y)

            if not nombre_baton:
                raise ValueError('')

            __valeur_y = []

            taille_valeur_y = 0

            for valeur_y in valeur_y:

                if not isinstance(valeur_y, (int, float)):
                    raise ValueError('')

                valeur_y = round(valeur_y, 3)

                __valeur_y.append(valeur_y)

                if valeur_y > max_valeur_y:
                   max_valeur_y = valeur_y

                elif valeur_y < min_valeur_y:
                   min_valeur_y = valeur_y

                len_valeur_y = len(str(valeur_y))

                if len_valeur_y > taille_valeur_y:
                    taille_valeur_y = len_valeur_y

        elif isinstance(valeur_y, (int, float)):

            valeur_y = round(valeur_y, 3)

            __valeur_y = [valeur_y]

            nombre_baton = 1

            if valeur_y > max_valeur_y:
               max_valeur_y = valeur_y

            elif valeur_y < min_valeur_y:
               min_valeur_y = valeur_y

            taille_valeur_y = len(str(valeur_y))

        else:
            raise ValueError('')


        if isinstance(valeur_x, float):

            __valeur_x = valeur_x = round(valeur_x, 3)

            taille_valeur_x = len(str(valeur_x))

        elif isinstance(valeur_x, (int, str)):

            __valeur_x = valeur_x

            taille_valeur_x = len(str(valeur_x))

        else:
            raise ValueError('')


        __valeurs[__valeur_x] = __valeur_y


        if nombre_baton > taille_baton:
            taille_baton = nombre_baton

        if taille_valeur_x > taille_max_valeurs_x:
           taille_max_valeurs_x = taille_valeur_x

        if taille_valeur_y > taille_max_valeurs_y:
           taille_max_valeurs_y = taille_valeur_y


    valeurs = __valeurs


    # Espacement des bâtons.

    if taille_baton >= taille_max_valeurs_x:
        espacement_baton = ' '
        taille_max_valeurs_x = taille_baton

    else:
        espacement_baton = ' ' * (taille_max_valeurs_x - (taille_baton - 1))


    # Détermination du palier et de la valeur de la première ligne.

    min_valeur_y = 0 if min_y_nul else min_valeur_y

    palier = (max_valeur_y - min_valeur_y) / max_valeurs_y

    if not palier:
        palier = 1

    surplus = max_valeur_y % palier

    ligne_valeur_y = round(max_valeur_y - surplus)

    # Création de l'affichage.

    affichage =  []

    saut_effectuée = saut_valeur_y

    for _ in range(max_valeurs_y):

        if saut_valeur_y > saut_effectuée:
            indication_ligne = ''
            saut_effectuée += 1

        else:
            indication_ligne = str(int(ligne_valeur_y))
            saut_effectuée = 0

        ligne = (
            ' ' * (taille_max_valeurs_y - len(indication_ligne) + 1)
            + indication_ligne
            + CARAC_BARRE_Y
            + ' '
        )

        for valeurs_y in valeurs.values():

            index_baton = 0

            for valeur_y in valeurs_y:

                if valeur_y > ligne_valeur_y:
                    ligne += (
                        CARAC_BARRE_H_SUP_COULEUR[index_baton] if couleur
                        else
                            CARAC_BARRE_H_SUP
                )
                 
                elif valeur_y == ligne_valeur_y:
                    ligne += (
                        CARAC_BARRE_H_EGA_COULEUR[index_baton] if couleur
                        else
                            CARAC_BARRE_H_EGA
                    )

                elif (min_valeur_y + palier >= ligne_valeur_y
                      and valeur_y != min_valeur_y):
                    ligne += (
                        CARAC_BARRE_H_INF_COULEUR[index_baton] if couleur
                        else
                            CARAC_BARRE_H_INF
                    )
                 
                else:
                    ligne += ' '

                index_baton += 1

            ligne += espacement_baton

        ligne_valeur_y -= palier

        affichage.append(ligne)

    # Ajout de la ligne des absicces.

    affichage.append(
        ' ' * (taille_max_valeurs_y - len(str(min_valeur_y)) + 1)
        + str(min_valeur_y)
        + '└'
        + CARAC_BARRE_X * len(valeurs) * (taille_max_valeurs_x + 1)
    )    

    # Ajout des valeurs en absices.

    affichage.append(
        ' ' * (taille_max_valeurs_y + 3)
        + ''.join(
            "%s%s" % (
                valeur_x, 
                ' ' * (taille_max_valeurs_x - len(str(valeur_x)) + 1)
            )
            for valeur_x in valeurs.keys()
        )
    )


    # Affichage.

    diagramme = (
        (titre + '\n\n' if titre else '')
        + '\n'.join(affichage)
        + (
            '\n\n' + '\n'.join(
                '| - ' + couleur + indication + COULEUR_MAZ
                for couleur, indication in zip(COULEURS, legende)
            )
            if legende else ''
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