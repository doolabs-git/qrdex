# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 08:11:59 2020

@author: dohyu
"""

from pkmnobject import get_data
import csv

namelist = []
with open('allfile.csv',newline='') as pokefile:
            reader = csv.reader(pokefile)
            for row in reader:
                if row[0] != 'Name':
                    namelist.append(row[0])
                else:
                    continue
                
with open('pokedata.csv', 'w', newline="") as newfile:
    writer = csv.writer(newfile)
    writer.writerow(['Name', "Types", 'Base Stat', 'Sprite Link'])           
    for name in namelist:
        dic = get_data(name)
        writer.writerow(dic.values())
                

    
            
            
             
            
                