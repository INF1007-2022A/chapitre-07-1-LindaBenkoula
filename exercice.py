#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import sys
sys.path.insert(1, 'D:\charge_cours\INF1007\H2021\exercices\\2021H_ch6_1_exercices')
from exercice_ch6 import frequence
from turtle import *
import re

# TODO: Définissez vos fonction ici
#volume et masse d'un ellipsoide
def compute_volume_and_mass(a=2, b=4, c=6, masse_vol=8):
    V = math.pi*a*b*c*4/3
    masse = masse_vol*V
    return V, masse

#dessine les branches de l'arbre en utilisant la réscursivité --> 3 paramètres :
# longueur des branches épaisseur des branches et angle entre les branches
def draw_branches(branch_len, pen_size, angle):
    if branch_len > 0 and pen_len > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branches(branch_len - 10, pen_size - 1, angle - 5)
        left(angle*2)
        draw_branches(branch_len - 10, pen_size - 1, angle - 5)
        right(angle)
        backward(branch_len)

def draw_tree():
    setheading(90)
    color("green")
    draw_branches(70, 7, 35)
    done()

#Un programme principal saisit une chaîne d'ADN valide et une séquence d'ADN valide
# (valide signifie qu'elles ne sont pas vides et sont formées exclusivement d'une combinaison
# arbitraire de "a", "t", "g" ou "c").


# Première étape : si fonction valide --> VRAI
def valide(saisie):
    """
    if len(saisie) != 0:
        return set(saisie).issubset("atgc")

    return False
    """
    return bool(re.match("^[atcg]+$, saisie"))


#deuxième étape : Écrire une fonction saisie qui effectue une saisie valide et renvoie
#la valeur saisie

def saisie(type):
    value = input(f"Entrez une {type} d'ADN valide: ")
    if valide(value):
        return value
    else:
        print(f"La {type} n'est pas valide")
        return saisie(type)

#Écrire une fonction proportion qui reçoit deux arguments,
# la chaîne et la séquence et qui retourne la proportion de
# séquence dans la chaîne. --> on utilise fonction frequence déja fait dans chap.6

def proportion(chaine, sequence):
    proportion_of_sequence_in_chain = chaine.count(sequence)/len(chaine)
    return proportion_of_sequence_in_chain

def check_dna():
    chaine = saisie("chaine")
    sequence = saisie("sequence")
    prop = proportion(chaine, sequence)
    print("Il y a {0:.2f} % de {1}.".format(prop * 100, sequence))


#ex. il y a 10.53 % de "ca"



#Écrire un programme qui trie les lettres à partir du dictionnaire et qui retourne
# la lettre avec la fréquence la plus haute, en utilisant une fonction lambda.
#JE COMPRENDS PAS CELUI LÀ
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    draw_tree()
    print(compute_volume_and_mass())
    print((lambda sentence: sorted(frequence(sentence), key=frequence(sentence).__getitem__)[-1])("big big test bb"))
    check_dna()
