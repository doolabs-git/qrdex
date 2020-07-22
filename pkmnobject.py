# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:13:59 2020

@author: dohyu
"""
import csv
import json
import requests
import urllib
import PIL

# Promt user for Pokemon to search for
pokename = input("What pokemon you want to know about?: ")

# Obtain the information URL for the pokemon based on the CSV file
def get_url(pokemon):
    
    with open('allfile.csv',newline='') as pokefile:
        reader = csv.reader(pokefile)
        for row in reader:
            if row[0] == pokemon:
                return row[1]
            else: continue
  

# Obtain basic data to store
def get_data(pokemon):
    
    # Create an empy dictionary to store the data      
    data_dict = {}

    
    # From URL convert to json format text
    data = requests.get(get_url(pokemon), params=None)
    data_load = json.loads(data.text)
    
    data_dict['name'] = pokemon
    
    # Append pokemon's type
    data_dict['type'] = []
    data_dict['type'].append(data_load['types'][0]['type']['name'])
    
    # If pokemon has two types, store both
    try:
       data_dict['type'].append(data_load['types'][1]['type']['name'])
    except:
        pass
    
    # Sums all the base stat for the 6 stats
    data_dict['base_stat'] = 0
    for item in data_load['stats']:
        data_dict['base_stat'] += item["base_stat"]
    
    # Create sprite key with value URL
    data_dict['sprite'] = data_load['sprites']['front_default']
    print(data_dict)
    return data_dict

def print_sprite(pokemon):
    dic = get_data(pokemon)
    url = dic['sprite']
    urllib.request.urlretrieve(url, "pokemon.png")
    img = PIL.Image.open("pokemon.png")
    img.show()
    
    

# Execute functions
get_url(pokename)
get_data(pokename)
print_sprite(pokename)



newdic = {}


#%%
import os
print(os.listdir('.'))





    
                
                
