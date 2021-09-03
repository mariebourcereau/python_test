#!/usr/bin/python3

# print("\nMettre en majuscule la première lettre\n")

# def capital():
#     texte = input("\nEntrer un texte :\n").capitalize()
#     print(texte)

# capital()

def capital_case(v):
    """
Permet de passer la première lettre en capitale 
    """
    return v.capitalize()

# r = capital_case('marie')
# print(r)

def test_capital_case():
    resultat = capital_case("marie")
    assert resultat == 'Marie'