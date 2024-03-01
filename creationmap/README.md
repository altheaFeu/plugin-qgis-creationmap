# Plugin QGIS pour créer une carte de densité de la population

## Composition du Projet
Ce projet QGIS est composé de 4 principaux scripts : 

- **`CreationMap.py`** qui est le cœur du projet et contient les classes principales
- **`CreateDensity.py`** qui comporte toutes les fonctions permettant de calculer la densité des habitants par commune
-  **`Centroides.py`** qui comportes toutes les fonctions permettant de calculer les centroÏdes
- **`Affichage.py`** qui permet d'appliquer la symbologie choisie par l'utilisateur, le changement de crs et la sauvegarde des données.

## Installation

Ouvrez votre terminal ou votre ligne de commande et exécutez la commande suivante pour cloner le référentiel du plugin sur votre machine locale :
```bash
git clone https://github.com/altheaFeu/plugin-qgis-creationmap.git
```

Copier le dossier **`creationmap`** dans le répertoire de vos plugins QGIS **`~QGIS3/profiles/default/python/plugins/`**. L'extension apparaîtra en haut à droite dans la barre d'outil.
