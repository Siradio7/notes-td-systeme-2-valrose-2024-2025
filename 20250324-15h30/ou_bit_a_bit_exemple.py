def une_fonction_booleene_a_la_python(b1, b2, b3):
    print("b1=", b1)
    print("b2=", b2)
    print("b3=", b3)

Wb1 = 0b00000001
Wb2 = 0b00000010
Wb3 = 0b00000100


def la_meme_fonction_booleene_a_la_C(octet):
    b1 = (octet & Wb1) != 0
    b2 = (octet & Wb2) != 0
    b3 = (octet & Wb3) != 0

une_fonction_booleene_a_la_python(True, False, True)
la_meme_fonction_booleene_a_la_C(0b00000101)
la_meme_fonction_booleene_a_la_C(Wb1 | Wb3)