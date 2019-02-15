# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 08:55:14 2019

@author: dupouyj
"""

from lecture import Lecture
from reseau import Reseau
from bus import Bus
from arret import Arret





if __name__ == "__main__" :
    
#    num_bus = eval(input("n° du bus : "))
#    arret_dep = eval(input("nom de l'arret de depart : "))
#    arret_arr = eval(input("nom de l'arret d'arrivee : "))
    

    
    
    fichier2 = open("2_Piscine-Patinoire_Campus.txt", "r")
    contenu2 = fichier2.read()
    lect2 = Lecture(contenu2)
    
    res=Reseau() #creation de l'objet reseau
    bus2=Bus(2)  #creation d'un objet bus2
    
    #ajout des arrets dans la ligne de bus
    bus2.addArretsAller(lect2.regular_date_go())
    bus2.addArretsRetour(lect2.regular_date_back())
    
    res.setBus(bus2)  #ajout du bus au réseau

    
    #donne des temps a chaque arc du reseau
    res.setTempsArcs(lect2.regular_date_go())
    res.setTempsArcs(lect2.regular_date_back())
    print("temps", res.arcs[-1].temps,"min")


    print("\n\nchemin le plus court : ", res.shortest('GARE_QUAI_EST', 'Arcadium',[]))
    print("\n\nchemin le plus rapide : ",res.fastest('GARE_QUAI_EST', 'Arcadium')[0],"\ntemps nécessaire : ",res.fastest('GARE_QUAI_EST', 'Arcadium')[1],"min\n")

    fichier2.close()