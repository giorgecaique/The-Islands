# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 20:34:07 2018

@author: giorge.luiz
"""

import matplotlib, math, pandas as pd

# first line: 3 integers n (4 <= n <= 100), b1, and b2 (0 < b1, b2 < n-1 and b1 <> b2)

inpt = """5 1 3 
1 3
3 4
4 1
7 5
8 3
5 3 2
0 10
3 14
4 7
7 10
8 12
0 0 0""".split('\n')

islands = []

island_path = []

class island(object):
    island_id = 0
    x = 0
    y = 0
    case = 0
    special_island = False
    
    def __init__(self, island_id = None, x = None, y = None, case = None, special_island = False):
        self.island_id = island_id
        self.x = x
        self.y = y
        self.case = case
        self.special_island = special_island
        

def euclidian_distance(x1, x2, y1, y2):
    result = math.sqrt(math.pow((x1 - x2),2) +  math.pow((y1 - y2),2))
    return result

def greedy_choice_property(current_island):
    global islands
    selected_island = None
    selected_distance = 99999999999
    for island in islands:
        if selected_island != None:
            if len(island_path) == 5:
                selected_island = island_path[0]
            elif not current_island.special_island and euclidian_distance(current_island.x, island.x, current_island.y, island.y) < selected_distance and island.special_island:
                selected_island = island
                selected_distance = euclidian_distance(current_island.x, island.x, current_island.y, island.y)
                
            elif current_island.special_island and euclidian_distance(current_island.x, island.x, current_island.y, island.y) < selected_distance and not island.special_island:
                selected_island = island
                selected_distance = euclidian_distance(current_island.x, island.x, current_island.y, island.y)
        else:
            selected_island = island
            selected_distance = euclidian_distance(current_island.x, island.x, current_island.y, island.y)
    
    return selected_island

def load_islands():
    case = 0
    island_id = 0
    global islands
    b1 = -1
    b2 = -1
    for item in inpt:
        split_item = item.strip().split(' ')
        if len(split_item) == 3 and split_item[0] == '0': # end of input
            break
        
        if len(split_item) == 3: # header
            b1 = int(split_item[1])
            b2 = int(split_item[2])
            case+=1
            island_id = 0
            print(split_item, b1, b2)
            continue
        
        
        islnd = island(island_id, int(split_item[0]), int(split_item[1]), case, island_id == b1 or island_id == b2)
        
        island_id+=1
        
        
        islands.append(islnd)

def get_dataframe(l):
    pre_df = []
    for island in l:
        pre_df.append({
                    'island_id' : island.island_id,
                    'x' : island.x,
                    'y' : island.y,
                    'case' : island.case,
                    'special_island' : island.special_island
                })
    return pd.DataFrame(pre_df)

def greedy_algorithm():
    global islands, island_path
    case = 1
    for island in islands:
        if island.case == case:
            if island.island_id == 0:
                island_path.append(island)
            elif island.island_id == 1:
                island_path.append(island)
                island_path.append(greedy_choice_property(island))
            elif island not in island_path:
                island_path.append(greedy_choice_property(island_path[-1]))
        print('Case', case, )
        case +=1
        

def main():
    load_islands()
    greedy_algorithm()
    df = get_dataframe(islands)
    df2 = get_dataframe(island_path)
    print(df)
    print(df2)

main()
    
    

                
        
    

    