# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 08:51:21 2019

@author: dupouyj
"""


from bus import Bus
from arret import Arret
from arc import Arc
import math



class Reseau:
    def __init__(self, bus=[], arrets=[], arcs=[], arcs_ponderes=[]):
        self.bus=bus
        self.arrets=arrets
        self.arcs=arcs    # liste qui contient des objets Arc



    def getArrets(self):
        return self.arrets

    
    
    def setBus(self, bus):  #bus= obj bus
        self.bus.append(bus)
        self.setArrets(bus)
        self.setArcs(bus)

    
    
    def setArrets(self, bus):
        liste_arrets=bus.arrets_aller+bus.arrets_retour
        for a in liste_arrets:
            if self.is_not_inbis(a,self.getArrets())==1:
                self.arrets.append(a)
 
       
    def setArcs(self, bus):        
        liste_arrets=bus.arrets_aller+bus.arrets_retour
        for i in range(len(liste_arrets)-1):
            unArc=Arc(liste_arrets[i], liste_arrets[i+1])
            
            if self.is_not_in(unArc,self.arcs)==1:
                self.arcs.append(unArc)

    def setTempsArcs(self, date):
        for i in range(len(date)-1):
            a=1
            while date[i][a] == "-" or date[i+1][a] == "-" :
                a=a+1
            temps = (int(date[i+1][a][0])*60+int(date[i+1][a][2:])) - (int(date[i][a][0])*60+int(date[i][a][2:]))
            
            for a in self.arcs:
                if a.arret_dep.nom == date[i][0] and a.arret_arr.nom == date[i+1][0]:
                    a.setTemps(temps)

    
    def is_not_in(self,elem, liste):   #retourne 1 si l'element n'est pas dans la liste et 0 sinon
        if len(liste)==0:
            return 1
        if len(liste)==1:
            if liste[0]==elem:
                return 0
            return 1
        
        if elem==liste[0]:
            return 0
        
        return 1* self.is_not_in(elem,liste[1:])
    
    
    def is_not_inbis(self,ar,listeArrets):  #retourne 1 si l'element n'est pas dans la liste et 0 sinon
        for arret in listeArrets:
            if arret.nom == ar.nom:
                return 0
        return 1 
   
    
    def shortest(self,dep,arr,chemins_possibles):
        if len(chemins_possibles) != 0:
            for ch in chemins_possibles:
                if ch[-1] == arr:
                    return ch
        
        if len(chemins_possibles) == 0:
            chemins_possibles.append([dep])
            
        new_chemins_possibles=[]
        for ch in chemins_possibles:
            new_dep = ch[-1]
            for a in self.arcs:
                if a.arret_dep.nom == new_dep:
                    new_chemins_possibles.append(ch+[a.arret_arr.nom])
                    
        return self.shortest(dep,arr,new_chemins_possibles)
    
    
    
    def fastest(self,dep,arr):
        temps = self.dijkstra(dep,arr)
        chemin = [arr]
        tChemin = 0
        courant = None
        
        for t in temps:
            if t[0] == arr:
                tChemin = t[1]
                courant = t[2]
                
        new_courant = None
        while courant != dep:
            for t in temps:
                if t[0] == courant:
                    chemin = [courant]+chemin
                    new_courant = t[2]
            courant = new_courant
        
        return [dep]+chemin,tChemin
                    
            
            
    
    
    def dijkstra(self,dep,arr):
        nav = self.remove(self.getArrets(),dep)
        temps = self.makeListTemps(dep)
        courant = dep
        
        while courant != arr:
            temps = self.majTemps(temps, courant)
            courant = self.getNewCourant(nav, temps) #noeud qui est encore dans la liste des noeuds a visiter et dont le temps dans la liste des temps est le plus petit
            nav = self.remove(nav, courant)
        
        return temps



    def remove(self, liste, arret):
        for i in range(len(liste)):
            if liste[i].nom == arret:
                return liste[:i]+ liste[i+1:]
        return liste
            
    
    
    def makeListTemps(self,dep):
        temps = [[dep,0,dep]]
        
        for i in range(len(self.getArrets())):
            arret_courant = self.getArrets()[i].nom
            
            if self.sont_voisins(dep, arret_courant)[0]:
                t = self.sont_voisins(dep, arret_courant)[1]
                temps.append([arret_courant,t,dep])
            
            else:
                temps.append([arret_courant, math.inf, None])
        
        return temps
    
                
    def sont_voisins(self,n1,n2):
        for a in self.arcs:
            if a.arret_dep.nom==n1 and a.arret_arr.nom==n2:
                return True,a.temps
            if a.arret_dep.nom==n2 and a.arret_arr.nom==n1:
                return True,a.temps

        return False,0
    
    
    def majTemps(self,listeTemps, noeud):
        liste = []
        for time in listeTemps:
            if time[2] == None:
                if self.sont_voisins(time[0], noeud)[0]:
                    a=[time[0],0,0]
                    
                    for t in listeTemps:
                        if t[0]==noeud:
                            t1 = t[1]
                    t2 = self.sont_voisins(time[0], noeud)[1]
                            
                    a[2] = noeud
                    a[1] = t1 + t2 
                    liste.append(a)
                    
                else:
                    liste.append(time)
            else:
                liste.append(time)
                
        return liste
    
    
    def getNewCourant(self, listeNoeuds, listeTemps):
        min = math.inf
        noeud = 'oo'
        for a in listeNoeuds:
            for temps in listeTemps:
                if temps[0] == a.nom and temps[1]<min:
                    min = temps[1]
                    noeud = a.nom
        return noeud
                
            

        


if __name__ == "__main__" :

    res=Reseau()
    
    

      
        