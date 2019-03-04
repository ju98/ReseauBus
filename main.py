# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 08:55:14 2019

@author: dupouyj
"""

from lecture import Lecture
from reseau import Reseau
from bus import Bus



if __name__ == "__main__" :
    
  
    #ouverture et lecture des fichiers contenants les horaires de bus
    fichier1 = open("1_Poisy-ParcDesGlaisins.txt","r")
    contenu1 = fichier1.read()
    lect1 = Lecture(contenu1)
    
    fichier2 = open("2_Piscine-Patinoire_Campus.txt", "r")
    contenu2 = fichier2.read()
    lect2 = Lecture(contenu2)


################ JOURS NORMAUX    
    res=Reseau() #creation de l'objet reseau
    bus1=Bus(1)  #creation d'un objet bus1
    bus2=Bus(2)  #creation d'un objet bus2

    
    #ajout des arrets dans les lignes de bus
    bus1.addArretsAller(lect1.regular_date_go())
    bus1.addArretsRetour(lect1.regular_date_back())
    
    bus2.addArretsAller(lect2.regular_date_go())
    bus2.addArretsRetour(lect2.regular_date_back())
    
    
    #ajout des bus au réseau
    res.setBus(bus1)
    res.setBus(bus2)
    

    
    #affecte un temps a chaque arc du reseau
    res.setTempsArcs(lect1.regular_date_go())
    res.setTempsArcs(lect1.regular_date_back())
    res.setTempsArcs(lect2.regular_date_go())
    res.setTempsArcs(lect2.regular_date_back())
    
    #supprime les arcs en trop (qui ne sont pas en liaison directe)
    res.arcs = res.deleteArcs()


################## JOURS FERIES
    reswe=Reseau() #creation de l'objet reseau en weekend et jours feries
    bus1we=Bus(1)
    bus2we=Bus(2)

    #ajout des arrets dans les lignes de bus les jours feries
    bus1we.addArretsAller(lect1.we_holidays_date_go())
    bus1we.addArretsRetour(lect1.we_holidays_date_back())
    
    bus2we.addArretsAller(lect2.we_holidays_date_go())
    bus2we.addArretsRetour(lect2.we_holidays_date_back())
    
    #ajout des bus au reseau
    reswe.setBus(bus1we)
    reswe.setBus(bus2we)   

#    #affecte un temps a chaque arc du reseau les jours feries
#    reswe.setTempsArcs(lect1.we_holidays_date_go())
#    reswe.setTempsArcs(lect1.we_holidays_date_back())
#    reswe.setTempsArcs(lect2.we_holidays_date_go())
#    reswe.setTempsArcs(lect2.we_holidays_date_back())
#    
#    #supprime les arcs en trop (qui ne sont pas en liaison directe)
#    reswe.arcs = reswe.deleteArcs()



    
################## interraction avec l'utilisateur
    a = eval(input("Que voulez vous faire ?\n\t1:Obtenir le chemin le plus court\n\t2:Obtenir le chemin le plus rapide\nNuméro : "))
#    b = eval(input("\nJour férié ? (oui/non) :"))
    for i in range(len(res.arrets)):
        print(i,":",res.arrets[i].nom)
    num_arret_dep = eval(input("Arret de départ ?\nNuméro : "))
    num_arret_arr = eval(input("Arret d'arrivée ?\nNuméro : "))

    for i in range(len(res.arrets)):
        if num_arret_dep == i:
            arret_dep = res.arrets[i].nom
        if num_arret_arr == i:
            arret_arr = res.arrets[i].nom
       
    if a == 1:
        print("\n\nChemin le plus court : ", res.shortest(arret_dep, arret_arr,[]))
    if a == 2:
        print("\n\nChemin le plus rapide : ",res.fastest(arret_dep, arret_arr)[0],"\ntemps nécessaire : ",res.fastest(arret_dep, arret_arr)[1],"min\n")
        
#################
    
    fichier1.close()
    fichier2.close()