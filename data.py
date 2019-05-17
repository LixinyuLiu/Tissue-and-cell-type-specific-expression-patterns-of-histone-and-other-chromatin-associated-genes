# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:27:46 2019

@author: llxy
"""

import pandas as pd

BioGrid = pd.read_excel('BioGrid.xlsx')
EMandhistone = pd.read_excel('Book2.xlsx')

Summary = []
for gene in EMandhistone['Genes']:
    for gene1 in BioGrid['Official Symbol Interactor A']:
        if gene1 == gene:
            Summary.append(gene)


#Writer = pd.ExcelWriter()
Summary = list(dict.fromkeys(Summary))
## len(Summary) 201 genes in common for both epeigenetics modulator and hostone genes

##for gene in Summary:
##    print(BioGrid[BioGrid['Official Symbol Interactor A'] == gene])

A = list(BioGrid['Official Symbol Interactor A'])    
nl = []
for index in range(len(Summary)):
    if Summary[index] in A:
        nl.append(A.index(Summary[index]))

B2 = BioGrid.loc[nl,:]
B2.to_csv('Biogridderived.csv')
