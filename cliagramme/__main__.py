#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python 3.6.2
# ----------------------------------------------------------------------------

import json
import requests
import argparse


from boite import boite
from baton import baton
from rectangulaire import rectangulaire


def jsonrequest(url, methode='GET'):
    return requests.request(methode, url).json()

def jsonfile(chemin, mode='r', *, encoding='utf-8'):
    file = open(chemin, mode, encoding=encoding)
    data = file.read()
    file.close()
    return json.loads(data)

def eval_valeurs(texte:str) -> dict:
    return eval(
        texte,
        {
            'jsonrequest': jsonrequest,
            'jsonfile': jsonfile
        }
    )


parser = argparse.ArgumentParser()

parser.add_argument('valeurs',
    type=eval_valeurs
)
parser.add_argument('--titre',
    type=str,
    default=None
)

parser.add_argument('--baton',
    dest='diagramme',
    action='store_const', const=baton
)
parser.add_argument('--boite',
    dest='diagramme',
    action='store_const', const=boite
)
parser.add_argument('--rectangulaire',
    dest='diagramme',
    action='store_const', const=rectangulaire
)

args = parser.parse_args()

diagramme = args.__dict__.pop('diagramme')
diagramme(**args.__dict__)