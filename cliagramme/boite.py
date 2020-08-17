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

    valeur_min = valeurs[1]
    valeur_max = valeurs[-1]

    nbr_valeurs = len(valeurs)

    valeur_Q1 = valeurs[round(nbr_valeurs / 4)]
    valeur_Q3 = valeurs[round(nbr_valeurs / 4 * 3)]

    if not nbr_valeurs % 2 == 0: # Si pair, sans le None
        medianne = round(
            (valeurs[nbr_valeurs // 2] + valeurs[nbr_valeurs // 2 + 1]) / 2
        )
    else: # Si impair
        medianne = valeurs[round(nbr_valeurs / 2)]

    palier = (valeur_max - valeur_min) / graduation

    espace_min_Q1 = round((valeur_Q1 - valeur_min) / palier)
    espace_Q1_medianne = round((medianne - valeur_Q1) / palier)
    espace_medianne_Q3 = round((valeur_Q3 - medianne) / palier)
    espace_Q3_max = round((valeur_max - valeur_Q3) / palier)

    valeur_min = round(valeur_min)
    valeur_Q1 = round(valeur_Q1)
    medianne = round(medianne)
    valeur_Q3 = round(valeur_Q3)
    valeur_max = round(valeur_max)

    diagramme = (
        (
            titre + '\n' if titre
            else
                ''
        )

        ### 1ère ligne
        + ' '
        # Patte
        + ' ' 
        + ' ' * espace_min_Q1 
        # Boite
        + '┌' + '─' * espace_Q1_medianne 
        + ('┬' if valeur_Q1 != medianne and medianne != valeur_Q3 else '─')
        + '─' * espace_medianne_Q3 + '┐'
        # Patte 
        + ' ' * espace_Q3_max
        + ' '

        + '\n'

        ### 2ème ligne
        + ' '
        # Patte
        + ('├' if valeur_min != valeur_Q1 else ' ')
        + '─' * espace_min_Q1 
        # Boite
        + '┤' + ' ' * espace_Q1_medianne 
        + ('│' if valeur_Q1 != medianne and medianne != valeur_Q3 else ' ')
        + ' ' * espace_medianne_Q3 + '├'
        # Patte
        + '─' * espace_Q3_max 
        + ('┤' if valeur_Q3 != valeur_max else ' ')

        + '\n'
        
        ### 3ème ligne
        + ' '
        # Patte
        + ' ' 
        + ' ' * espace_min_Q1
        # Boite
        + '└' + '─' * espace_Q1_medianne 
        + ('┴' if valeur_Q1 != medianne and medianne != valeur_Q3 else '─')
        + '─' * espace_medianne_Q3 + '┘'
        # Patte
        + ' ' * espace_Q3_max 
        + ' '

        + '\n'

        ### Ligne graduation
        + '─'
        # Patte
        + ('┼' if valeur_min != valeur_Q1 else '─')
        + '─' * espace_min_Q1 
        # Boite
        + '┼' + '─' * espace_Q1_medianne 
        + ('┼' if valeur_Q1 != medianne and medianne != valeur_Q3 else '─') 
        + '─' * espace_medianne_Q3 + '┼'
        # Patte
        + '─' * espace_Q3_max
        + ('┼' if valeur_Q3 != valeur_max else '─')
        + '─'

        + '\n'

        ### Ligne valeurs
        + ' '
        # Patte
        + (str(valeur_min) if valeur_min != valeur_Q1 else ' ')
        + ' ' * (espace_min_Q1 + (1 - len(str(valeur_min))))
        # Boite
        + str(valeur_Q1) + ' ' * (espace_Q1_medianne + (1 - len(str(valeur_Q1))))
        + (
            str(medianne) if valeur_Q1 != medianne and medianne != valeur_Q3 
            else
                ' '
        )
        + ' ' * (espace_medianne_Q3 + (1 - len(str(medianne))))
        + str(valeur_Q3) + ' ' * (espace_Q3_max + (1 - len(str(valeur_Q3))))
        # Patte
        + (str(valeur_max) if valeur_Q3 != valeur_max else ' ')
    )

    if return_diagramme:
        return diagramme

    print(diagramme)