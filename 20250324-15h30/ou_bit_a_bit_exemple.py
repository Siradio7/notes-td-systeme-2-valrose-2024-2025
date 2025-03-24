# COMMENT UTILISE-T-ON LE BIT A BIT EN C POUR
# PASSER DES PARAMETRES A UNE FONCTION ?

# illustration sur un exemple

def f(b1, b2, b3):
    """
    une fonction Booléene écrite "à la Python" 
    (ou autre langage avec type Booléen), avec *3* paramètres
    """
    print("b1=", b1)
    print("b2=", b2)
    print("b3=", b3)

# en C, le triplet de Booleens se représente de manière compacte
# en utilisant un octet (8 bits)

# exemple: `(True, False, True)` se code par 
# l'octet `0b00000101`, i.e. l'entier 5 en écriture décimale
# note : le `0b` indique qu'on écrit en binaire

# pour passer du triplet de Booléens à l'octet, et vice versa,
# on utilise les masques de bits suivants:
masque_b1 = 0b00000001 # b1 sera codé sur le bit de poids faible
masque_b2 = 0b00000010 # b2 sera codé sur le bit suivant 
masque_b3 = 0b00000100 # b3 sera codé sur le bit encore après


# exemple de passage d'un octet à un triplet de Booléens avec les
# masques de bits et l'opérateur `&` (et bit à bit)

def f2(octet):
    """
    la fonction f précédente, mais avec *un seul* paramètre, "à la C"
    """
    b1 = (octet & masque_b1) != 0   
    b2 = (octet & masque_b2) != 0
    b3 = (octet & masque_b3) != 0
    f(b1, b2, b3)
    # note : on utilise `!= 0` pour convertir l'entier en booléen, 
    # mais c'est inutile car implicite en C (True ~ "non nul", False ~ 0)
    # et "semi-implicite" en Python (si on n'utilise pas le typage statique), 
    # sous influence de C


# Exemple de passage d'un triplet de Booléens à un octet

# Supposons qu'on veuille faire l'appel de fonction suivant

f(True, False, True)

# il faut donc coder (b1, b2, b3)=(True, False, True) en un seul octet.
# En C, on fait cela avec l'opérateur `|` (ou bit à bit).
# On utilise les masques de bits pour faire le codage:
# on liste les bits à 1 et on les additionne (avec `|` ou `+`)

f2(masque_b1 | masque_b3) # ou bien `f2(masque_b1 + masque_b3)`