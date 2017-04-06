# -*- coding: utf-8 -*-
"""   Ce programme se charge de se positionner là où vous mettez votre musique. Pensez à bien changer le chemin pour que ça tourne sur votre machine. Pour ma part je place ma musique dans une partition et je classe les chansons par artistes et albums.
    Pas de module à installer
    OS : Kubuntu 16.04 
    
    AMELIORATION : 
        - Gener un csv pour contenir les informations sur les chansons. 
        - Creer un classifieur pour choisir le prochain morceau selon le style (exemple : si on ecoute un morceau de jazz, on a envie que le morceau suivant soit dans le même genre de musique.
        
        

Pour le fun ! 
"""

import os 
import subprocess 
import random as rdm 

#------------------------------------------------------------------------
PLAYER         = ("clementine","vlc")
PATH_CENTRAL   = "/media/skndr-ros/DATA/music"
MODE           = ("On","Off","StandBy")
FORMAT         = (".mp3",".flac",".wma",".mp4")
SHELL_COM_HOME = ' find $directory -type f -name "*FORMAT[0]" '    #trouve tous les mp3 sur la partition
#------------------------------------------------------------------------

class Song : 
    def __init__(self,extension) : 
        self.extension = extension
        self.name      = name
        self.album     = album
        
class Player : 
    def __init__(self) : 
        self.path = PATH_CENTRAL
        self.mode = MODE[0]
        self.format_tol = FORMAT 
        self.state = True #false si on joue sur la partition
        self.comp = 0 #incremente a chaque chanson
    
    def check_folders(self,pth_folder) : 
        try : 
            gen = next(os.walk(pth_folder))[1]
        except StopIteration : 
            return (False,[])
        if len(gen) == 0 : 
            return (False,[])  
        else : 
            return (True,gen)
    
    def nav(self,rep,gen,reper) : 
        if rep == True : 
            x = rdm.randint(1,len(gen)) 
            return reper + "/" + gen[x-1]
        else : 
            return reper
        
    def roulette_dir(self) :
        """Cette fonction se charge de faire un cd /repertoire_choisi_alea """
        ls = os.listdir(self.path)
        x = rdm.randint(1,len(ls))
        ex = os.path.splitext(ls[x-1])[1]
        while ex  == FORMAT[3] : 
           x = rdm.randint(1,len(ls))   
           ex = os.path.splitext(ls[x-1])[1]
        while len(os.listdir(self.path+"/"+ls[x-1])) < 1 and  ex  == FORMAT[3] :
           x = rdm.randint(1,len(ls))
           print("dossier vide")
        elem = ls[x-1]
        (rep,gen) = self.check_folders(self.path+"/"+elem) 
        if rep :  
            while(rep) :   #check si on a encore des dossiers
                ch = self.nav(rep,gen,elem)
                (rep,gen) = self.check_folders(ch)
                os.chdir(os.path.expanduser(self.path+"/"+ch))
                print(ch) 
        else : 
            os.chdir(self.path+"/"+ls[x-1])
        #print(os.getcwd())
        ls_songs = os.listdir(os.getcwd())
        print(ls_songs)
        i = 1
        if ls_songs == [] : 
            self.roulette_dir()
            i+=1 #debug
            print(i)  #debug
        else : 
            self.roulette_songs(ls_songs)  #recursivement..
    
    def roulette_songs(self,ls) : 
        try : 
            x = rdm.randint(0,len(ls)-1)
            extension = os.path.splitext(ls[x-1])[1]
            while extension not in self.format_tol : 
                x = rdm.randint(0,len(ls))
                extension = os.path.splitext(ls[x-1])[1]
                #print(extension)
                #print(ls)
            if os.path.splitext(ls[x-1])[1] in FORMAT : 
                print(ls[x-1])
                subprocess.call(["clementine",ls[x-1]])
            else : 
                self.roulette_songs(ls)
        except ValueError : #or IndexError :   
            print(len(g(ls)))

        
#~*--*~--*~--*~--*~--*~--*~--*~--*~--*~--*~--*~--*~--*~--*~--*~--*~--*~--*~       
def main() : 
    run = Player() 
    run.roulette_dir()

if __name__ == "__main__" :   
    main()
        
        