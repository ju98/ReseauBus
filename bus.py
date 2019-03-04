# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 08:26:59 2019

@author: dupouyj
"""


from arret import Arret

class Bus:
    def __init__(self, ligne, arrets_aller=[], arrets_retour=[]):  #arrets a rentrer dans l'ordre
        self.ligne=ligne
        self.arrets_aller=arrets_aller
        self.arrets_retour=arrets_retour
    
    
    def setArretAller(self,arret):
        self.arrets_aller.append(arret)
    
    def setArretRetour(self,arret):
        self.arrets_retour.append(arret)
    
    
    def addArretsAller(self,dates):
        '''
           Ajoute les arrets aller à l'aide de l'horaire du bus 
        '''
        for i in range(len(dates)):
            arret = Arret(dates[i][0])
            self.setArretAller(arret)

    
    def addArretsRetour(self,dates):
        '''
           Ajoute les arrets aller à l'aide de l'horaire du bus 
        '''
        for i in range(len(dates)):
            arret = Arret(dates[i][0])
            self.setArretRetour(arret)

    
    
    
    
    def sens(self, depart, arrivee):
        for i in range(len(self.arrets_aller)):
            if self.arrets_aller[i]==depart:  #le depart apparait en premier, donc on retourne true qui correspond au sens aller
                return True
            if self.arrets_aller[i]==arrivee:  #l'arrivee arrive en premier, donc on retourne false qui correspond au sens retour
                return False
    