# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 09:52:26 2019

@author: dupouyj
"""




class Lecture:
    def __init__(self,contenu):
        self.contenu = contenu
    
    
    def separationDates(self, dates):
        # separe les differentes lignes d'horaires
        # retourne une liste de string de la forme : [['Arret', 'heure1', '...'],['Arret', 'heure1','...']]
        T = []
        splitted_dates = dates.split("\n")
        for stop_dates in splitted_dates:
            tmp = stop_dates.split(" ")
            T.append(tmp)
        return T
    

    
    def slited_content(self):
        #contenu du fichier sous forme d'une liste de string (qui on ete separes losqu'il y a 2 retours a la ligne \n)
        return self.contenu.split("\n\n")
    
    
    def regular_path(self):
        return self.slited_content()[0]
    
    def regular_stop(self):
        #liste des arrets reguliers
        return self.slited_content()[0].split(" N ")
    
    def regular_date_go(self):
        return self.separationDates(self.slited_content()[1])
    
    def regular_date_back(self):
        return self.separationDates(self.slited_content()[2])
    
    
    def we_holidays_path(self):
        return self.slited_content()[3]
    
    def we_holidays_date_go(self):
        return self.separationDates(self.slited_content()[4])
    
    def we_holidays_date_back(self):
        return self.separationDates(self.slited_content()[5])




if __name__ == "__main__" :
    fichier2 = open("2_Piscine-Patinoire_Campus.txt", "r")
    contenu2 = fichier2.read()
    lect2 = Lecture(contenu2)
    
    #print(lect2.slited_content())


    fichier2.close()