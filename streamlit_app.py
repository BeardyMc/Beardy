import streamlit as st
import math
import numpy as np
import pandas as pd


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
  st.write(f"Windup for **{skin_q}** skin: {skin_windup}")

N_ls = st.slider(
    label="Select desired amount of lifesteal slots, recommended 2:", 
    min_value=0,
    max_value=12,
    value=2,
    step=1
)

fairy = st.toggle("Using damage fairy",value=True) 

fairy2 = st.radio(
    "Fairy choice",
    ["Damage", "5th hit"], 
    horizontal=True) 

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
    
    # initialise combined
    CB=[]
    choice=[]
    single_speed=2
    double_speed=2
    
    for AS in all_AS:
        item_single, item_double = manual_lookup(AS,IB)
        skin_single, skin_double = manual_lookup(AS,SB)
        
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
            
                

def best_substats(timings, N_ls):
    timings=np.array(timings)
    # function for finding optimal substat builds
    cd_max = 0.8
    cc_max = 0.12
    dc_max = 0.2
    dmg_max = 0.15
    rdmg_max = 0.15
    spd_max = 0.4

    # CC = 0.8 #setting manually due to Mira, update at each new fairy launch
    
    # initialise
    Record=[[0,0,0,0,0,0,0,0]]
    
    for i in range(70,101):
        perf=i/100
        bestest=[0,0,0,0,0,24,0]
        
        for N_cc in range(1,13):
            CC = min(1, N_cc * cc_max * perf)
        
            for N_cd in range(1, 13):
                cd = N_cd * cd_max * perf
        
                for N_dmg in range(7):  # 0 to 6 inclusive
                    dmg = N_dmg * dmg_max * perf
            
                    for N_rdmg in range(N_dmg + 1):  # 0 up to N_dmg inclusive
                        rdmg = N_rdmg * rdmg_max * perf
                
                        for N_dc in range(7):  # 0 to 6 inclusive
                            dc = min(1, dc_max * N_dc * perf)
                    
                            for N_spd in range(1, 13):
                                if (N_cc+N_spd+N_dc+N_rdmg+N_dmg+N_cd) == (24-N_ls):
                                    spd = N_spd * spd_max * perf * 100
                                    
                                    B = timings[:,0]<spd
                                    C = timings[B]
                                    time1 = C[-1, 1:3]
                                    
                                    APS = (1 - dc) / time1[0] + dc * 2 / time1[1]
                                    Crit_multi = CC * (1.2 + cd) + 0.2
                                    DPS = (dmg + 1) * (rdmg + 1) * Crit_multi * APS
    
                                    best_new = [N_cc, N_cd, N_dmg, N_rdmg, N_dc, N_spd, DPS]
    
                                    if DPS > bestest[6]:
                                        bestest = best_new
                                        best_val = [CC, cd, dmg, rdmg, dc, spd]
    
                                    elif DPS == bestest[6]:
                                        if max(best_new[0:6]) < max(bestest[0:6]):
                                            bestest = best_new
                                            best_val = [CC, cd, dmg, rdmg, dc, spd]
        print(Record)
        last_row_check = Record[-1][1:6]
        if np.any(last_row_check != bestest[0:5]):
            new_row = [perf] + bestest
            Record.append(new_row)
     
    print(Record)
    Record = np.array(Record)
    Record = Record[1:]

    Record_stats = Record.copy()
    Record_stats[:, 1:7] = Record[:, 1:7] * Record[:, 0:1]
    max_factors = np.array([cc_max, cd_max, dmg_max, rdmg_max, dc_max, spd_max])
    Record_stats[:, 1:7] = Record_stats[:, 1:7] * max_factors * 100

    return Record, Record_stats
                       
                                

    return Record, Record_stats


if Clicked:
    item_breakpoints = calculate_breakpoints(item_windup)

    if skin_q !="None":
        skin_breakpoints = calculate_breakpoints(skin_windup)
        final_breakpoints, wearing = combine_breakpoints(item_breakpoints,skin_breakpoints)
    else:
        final_breakpoints = item_breakpoints

    df = pd.DataFrame(final_breakpoints,columns=["Attack Speed", "Single Attack cycle", "Double Attack cycle"]) 

    if skin_q != "None":
        df["Applied Skin"] = wearing
    

    SubN, SubV = best_substats(final_breakpoints, N_ls)

    col_names = ['% Perf', 'Crit Chance', 'Crit Dmg', 'Damage', 'Ranged', 'Double', 'Speed']

    combined_df = pd.DataFrame()
    combined_df['% Perf'] = SubN[:, 0]

    # Loop through columns 1 to 5 to combine raw and scaled values
    for i, col_name in enumerate(col_names[1:], start=1):
        raw_vals = SubN[:, i]
        scaled_vals = SubV[:, i]
    
    # Combine them into a "Raw / Scaled" string format
    # (Using int() on raw values since tiers are whole numbers, and .1f for scaled)
        combined_df[col_name] = [
            f"{int(r)} ({s:.1f}%)" for r, s in zip(raw_vals, scaled_vals)
        ]
    
    st.divider()
    st.subheader("Results")
    st.write("These results all assume 3 slots are taken for Skill Damage, with a lvl 20 Mira giving 80% Crit Chance. \n\nThis is optimising for the highest DPS, which sometimes lowers speed for bigger hits. This has the trade-off of hampering survivability if the enemy can hit you multiple times between your lifesteal activating. \n\nHere are the number of slots that should be given to each substat if the required level of perfection is reached, plus the raw substat value:")
    st.dataframe(
        combined_df, 
        use_container_width=True, 
        height="content", 
        hide_index=True
    )

    st.write("Below we look at the PvP capabilities of these builds. \n\nNote: standard health is 8x damage, with a 5x multiplier in PvP. Pet typing and equipped items levels can change this distribution. These percentages assume health is the standard 40x base damage before modifiers.") 

    col_names = ["% Perf", "Speed", "APS", "DPS", "Lifesteal", "Regen/s", "Regen/hit"] 
    second_df = pd.DataFrame()
    second_df['% Perf'] = SubN[:, 0]

    workable_breakpoints = np.array(final_breakpoints)
    spd_str=[]
    aps=[] 
    lifesteal=[]
    regenH=[] 
    regenS=[] 

    for i in range(len(SubV)):
        spd=SubV[i,6]
        B=workable_breakpoints[:,0]<spd
        C=workable_breakpoints[B,1:3]
        
        spd_str.append(f"{spd:.0f}% ({C[-1,0]:.1f}s / {C[-1,1]:.1f}s)")
        aps.append((1-SubV[i,5]/100)/C[-1,0] + 0.02*SubV[i,5]/C[-1,1])
        lifesteal.append(SubV[i,0]*20*N_ls)
        regenH.append((lifesteal[i]*SubV[i,7]/aps[i])/40)
        regenS.append(lifesteal[i]*SubV[i,7]/40)
        
        
 
    second_df['Speed'] = spd_str
    second_df['APS'] = aps
    second_df['DPS'] = SubV[:,7]
    second_df['Lifesteal'] = lifesteal 
    second_df['Regen/s'] = regenS
    second_df['Regen/hit'] = regenH

    


    st.dataframe(
        second_df.style.format({
        '% Perf': '{:.2f}',
        'APS': '{:.2f}',
        'DPS': '{:.2f}',
        'Lifesteal': '{:.1f}%',
        'Regen/s': '{:.2f}%',
        'Regen/hit': '{:.2f}%'
    }),  
        use_container_width=True, 
        height="content", 
        hide_index=True
    )

    st.divider()
    st.write("Here is the full breakpoint table for your build:")
    st.dataframe(df, use_container_width=True, height="content", hide_index=True)
    


