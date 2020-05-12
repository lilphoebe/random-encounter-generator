#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 15:46:13 2020

@author: phoebethatcher
"""


# A *truly* random random encounter generator for DnD 5e.


import csv
import random

#gets information from user about parameters of encounters
def players_define():
    # player_number = input("How many players are in your party? > ")
    player_number = None
    while player_number == None:
        input_player_number = input("How many players are in your party? > ")
        new_player_number = floatify(input_player_number)
        if new_player_number == None:
            print("Please enter a valid number.")
        else:
            player_number = new_player_number        
    player_level = None
    while player_level == None:
        input_player_level = input("What is the average level of your players? > ")
        new_player_level = floatify(input_player_level)
        if new_player_level == None:
            print("Please enter a valid number.")
        else:
            player_level = new_player_level
    print(f"Here are potential encounters for {player_number} players of average level {player_level}." + "\r\n")
    create_encounter(player_number, player_level)
    
#turns inputs into floats
def floatify(str):
    try:
        done = float(str)
    except ValueError:
        return None
    return done   
    
    
#loads the csv of monsters, and trims it for use.
def load_monsters():
    monsterFile = open('monster_list.csv', 'r', newline='')
    monsterReader = csv.reader(monsterFile)
    monsterData1 = list(monsterReader)
    monsterData = monsterData1[1:]
    return(monsterData)

    
#brings monster list, party info together, 
#loops through monsters to find an initial list of qualifying monsters
#prints and tidies the encounters once they're created. 
def create_encounter(player_number, player_level):
    monsterData = load_monsters()
    party_capacity = calculate_cap(player_number, player_level)
    available_monsters = []
    for row in monsterData[:-2]:
         cr = float(row[1])
         if cr <= party_capacity:
             available_monsters.append(row)
    first_encounter = make_possibilities(party_capacity, available_monsters)
    tidy_print(first_encounter)
    second_encounter = make_possibilities(party_capacity, available_monsters)
    tidy_print(second_encounter)
    third_encounter = make_possibilities(party_capacity, available_monsters)
    tidy_print(third_encounter)
    fourth_encounter = make_possibilities(party_capacity, available_monsters)
    tidy_print(fourth_encounter)
    fifth_encounter = make_possibilities(party_capacity, available_monsters)
    tidy_print(fifth_encounter) 
    
#randomly selects from available monsters and puts them in a list
def make_possibilities(party_capacity, available_monsters):
    an_encounter = []
    current_capacity = 0
    ran = 0
    while current_capacity < party_capacity:
        eval_monsters = evaluated_monsters(current_capacity, party_capacity, available_monsters)
        ran = random.randint(0, ((len(eval_monsters)-1)))
        an_encounter.append(eval_monsters[ran])
        current_capacity = calculate_encounter(an_encounter)
    return(an_encounter)
    
#calculates the party's challenge capacity
def calculate_cap(player_number, player_level):
    if player_number > 4:
        return ((player_level + ((player_number-4)/2)))
    else:
        return ((player_level + player_number) -4)
    
#calculates the remaining challenge capacity each time a monster is added to the encounter
def calculate_encounter(an_encounter):
    each_cr = []
    summable_variable = 0
    for row in an_encounter:
        summable_variable = float(row[1])
        each_cr.append(summable_variable)
    finished_sum = sum(each_cr)
    return finished_sum
 
#re-evaluates the list of available monsters every time a monster is added to the encounter        
def evaluated_monsters(current_capacity,party_capacity,available_monsters):
    evaluated_list = []
    for row in available_monsters:
        cr = float(row[1])
        if cr <= (party_capacity - current_capacity):
            evaluated_list.append(row)
    return evaluated_list

#tidies up string to present encounter to user    
def tidy_print(list):
    encounter_names_list = []
    for row in list:
        monster_name = row[0]
        encounter_names_list.append(monster_name)
    untidy_characters = ["'", "]", "[","\""]   
    tidy_names = str(encounter_names_list)
    for char in untidy_characters:
        tidy_names = tidy_names.replace(char, "")  
    printing = "Your party fights: {enc}".format(enc = str(tidy_names))
    with_spacing = printing + "\r\n"
    print(with_spacing)
    
    
players_define()