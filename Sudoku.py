from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import random
from random import sample
from ortools.sat.python import cp_model

def Sudoku():
     
    #affichage des sudokus
    def Affichage(Morpion):
        for i in range(len(Morpion)):
            for j in range(len(Morpion[i])):
                print(Morpion[i][j], '|',end=' ')  
            print()
        return Morpion
   
    #creation sudoku
    tab=[]
    for i in range(9):
        tab2 =['-']
        for j in range(8):
            tab2.append('-')
        tab.append(tab2)
    #Affichage(tab)
     
    #creation model
    model = cp_model.CpModel()
   
    #creation des variables
    for i in range(9):
        for j in range(9):
            tab[i][j] = model.NewIntVar(1,9,'x')
    tab[0][0] = random.randint(1,9)
    tab[3][2] = random.randint(1,9)
    tab[4][7] = random.randint(1,9)
    tab[6][7] = random.randint(1,9)


    #Affichage(tab)

    #creation des contraintes en ligne
    tabContraintes=[1,2,3,4,5,6,7,8,9]
    for i in range(9):
        for j in range(9):
            tabContraintes[j] = tab[i][j]
        model.AddAllDifferent(tabContraintes)


    #creation des contraintes en colonne
    tabContraintes=[1,2,3,4,5,6,7,8,9]
    for i in range(9):
        for j in range(9):
            tabContraintes[j] = tab[j][i]
        model.AddAllDifferent(tabContraintes)
       
    #creation des contraintes de blocs
    tabContraintes=[1,2,3,4,5,6,7,8,9]
    for g in range(0,7,3):
        for k in range(0,7,3):
            l=0
            for i in range(g,g+3):
                for j in range(k,k+3):
                    tabContraintes[l] = tab[i][j]
                    l=l+1
            model.AddAllDifferent(tabContraintes)
            
    #demande du niveau 
    niveau=input('Quel niveau souhaitez-vous ? \nA - tres difficile - 17 cases sont données\nB - difficile - 26 cases sont données\nC - moyen - 33 cases sont données\nD - facile - 40 cases sont données \nE - débutant - 50 cases sont données')
    if(niveau=='A') :
        score = 17
    if(niveau=='B') :
        score = 26  
    if(niveau=='C') :
        score = 33
    if(niveau=='D') :
        score = 40
    if(niveau=='E') :
        score = 50      
    l=0
    #enlève le nombre de cases 
    while(l<(81-score)):
        i=random.choice(range(9))
        j=random.choice(range(9))
        if(tab[i][j]!=0):
            tab[i][j]=0
            l=l+1
                
    #creation des solvers et resolution du model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
   
    if status == cp_model.FEASIBLE:    
        #Affichage(tab)
        for i in range(9):
            for j in range(9):
                print ('%i' % solver.Value(tab[i][j]), '|',end=' ')
            print()
    elif status == cp_model.INFEASIBLE:
        print ('infeasible')
 
Sudoku()
