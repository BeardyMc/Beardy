import streamlit as st
import math
import numpy as np

st.title("🎈 Beardy Does Maths")
st.write(
    "Built using streamlit: [docs.streamlit.io](https://docs.streamlit.io/) \n\nWeapon:\n"
)
era = st.selectbox(
    "Age:",
    [   "Primitive",
        "Medieval",
        "Early-Modern",
        "Modern",
        "Space",
        "Interstellar",
        "Multiverse",
        "Quantum",
        "Underworld",
        "Divine",
    ],
) 

if era == "Primitive":
    items = ["Blowgun", "Rock", "Slinger"] 
elif era =="Medieval":
    items = ["Bow", "Tomahawk"] 
elif era == "Early-Modern":
    items = ["Crossbow", "Dual Pistols", "Musket"]
elif era == "Modern":
    items = ["AK", "M4", "Sniper", "Uzi"]
elif era == "Space":
    items = ["Blaster", "Space Gun", "Space Pistol"] 
elif era == "Interstellar":
    items = ["Ionic Blaster", "Plasma Rifle", "Ray Gun"]
elif era == "Multiverse":
    items = ["Virtual Gun", "Virtual Bow"] 
elif era == "Quantum":
    items = ["Black Bow", "Black Gun", "Black Staff"] 
elif era == "Underworld":
    items = ["Abyssal Fork", "Abyssal Trident"] 
elif era == "Divine":
    items = ["Staff", "Staff of Wisdom"]
else:
    items = ["Please select an age"] 

selected_item = st.selectbox(f"Weapon:", items)

skin_q = st.selectbox(
    "Skin:",
    [
        "None",
        "Anubis",
        "Boxer",
        "Bunny",
        "Cat",
        "Chef",
        "Clown",
        "Cubeguy",
        "Dark Planet Warrior",
        "Demon",
        "Druid",
        "Eagle",
        "Fishbowl",
        "Flower",
        "King",
        "Knight",
        "Lavaman",
        "Leprechaun",
        "Millionaire",
        "Mummy",
        "Mushroom",
        "Reaper",
        "Shark",
        "Skater",
        "Skeleton",
    ],
)

weapon_windups = {
    # Primitive
    "Blowgun": 0.467,
    "Rock": 0.683,
    "Slinger": 1.083,
    # Medieval
    "Bow": 1.083,
    "Tomahawk": 0.683,
    # Early-Modern
    "Crossbow": 0.567,
    "Dual Pistols": 0.833,
    "Musket": 0.667,
    # Modern
    "AK": 0.5,
    "M4": 0.5,
    "Sniper": 0.833,
    "Uzi": 0.333,
    # Space
    "Blaster": 0.667,
    "Space Gun": 0.717,
    "Space Pistol": 0.917,
    # Interstellar
    "Ionic Blaster": 0.667,
    "Plasma Rifle": 0.833,
    "Ray Gun": 0.967,
    # Multiverse
    "Virtual Gun": 0.833,
    "Virtual Bow": 1.083,
    # Quantum
    "Black Bow": 0.833,
    "Black Gun": 1.0,
    "Black Staff": 0.95,
    # Underworld
    "Abyssal Fork": 0.817,
    "Abyssal Trident": 1.0,
    # Divine
    "Staff": 0.833,
    "Staff of Wisdom": 0.717,
}
 
item_windup = weapon_windups.get(selected_item, 1.0)

# Show on screen
st.write(f"Item Windup for {selected_item}: **{item_windup}s**")

# 1. Dictionary for all skin modifiers
skin_modifiers = {
    "Anubis": 0.667,
    "Boxer": 0.917,
    "Bunny": 0.933,
    "Cat": 0.2,
    "Chef": 0.767,
    "Clown": 0.767,
    "Cubeguy": 0.667,
    "Dark Planet Warrior": 0.9,
    "Demon": 0.9,
    "Druid": 0.95,
    "Eagle": 0.9,
    "Fishbowl": 0.933,
    "Flower": 1.0,
    "King": 0.717,
    "Knight": 0.717,
    "Lavaman": 0.967,
    "Leprechaun": 0.317,
    "Millionaire": 0.667,
    "Mummy": 0.667,
    "Mushroom": 0.733,
    "Reaper": 0.567,
    "Shark": 0.9,
    "Skater": 0.733,
    "Skeleton": 0.783,
}

if skin_q != "None":
  skin_windup = skin_modifiers.get(skin_q, 1.0)
  st.write(f"Active Skin: **{skin_q}** (Windup: {skin_windup})")

Clicked = st.button("Let's go!")

def calculate_breakpoints(Windup):
    #fun comes here
    breakpoints=[[0,0,0]] #initialise
    BaseD=1.5 #standard time for all weapons
    
    inc=0.09999999976 #fd6
    n_tics = math.ceil(Windup / inc)
    first_hit = inc * n_tics
    cooldown_tics = max(1, math.ceil((BaseD - first_hit) / inc))
    total_t = (n_tics + cooldown_tics + 1) * 0.1
    
    breakpoints[0][1] = round(total_t,1) #first row, second val
    
    d_reset = Windup * 0.75
    gap = max(1, math.ceil((Windup - d_reset) / inc))
    t2 = d_reset + gap * inc
    d_cool = max(1, math.ceil((BaseD - t2) / inc))
    n_tics = math.ceil(Windup / inc)
    d_total = gap + d_cool + 1 + n_tics

    breakpoints[0][2] = round(d_total * 0.1,1)#first row, third val
    
    for i in range(1,48001):
        AS=i*0.01

        spd_multi = 1 + AS / 100
        inc = spd_multi * 0.09999999976
        n_tics = math.ceil(Windup / inc)
        first_hit = inc * n_tics
        cooldown_tics = max(1, math.ceil((BaseD - first_hit) / inc))
        total_t = round((n_tics + cooldown_tics + 1) * 0.1,1)

        gap = max(1, math.ceil((Windup - d_reset) / inc))
        t2 = d_reset + gap * inc
        d_cool = max(1, math.ceil((BaseD - t2) / inc))
        n_tics = math.ceil(Windup / inc)  # re-evaluated
        d_total = round((gap + d_cool + 1 + n_tics) * 0.1,1)

        if total_t < breakpoints[-1][1] or d_total < breakpoints[-1][2]:
            breakpoints.append([round(AS,2), total_t, d_total])
    
    return breakpoints
    

def manual_lookup(x_val, dataset):
    # search function
    active_row = dataset[0]  # default to first row
    for row in dataset:
        if row[0] <= x_val:
            active_row = row
        else:
            break  # Stop once we pass x_val
    return active_row[1], active_row[2]  # Returns (val1, val2)

def combine_breakpoints(IB,SB):
    # get all AS breakpoints
    all_AS = set()
    for row in IB:
        all_AS.add(row[0])
    for row in SB:
        all_AS.add(row[0])    
    all_AS = sorted(list(all_AS))
    print(all_AS)
    
    # inigltialise combined
    CB=[]
    choice=[]
    single_speed=2
    double_speed=2
    
    for AS in all_AS:
        item_single, item_double = manual_lookup(AS,IB)
        skin_single, skin_double = manual_lookup(AS,SB)
        
        print("item")
        print([AS,item_single,item_double])
        print("skin")
        print([AS,skin_single,skin_double])
        print("current")
        print([single_speed, double_speed])
        if item_single<single_speed or item_double<double_speed or skin_double<double_speed:
            if item_double < skin_double:
                CB.append([AS, item_single, item_double])
                choice.append("Item")
                double_speed=item_double
            elif item_double > skin_double:
                CB.append([AS, skin_single, skin_double])
                choice.append("Skin")
                double_speed=skin_double
            else:
                CB.append([AS,item_single,item_double])
                choice.append("equal")
                double_speed=item_double
            single_speed=item_single
        
    return CB, choice
            
                




if Clicked:
    item_breakpoints = calculate_breakpoints(item_windup)

    if skin_q !="None":
        skin_breakpoints = calculate_breakpoints(skin_windup)
        final_breakpoints, wearing = combine_breakpoints(item_breakpoints,skin_breakpoints)
    else:
        final_breakpoints = item_breakpoints


    st.write("Calculated Breakpoints") 
    


