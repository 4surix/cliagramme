#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python 3.6.2
# ----------------------------------------------------------------------------

"""Diagramme en boite.

    │      ┌────────┬───────────┐    │
    ├──────┤        │           ├────┤
    │      └────────┴───────────┘    │

────┴──────┴────────┴───────────┴────┼───
    Mini   Q1       Médiane     Q3   Max
    2      5        6           7    9

[
    2, 5, 5, 5.5, 6, 6, 6.5, 7, 7, 9
]

"""

def boite(*, 
        titre:str = None, valeurs:list, 
        graduation:int = 30, return_diagramme:bool = False
    ) -> None or str:

    valeurs = sorted(valeurs)

    # Rajout de None en position 0.
    # Cette valeur ne sera jamais utilisée, 
    #   elle sert à déplacer les indexs de 1
    #   pour que l'accée aux indexs soit plus intuitive.
    valeurs.insert(0, None)

    nbr_valeurs = len(valeurs) - 1 # On ne compte pas le None

    valeur_min = valeurs[1]
    valeur_max = valeurs[-1]

    valeur_Q1 = valeurs[round(nbr_valeurs / 4)]
    valeur_Q3 = valeurs[round(nbr_valeurs / 4 * 3)]

    if nbr_valeurs % 2 == 0:
        medianne = (
            (valeurs[nbr_valeurs // 2] + valeurs[nbr_valeurs // 2 + 1]) / 2
        )
        if str(medianne)[-2:] == '.0':
            medianne = int(medianne)
    else:
        medianne = valeurs[round(nbr_valeurs / 2)]

    palier = (valeur_max - valeur_min) / graduation

    espace_min_Q1 = round((valeur_Q1 - valeur_min) / palier)
    espace_Q1_medianne = round((medianne - valeur_Q1) / palier)
    espace_medianne_Q3 = round((valeur_Q3 - medianne) / palier)
    espace_Q3_max = round((valeur_max - valeur_Q3) / palier)

    valeur_min = round(valeur_min, 3)
    valeur_Q1 = round(valeur_Q1, 3)
    medianne = round(medianne, 3)
    valeur_Q3 = round(valeur_Q3, 3)
    valeur_max = round(valeur_max, 3)

    surplus = 0

    len__ = len(str(valeur_min))
    if len__ > espace_min_Q1 and len__ > surplus:
        surplus = len__

    len__ = len(str(valeur_Q1))
    if len__ > espace_Q1_medianne and len__ > surplus:
        surplus = len__

    len__ = len(str(medianne))
    if len__ > espace_medianne_Q3 and len__ > surplus:
        surplus = len__

    len__ = len(str(valeur_Q3))
    if len__ > espace_Q3_max and len__ > surplus:
        surplus = len__

    espace_min_Q1 += surplus
    espace_Q1_medianne += surplus
    espace_medianne_Q3 += surplus
    espace_Q3_max += surplus

    diagramme = (
        (
            titre + '\n' if titre
            else
                ''
        )

        ### 1ère ligne
        + ' '
        # Patte
        + (' ' + ' ' * espace_min_Q1 if valeur_min != valeur_Q1 else '')
        # Boite
        + '┌' 
        + '─' * espace_Q1_medianne 
        + ('┬' if valeur_Q1 != medianne and medianne != valeur_Q3 else '─')
        + '─' * espace_medianne_Q3 
        + '┐'
        # Patte 
        + (' ' * espace_Q3_max  + ' ' if valeur_Q3 != valeur_max else '')

        + '\n'

        ### 2ème ligne
        + ' '
        # Patte
        + ('├' + '─' * espace_min_Q1 if valeur_min != valeur_Q1 else '')
        # Boite
        + ('┤' if valeur_min != valeur_Q1 else '│')
        + ' ' * espace_Q1_medianne 
        + ('│' if valeur_Q1 != medianne and medianne != valeur_Q3 else ' ')
        + ' ' * espace_medianne_Q3 
        + ('├' if valeur_Q3 != valeur_max else '│')
        # Patte
        + ('─' * espace_Q3_max  + '┤' if valeur_Q3 != valeur_max else '')

        + '\n'
        
        ### 3ème ligne
        + ' '
        # Patte
        + (' ' + ' ' * espace_min_Q1 if valeur_min != valeur_Q1 else '')
        # Boite
        + '└' + '─' * espace_Q1_medianne 
        + ('┴' if valeur_Q1 != medianne and medianne != valeur_Q3 else '─')
        + '─' * espace_medianne_Q3 + '┘'
        # Patte
        + (' ' * espace_Q3_max  + ' ' if valeur_Q3 != valeur_max else '')

        + '\n'

        ### Ligne graduation
        + '─'
        # Patte
        + ('┼' + '─' * espace_min_Q1 if valeur_min != valeur_Q1 else '')
        # Boite
        + '┼' + '─' * espace_Q1_medianne 
        + ('┼' if valeur_Q1 != medianne and medianne != valeur_Q3 else '─') 
        + '─' * espace_medianne_Q3 + '┼'
        # Patte
        + ('─' * espace_Q3_max + '┼' if valeur_Q3 != valeur_max else '')
        + '─'

        + '\n'

        ### Ligne valeurs
        + ' '
        # Patte
        + ( 
            '' if valeur_min == valeur_Q1 
            else
                str(valeur_min) + ' ' * (espace_min_Q1 + (1 - len(str(valeur_min))))
        )
        # Boite
        + str(valeur_Q1) 
        + ' ' * (espace_Q1_medianne + (1 - len(str(valeur_Q1))))
        + (
            str(medianne) if valeur_Q1 != medianne and medianne != valeur_Q3 
            else
                ' '
        )
        + ' ' * (espace_medianne_Q3 + (1 - len(str(medianne))))
        + str(valeur_Q3)
        # Patte
        + (
            '' if valeur_Q3 == valeur_max
            else
                ' ' * (espace_Q3_max + (1 - len(str(valeur_Q3)))) + str(valeur_max)
        )
    )

    if return_diagramme:
        return diagramme

    print(diagramme)