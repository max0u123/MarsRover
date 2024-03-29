# MarsRover
Vous connaissez le point d’impact du Rover (x,y) et son orientation de départ (N,S,E,W)

Le Rover sait avancer, reculer et tourner de 90° sur lui-même dans les 2 sens.
Après chaque commande il renvoie son état (position et orientation)
Les planètes sont toroïdales et de taille finie entière.

### Lancer le projet
Lancer ```pip3 install -r requirements.txt``` dans le dossier MarsRover pour installer les requirements.

Ensuite, pour lancer le projet, il faut lancer le fichier ```server_main.py```. 
Par la suite, lorsque cela est demandé, lancer le fichier ```client.py```.

> Toutes les interactions seront à faire depuis le client.

##### Commandes de lancement
```python src/server_main.py```

```python src/client.py```

### Lancer les tests

Pour lancer les tests, il suffit de lancer la commande :
```python -m unittest tests.test_rover```.

**Groupe A:**
Maxime Coulon
Gabriel Odillard
Lucas Ducourneau
Rémi Rault
Maxence Quilichini
