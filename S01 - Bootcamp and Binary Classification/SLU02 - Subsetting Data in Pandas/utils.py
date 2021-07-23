import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm


MAP_COLOURS = [
    ["k", "w", "w", "k", "k", "k", "k", "w", "k", "k"],
    ["w", "w", "w", "k", "k", "w", "w", "w", "w", "k"],
    ["w", "w", "w", "k", "w", "w", "w", "w", "w", "k"],
    ["w", "w", "w", "w", "w", "w", "w", "w", "w", "w"],
    ["c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
    ["w", "k", "w", "w", "w", "w", "w", "w", "w", "w"],
    ["w", "k", "w", "w", "w", "w", "w", "k", "w", "k"],
    ["w", "k", "w", "w", "w", "k", "w", "k", "w", "k"],
    ["w", "k", "w", "w", "k", "k", "k", "k", "w", "k"]
]

CLUE_START_IDX = [1, 0, 0, 3, 2, 1, 1, 0, 1, 3]
CLUE_END_IDX = [9, 5, 9, 9, 8, 7, 8, 6, 9, 6]


def duration_to_int(duration: str) -> int:
    """ 
    Computes integer duration of string if format corresponds to X min

    Args:
        duration (str): the input duration string
    Returns:
        int: number of corresponding minutes
    """

    match = re.match(r"(\d+ ?)(?=min)", duration)
    if match:
        return int(match.group())
    else:
        return np.nan 
    
    
def add_column_duration_int(df: pd.DataFrame) -> pd.DataFrame:
    """ 
    Add a new column `duration_int` containing the duration as an integer
     to a dataframe with a previous column `duration`

    Args:
        df (pd.DataFrame): the input DataFrame
    Returns:
        df_new (pd.DataFrame): new dataframe with added `duration_int` column
    """

    # You will learn more about `apply` on later units
    df_new = df.copy()
    df_new["duration_int"] = df_new["duration"].apply(duration_to_int)
    return df_new


def draw_crosswords(text, colours):
    plt.figure()

    ny=10
    nx=10

    tb = plt.table(cellText=text, cellColours=colours, loc=(0,0), cellLoc='center')
    tc = tb.properties()['children']
    for cell in tc: 
        cell.set_height(1/ny)
        cell.set_width(1/nx)

    ax = plt.gca()
    ax.set_xticks([]);
    ax.set_yticks([]);

    plt.show() 

    

def draw_base_puzzle():
    n_cols = range(len(MAP_COLOURS[0]))
    n_rows = range(len(MAP_COLOURS))
    
    text = [["" for i in n_cols] for j in n_rows]
    draw_crosswords(text, MAP_COLOURS)

    
def draw_final_puzzle(clues):
    
    n_cols = range(len(MAP_COLOURS[0]))
    n_rows = range(len(MAP_COLOURS))
    
    text = [["" for i in n_cols] for j in n_rows]
    for col in n_cols:
        start_idx = CLUE_START_IDX[col]
        end_idx = CLUE_END_IDX[col]
        clue = clues[col]
        
        idx = 0
        for letter in clue:
            text[start_idx + idx][col] = clue[idx].upper()
            idx += 1 
            if start_idx + idx >= end_idx:
                break
        
    draw_crosswords(text, MAP_COLOURS)
