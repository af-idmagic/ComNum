**Opérations basiques avec des nombres complexes**
(c) Alexey FEDOROV (idmagic) 2020

`ComNum_test.py`
---
La classe ComNum définit un [nombre complexe](https://en.wikipedia.org/wiki/Complex_number) :

`>>> print(ComNum(X, Y))
X + Y*i`

où i est l'unité imaginaire (i*i = -1),
X est la partie réelle et Y est la partie imaginaire du nombre

Le paquet contient les méthodes basiques se rapportant au nombres complexes :

  *  `print` :		    impression d'un nombre complexe sous forme classique 'X + Y*i'
  *  `round` :		    arrondissement des parties réelle et imaginaire d'un nombre complexe aux n décimales
  *  `==` :			    vérification d'égalité entre 2 nombres complexes
  *  `+ - * /` :		les opérations arithmetiques de base
  *  `modul`, `argt` :	modulus and argument d'un nombre complexe
  *  `conjug` :		    nombre complexe conjugué (X - Y*i)
  *  `recipr` :		    nombre complexe réciproqué
  *  `pr_sqrt` :		racine carrée principale d'un nombre complexe
  *  `pr_com_ln` :	    valeur principale de logarithme naturel d'un nombre complexe
  *  `com_exp` :		un nombre complexe en puissance n (où n est obligatoirement un nombre entier)
  *  `com_exp_alt` :	idem, solution alternative de calcul
  
Lancez `help(ComNum)` pour lire les docstrings et les doctests démonstratifs pour ces méthodes.
  
`ComNum_use_examples.py`
---
Script démonstratif pour des opérations avec des nombres complexes
qui utilise toutes les méthodes définis dans ComNum_test.py

Lancez-le pour une démonstration concise et explicite.
