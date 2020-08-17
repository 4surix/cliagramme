## Cliagramme
Module servant à afficher et gérer facilement des diagrammes en console.  
D'où le nom, CLI diagramme, cliagramme.  
  
Les diagrammes disponible sont :
- Diagramme en bâton (ou à barre).
- Diagramme en boite (ou à moustache).
- Diagramme rectangulaire (équivalent de circulaire).

## Aperçu

```python
import cligramme

# Source : https://www.faune-france.org/

DONNEES_HIRONDELLE = {
    # mois: [En 2019, En 2020]
    'Jan.': [0.0, 0.0], 
    'Fev.': [0.08, 0.13], 
    'Mars': [2.49, 0.76], 
    'Avril': [10.13, 4.18], 
    'Mai': [7.04, 5.93], 
    'Juin': [5.07, 5.26], 
    'Jui.': [14.2, 10.5], 
    'Aout': [19.75, 0.0], 
    'Sep.': [14.79, 0.0], 
    'Oct.': [0.35, 0.0], 
    'Nov.': [0.05, 0.0], 
    'Dec.': [0.0, 0.0]
}

LISTE_MOIS = DONNEES_HIRONDELLE.keys()

cliagramme.baton(
    titre="Présence Hirondelle de rivage par mois en France.",
    valeurs=DONNEES_HIRONDELLE,
    legende=[
        "Année 2019",
        "Année 2020"
    ],
    max_valeurs_y=12,
)

INDEX_2019 = 0
INDEX_2020 = 1

MOIS_ACTUEL = 8

cliagramme.boite(
    titre="Présence Hirondelle de rivage en 2019 en France.",
    valeurs=[
        DONNEES_HIRONDELLE[mois][INDEX_2019]
        for mois in LISTE_MOIS
    ],
    graduation=40
)

cliagramme.boite(
    titre="Présence Hirondelle de rivage en 2020 en France.",
    valeurs=[
        DONNEES_HIRONDELLE[mois][INDEX_2020]
        for mois in LISTE_MOIS
    ],
    graduation=40
)

cliagramme.rectangulaire(
    titre="Plus grande présence Hirondelle de rivage en 2019 en France.",
    valeurs={
        mois: DONNEES_HIRONDELLE[mois][INDEX_2019]
        for mois in LISTE_MOIS
    }
)
```

![](https://i.imgur.com/gYBRGFA.png)

## Documentation

#### baton(\*, titre:str = None, valeurs:dict or list, legende:list = None, max_valeurs_y:int = 10, min_y_nul:bool = True, saut_valeur_y:int = 1, couleur:bool = True, return_diagramme:bool = False) -> None or str:
Diagramme en bâton.  

##### titre:str
Titre du diagramme.

##### valeurs:dict or list
Valeurs qui constituera le diagramme.  
Si l'objet est de type `list`, le programme va comprendre que c'est une série.

##### legende:list
Légende du diagramme. Utile si il y a plusieurs bâton par valeur en abscisse.  

##### max_valeurs_y:int
Le nombre maximum de valeur en y (ordonnée). Autrement dit, la hauteur maximum du diagramme.  

##### min_y_nul:bool
Définie si la valeur minimal en y doit être zéro. Si `min_y_nul=False` alors la valeur minimal en y sera la plus petite valeur.  

##### saut_valeur_y:int
Définie le nombre de valeur en y qu'il faut sauter à chaque affichage de valeur. La valeur maximum et minimum seront toujours affichées.  

##### couleur:bool
Définie si le diagramme sera en couleur ou non.  

##### return_diagramme:bool
Si `return_diagramme=True`, n'affiche pas le diagramme et le retourne à la place.  

##### Exemple :  

```python
import cliagramme

cliagramme.baton(
    titre="Nombre d'enfant par famille",
    valeurs=[
        2, 3, 4, 0, 2, 5, 3, 0, 2, 1, 0, 6, 0, 3, 2
    ],
    max_valeurs_y=12,
    saut_valeur_y=3, # 12/3 == 4, seulement 4 valeurs en y
                     # seront affichées espacées de 3 blanc.
    couleur=False
)
```

![](https://i.imgur.com/eWcBKhf.png)

#### boite(\*, titre:str = None, valeurs:list, graduation:int = 30, return_diagramme:bool = False) -> str:
Diagramme en boite (ou à moustache).

##### titre:str
Titre du diagramme.  

##### valeurs:list
Valeurs qui constituera le diagramme.  

##### graduation:list
Définie le nombre maximum de trait dans la graduation. Autrement dit, la longueur maximum du diagramme.  

##### return_diagramme:bool
Si `return_diagramme=True`, n'affiche pas le diagramme et le retourne à la place.  

##### Exemple :  
  
```python
import cliagramme

notes = [
    16, 7, 10, 8, 19, 19, 4, 1, 17, 15, 14, 20, 1
]

cliagramme.boite(
    titre="Notes d'élèves.",
    valeurs=notes,
    graduation=20
)
```

![](https://i.imgur.com/qGXbdr0.png)

#### rectangulaire(\*, titre:str = None, valeurs:dict or list, legende:bool = True, longueur:int = 50, largeur:int = 3, couleur:bool = True, return_diagramme:bool = False) -> None or str:

##### titre:str
Titre du diagramme.  

##### valeurs:dict or list
Valeurs qui constituera le diagramme.  
Si l'objet est de type `list`, le programme va comprendre que c'est une série.  

##### legende:bool
Permet d'afficher, ou non, la légende du diagramme.  

##### longueur:int
Définie la longueur du diagramme.  

##### largeur:int
Définie la largeur du diagramme.  

##### couleur:bool
Définie si le diagramme sera en couleur ou non.  

##### return_diagramme:bool
Si `return_diagramme=True`, n'affiche pas le diagramme et le retourne à la place.  

##### Exemple :  
  
```python
import cliagramme

cliagramme.rectangulaire(
    titre="Catégorie d'espèces les plus touchées suivant leurs taux d'espèces menacées.",
    valeurs={
        "Mammifères": 14,
        "Reptiles": 24,
        "Amphibiens": 23,
        "Oiseaux nicheurs": 32,
        "Poisson d'eau douce": 19,
        "Crustacés": 28,
        "Flore": 15
    },
    largeur=2,
    longueur=20
)
```

![](https://i.imgur.com/TYlKF0Q.png)