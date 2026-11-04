import streamlit as st
import math
import numpy as np
import pandas as pd
import time

if "clicked" not in st.session_state:
    st.session_state.clicked = False


st.title("Beardy's Forge Master DPS Optimiser")
st.write(
    "Please select your weapon:" 
)


col1, col2 = st.columns([3, 2], wrap=False)
with col1:
    st.write("Do you have ranged or melee weapon?") 
with col2:
    melee_bad = st.segmented_control(
        "Do you have ranged or melee weapon?", 
        [
            "Ranged", 
            "Melee"
        ],
        required=True,
        default="Ranged",
        selection_mode="single", 
        label_visibility="collapsed",
        width="stretch"  
    ) 

# Melee weapons and their base windup times by age 
MELEE_WEAPONS = {
    "Primitive": {
        "Axe": 0.767,
        "Bone": 0.600,
        "Branch": 0.783,
        "Club": 0.933,
    },
    "Medieval": {
        "Sword & Shield": 0.567,
        "Spear & Shield": 0.650,
        "Scythe": 0.567,
        "War Hammer": 0.783,
        "Katana": 0.900,
    },
    "Early-Modern": {
        "Executioner": 0.667,
        "Pirate Sword": 0.767,
        "Rapier": 0.667,
    },
    "Modern": {
        "Baton": 0.583,
        "Knuckle Dusters": 0.667,
        "Riot Shield": 0.733,
        "Wrench": 0.783,
    },
    "Space": {
        "Robot Sword": 0.767,
        "Saber": 0.783,
    },
    "Interstellar": {
        "Double Saber": 0.750,
        "Isobaric Cutter": 0.717,
        "Light & Shield": 0.750,
    },
    "Multiverse": {
        "Projected Cutlass": 0.700,
        "Spearsh": 0.700,
        "Trident": 0.700,
        "Virtual Sword": 0.883,
    },
    "Quantum": {
        "Black Hammer": 1.100,
        "Black Spear": 0.900,
        "Black Sword & Shield": 0.567,
    },
    "Underworld": {
        "Soulpiercer": 0.817,
        "Doom Mace": 0.900,
        "Shadow Scimitar": 0.383,
    },
    "Divine": {
        "Angelic Pitchfork": 0.667,
        "Dragon Dagger": 0.733,
        "Serpent Sword": 0.733,
        "Siren's Song": 0.317,
    },
}

# Ranged weapons and their base windup times by age 
RANGED_WEAPONS = {
    "Primitive": {
        "Blowgun": 0.467,
        "Rock": 0.683,
        "Slinger": 1.083,
    },
    "Medieval": {
        "Bow": 1.083,
        "Tomahawk": 0.683,
    },
    "Early-Modern": {
        "Crossbow": 0.567,
        "Musket": 0.667,
        "Dual Pistols": 0.833,
    },
    "Modern": {
        "AK": 0.500,
        "M4": 0.500,
        "Sniper": 0.833,
        "Uzi": 0.333,
    },
    "Space": {
        "Blaster": 0.667,
        "Space Gun": 0.717,
        "Space Pistol": 0.917,
    },
    "Interstellar": {
        "Ionic Blaster": 0.667,
        "Plasma Rifle": 0.833,
        "Ray Gun": 0.967,
    },
    "Multiverse": {
        "Virtual Bow": 1.083,
        "Virtual Gun": 0.833,
    },
    "Quantum": {
        "Black Bow": 0.833,
        "Black Gun": 1.000,
        "Black Staff": 0.950,
    },
    "Underworld": {
        "Infernal Trident": 1.000,
        "Abyssal Fork": 0.817,
    },
    "Divine": {
        "Staff": 0.833,
        "Staff Of Wisdom": 0.717,
    },
}

selected_age = st.segmented_control(
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
    required=True,
    default="Primitive",
    selection_mode="single",
    width="stretch" 
    )

if melee_bad == "Melee":
    items=[f"{w}" for w, t in MELEE_WEAPONS[selected_age].items()]

else:
    items=[f"{w}" for w, t in RANGED_WEAPONS[selected_age].items()]
 
# choose item 
selected_item = st.segmented_control(
    "Weapon:",
    items, 
    required=True,
    default=items[0],
    selection_mode="single"
    )

# get winduo
if melee_bad == "Melee":
    item_windup =  MELEE_WEAPONS[selected_age].get(selected_item, 1.5)
else:
    item_windup = RANGED_WEAPONS[selected_age].get(selected_item, 1.5)

col1, col2 = st.columns([3, 2], wrap=False)
with col1:
    st.write("Do you have a weapon skin?") 
with col2:
    skin_hider = st.segmented_control(
        "Do you have a weapon skin?", 
        [
            "Yes", 
            "No"
        ],
        required=True,
        default="No",
        selection_mode="single",
        label_visibility="collapsed",
        width="stretch" 
    ) 
if skin_hider == "No":
    skin_q="None"
else:
    skin_q = st.segmented_control(
        "Skin:",
        [
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
            "Guardian", 
            "King",
            "Knight",
            "Lavaman",
            "Leprechaun",
            "Millionaire",
            "Moth", 
            "Mummy",
            "Mushroom",
            "Reaper",
            "Santa", 
            "Shadow", 
            "Shark",
            "Skater",
            "Skeleton",
            "Ski", 
            "Snowman", 
        ],
        required=True,
        default="Clown",
        selection_mode="single",
        #width="stretch" 
)


# Show on screen windup
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
    "Moth": 0.717,
    "Mummy": 0.667,
    "Mushroom": 0.733,
    "Reaper": 0.567,
    "Santa": 0.783,
    "Shadow": 0.717,
    "Shark": 0.9,
    "Skater": 0.733,
    "Skeleton": 0.783,
    "Ski": 0.783,
    "Snowman": 0.783
}

if skin_q != "None":
  skin_windup = skin_modifiers.get(skin_q, 1.0)
  if skin_q == "Druid" and melee_bad=="Melee":
      skin_windup=0.667
  elif skin_q == "Flower" and melee_bad=="Melee":
      skin_windup=0.783
  st.write(f"Windup for **{skin_q}** skin: {skin_windup}")

N_ls = st.slider(
    label="Select desired amount of lifesteal slots:", 
    min_value=0,
    max_value=12,
    value=3,
    step=1
)

# Columns force the segmented control to take up only 1 line
col1, col2 = st.columns([1, 3], wrap=False)
with col1:
    st.markdown("**Fairy Choice:**")
with col2:
    fairy_choice = st.segmented_control(
        "Fairy Choice Label", # Hidden label
        ["Damage", "5th hit boost", "Shield"], 
        label_visibility="collapsed", #Hides label
        required=True,
        default="5th hit boost", 
        selection_mode="single", 
        width="stretch"   
    )

if fairy_choice == "Shield" and melee_bad == "Ranged":
    target_options=["Overall", "vs Shield"] 
else:
    target_options=["Overall", "vs Shield", "Mixed"] 
fairy_shield = st.segmented_control(
    "Do you want to aim for best DPS overall, or vs critical hit defence fairy?", 
    target_options,
    required=True,
    default="Overall",
    selection_mode="single"
) 
if fairy_shield == "Overall":
    c_shield_q=0
elif fairy_shield == "vs Shield":
    c_shield_q=1
else:
    c_shield_q=2


# Create 3 columns: push space to the left, keep button on the right
col1, col2 = st.columns([3, 2], wrap=False)

with col2:
    clicked = st.button("Let's go!", width="stretch")

if clicked:
    st.session_state.clicked = clicked

def calculate_breakpoints(Windup):
    #fun comes here
    breakpoints=[[0,0,0]] #initialise
    BaseD=1.5 #standard time for all weapons
    
    inc= math.floor((2**32)/10)/(2**32) #fd6
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
            
                

def best_substats_5th(timings, N_ls, c_shield, melee_q):
    timings=np.array(timings)
    # function for finding optimal substat builds
    cd_max = 0.8
    cc_max = 0.12
    dc_max = 0.2
    dmg_max = 0.15
    if melee_q == "Ranged":
        rdmg_max = 0.15
        cs_max=5.26
    else:
        rdmg_max = 0.5
        cs_max=10.19
    spd_max = 0.4

    # CC = 0.8 #setting manually due to Mira, update at each new fairy launch
    
    # initialise
    Record=[[0,0,0,0,0,0,0,0,0]]
    Record_stats=[]
    
    for i in range(70,101):
        perf=i/100
        bestest=[0,0,0,0,0,24,0,0]
        
        for N_cc in range(13):
            CC = min(1, N_cc * cc_max * perf)
        
            for N_cd in range(13):
                cd = N_cd * cd_max * perf
        
                for N_dmg in range(13):  # 0 to 6 inclusive
                    dmg = N_dmg * dmg_max * perf
                    if melee_q == "Ranged":
                        rdmg_lim = N_dmg
                    else:
                        rdmg_lim = 12
                    for N_rdmg in range(rdmg_lim + 1):  # 0 up to N_dmg inclusive
                        rdmg = N_rdmg * rdmg_max * perf
                
                        for N_dc in range(8):  # 0 to 6 inclusive
                            dc = min(1, dc_max * N_dc * perf)
                    
                            for N_spd in range(1, 13):
                                if (N_cc+N_spd+N_dc+N_rdmg+N_dmg+N_cd) == (24-N_ls):
                                    spd = N_spd * spd_max * perf * 100
                                    
                                    B = timings[:,0]<spd
                                    C = timings[B]
                                    time1 = C[-1, 1:3]
                                    
                                    APS = (1 - dc) / time1[0] + dc * 2 / time1[1] 
                                    Crit_multi1 = CC * (1.2 + cd) + 1 - CC
                                    Crit_multi2 = CC * (1.2 + cd) * 0.3 + 1 - CC
                                    DPS1 = (dmg + 1) * (rdmg + 1) * Crit_multi1 * APS * 1.44
                                    DPS2 = (dmg + 1) * (rdmg + 1) * Crit_multi2 * APS * 1.44

    
                                    best_new = [N_cc, N_cd, N_dmg, N_rdmg, N_dc, N_spd, DPS1, DPS2]
    
                                    if c_shield==0:
                                        DPS=DPS1
                                        val_check = 6
                                    elif c_shield==1:
                                        DPS=DPS2
                                        val_check = 7
                                    else:
                                        if DPS2<cs_max:
                                            DPS=0
                                            DPS1=0
                                        else:
                                            DPS=DPS1
                                        val_check=6

                                    if DPS > bestest[val_check]:
                                        bestest = best_new
                                        best_val = [perf, CC*100, cd*100, dmg*100, rdmg*100, dc*100, spd, DPS1, DPS2]
    
                                    elif DPS == bestest[val_check]:
                                        if max(best_new[0:6]) < max(bestest[0:6]):
                                            bestest = best_new
                                            best_val = [perf, CC*100, cd*100, dmg*100, rdmg*100, dc*100, spd, DPS1, DPS2]
        
        last_row_check = Record[-1][1:6]
        if np.any(last_row_check != bestest[0:5]) and best_val[7]>0:
            new_row = [perf] + bestest
            Record.append(new_row)
            Record_stats.append(best_val) 
     
    Record = np.array(Record)
    Record = Record[1:] 
    Record_stats = np.array(Record_stats)

    return Record, Record_stats
                       

def best_substats_dmg(timings, N_ls, c_shield, melee_q):
    timings=np.array(timings)
    # function for finding optimal substat builds
    cd_max = 0.8
    cc_max = 0.12
    dc_max = 0.2
    dmg_max = 0.15
    if melee_q == "Ranged":
        rdmg_max = 0.15
        cs_max=5.26
    else:
        rdmg_max = 0.5
        cs_max=10.19
    spd_max = 0.4
    spd_max = 0.4

    # CC = 0.8 #setting manually due to Mira, update at each new fairy launch
    
    # initialise
    Record=[[0,0,0,0,0,0,0,0,0]]
    Record_stats=[] 
    
    for i in range(70,101):
        perf=i/100
        bestest=[0,0,0,0,0,24,0,0]
        
        for N_cc in range(13):
            CC = min(1, N_cc * cc_max * perf)
        
            for N_cd in range(13):
                cd = N_cd * cd_max * perf
        
                for N_dmg in range(13):  # 0 to 12 inclusive
                    N_health=N_dmg
                    health_r = N_health * perf * 0.15
                    dmg = math.floor(health_r/0.1) * 0.15
                    if melee_q == "ranged":
                        rdmg_lim = N_dmg
                    else:
                        rdmg_lim = 12
                    for N_rdmg in range(rdmg_lim + 1):  # 0 up to N_dmg inclusive
                        rdmg = N_rdmg * rdmg_max * perf
                
                        for N_dc in range(8):  # 0 to 6 inclusive
                            dc = min(1, dc_max * N_dc * perf)
                    
                            for N_spd in range(1, 13):
                                if (N_cc+N_spd+N_dc+N_rdmg+N_health+N_cd) == (24-N_ls):
                                    spd = N_spd * spd_max * perf * 100
                                    
                                    B = timings[:,0]<spd
                                    C = timings[B]
                                    time1 = C[-1, 1:3]
                                    
                                    APS = (1 - dc) / time1[0] + dc * 2 / time1[1]
                                    Crit_multi1 = CC * (1.2 + cd) + 1 - CC
                                    Crit_multi2 = CC * (1.2 + cd) * 0.3 + 1 - CC
                                    DPS1 = (dmg + 1) * (rdmg + 1) * Crit_multi1 * APS
                                    DPS2 = (dmg + 1) * (rdmg + 1) * Crit_multi2 * APS
                                    

    
                                    best_new = [N_cc, N_cd, N_dmg, N_rdmg, N_dc, N_spd, DPS1, DPS2]
    
                                    if c_shield==0:
                                        DPS=DPS1
                                        val_check = 6
                                    elif c_shield==1:
                                        DPS=DPS2
                                        val_check = 7
                                    else:
                                        if DPS2<cs_max:
                                            DPS=0
                                            DPS1=0
                                        else:
                                            DPS=DPS1
                                        val_check=6
                                    if DPS > bestest[val_check]:
                                        bestest = best_new
                                        best_val = [perf, CC*100, cd*100, health_r*100, rdmg*100, dc*100, spd, DPS1, DPS2]
    
                                    elif DPS == bestest[val_check]:
                                        if max(best_new[0:6]) < max(bestest[0:6]):
                                            bestest = best_new
                                            best_val = [perf, CC*100, cd*100, health_r*100, rdmg*100, dc*100, spd, DPS1, DPS2]
        
        last_row_check = Record[-1][1:6]
        if np.any(last_row_check != bestest[0:5]) and best_val[7]>0:
            new_row = [perf] + bestest
            Record.append(new_row)
            Record_stats.append(best_val)
     
    Record = np.array(Record)
    Record = Record[1:]
    Record_stats = np.array(Record_stats) 

    return Record, Record_stats


def best_substats(timings, N_ls, c_shield, melee_q):
    timings=np.array(timings)
    # function for finding optimal substat builds
    cd_max = 0.8
    cc_max = 0.12
    dc_max = 0.2
    dmg_max = 0.15
    if melee_q == "Ranged":
        rdmg_max = 0.15
        cs_max=5.26
    else:
        rdmg_max = 0.5
        cs_max=10.19
    spd_max = 0.4

    
    # initialise
    Record=[[0,0,0,0,0,0,0,0,0]]
    Record_stats=[] 
    
    for i in range(70,101):
        perf=i/100
        bestest=[0,0,0,0,0,24,0,0]
        
        for N_cc in range(13):
            CC = min(1, N_cc * cc_max * perf)
        
            for N_cd in range(13):
                cd = N_cd * cd_max * perf
        
                for N_dmg in range(13):  # 0 to 6 inclusive
                    dmg = N_dmg * dmg_max * perf
                    if melee_q == "Ranged":
                        rdmg_lim = N_dmg
                    else:
                        rdmg_lim = 12
                    for N_rdmg in range(rdmg_lim + 1):  # 0 up to N_dmg inclusive
                        rdmg = N_rdmg * rdmg_max * perf
                
                        for N_dc in range(8):  # 0 to 6 inclusive
                            dc = min(1, dc_max * N_dc * perf)
                    
                            for N_spd in range(1, 13):
                                if (N_cc+N_spd+N_dc+N_rdmg+N_dmg+N_cd) == (24-N_ls-4):
                                    spd = N_spd * spd_max * perf * 100
                                    
                                    B = timings[:,0]<spd
                                    C = timings[B]
                                    time1 = C[-1, 1:3]
                                    
                                    APS = (1 - dc) / time1[0] + dc * 2 / time1[1]
                                    Crit_multi1 = CC * (1.2 + cd) + 1 - CC
                                    Crit_multi2 = CC * (1.2 + cd) * 0.3 + 1 - CC
                                    DPS1 = (dmg + 1) * (rdmg + 1) * Crit_multi1 * APS
                                    DPS2 = (dmg + 1) * (rdmg + 1) * Crit_multi2 * APS
    
                                    best_new = [N_cc, N_cd, N_dmg, N_rdmg, N_dc, N_spd, DPS1, DPS2]
                                    if c_shield==0:
                                        DPS=DPS1
                                        val_check = 6
                                    elif c_shield==1:
                                        DPS=DPS2
                                        val_check = 7
                                    else:
                                        if DPS2<cs_max:
                                            DPS=0
                                            DPS1=0
                                        else:
                                            DPS=DPS1
                                        val_check=6
    
                                    if DPS > bestest[val_check]:
                                        bestest = best_new
                                        best_val = [perf, CC*100, cd*100, dmg*100, rdmg*100, dc*100, spd, DPS1, DPS2]
    
                                    elif DPS == bestest[val_check]:
                                        if max(best_new[0:6]) < max(bestest[0:6]):
                                            bestest = best_new
                                            best_val = [perf, CC*100, cd*100, dmg*100, rdmg*100, dc*100, spd, DPS1, DPS2]
        
        last_row_check = Record[-1][1:6]
        if np.any(last_row_check != bestest[0:5]) and best_val[7]>0:
            new_row = [perf] + bestest
            Record.append(new_row)
            Record_stats.append(best_val)
     
    Record = np.array(Record)
    Record = Record[1:]
    Record_stats = np.array(Record_stats)

    return Record, Record_stats



def dynamic_step(x):
    if x == 0 or x is None:
        return 0.01
    try:
        return float(10 ** (math.floor(math.log10(abs(x))) - 2)) 
    except ValueError:
        return 0.01
def dynamic_number_input(label, key, min_value=0.0):
    if key not in st.session_state:
        st.session_state[key] = min_value
    step_size = dynamic_step(st.session_state[key])

    return st.number_input(label, min_value=min_value, step=step_size, key=key)


if clicked:
    print(fairy_choice)
    with st.spinner("Finding highest DPS build...", show_time=True):
        item_breakpoints = calculate_breakpoints(item_windup)

        if skin_q !="None":
            skin_breakpoints = calculate_breakpoints(skin_windup)
            final_breakpoints, wearing = combine_breakpoints(item_breakpoints,skin_breakpoints)
        else:
            final_breakpoints = item_breakpoints
            wearing = [] 

    
        if fairy_choice == "5th hit boost":
            SubN, SubV = best_substats_5th(final_breakpoints, N_ls, c_shield_q, melee_bad)
        elif fairy_choice == "Damage":
            SubN, SubV = best_substats_dmg(final_breakpoints, N_ls, c_shield_q, melee_bad)
        else:
            SubN, SubV = best_substats(final_breakpoints, N_ls, c_shield_q, melee_bad)

    st.session_state.final_breakpoints = final_breakpoints
    st.session_state.wearing = wearing
    st.session_state.SubN = SubN
    st.session_state.SubV = SubV

if st.session_state.clicked:

    st.success("Done!") 

    final_breakpoints = st.session_state.final_breakpoints
    wearing = st.session_state.wearing
    SubN = st.session_state.SubN
    SubV = st.session_state.SubV


    df = pd.DataFrame(final_breakpoints,columns=["Attack Speed", "Single Attack cycle", "Double Attack cycle"]) 
    if skin_q != "None":
        df["Applied Skin"] = wearing 

    if fairy_choice == "Damage":
        col_names = ['% Perf', 'Crit %', 'Crit Dmg', 'Health', melee_bad, 'Double', 'Speed'] 
    else:
        col_names = ['% Perf', 'Crit %', 'Crit Dmg', 'Damage', melee_bad, 'Double', 'Speed']

    combined_df = pd.DataFrame()
    combined_df['% Perf'] = SubN[:, 0]

    # Loop through columns 1 to 5 to combine raw and scaled values
    for i, col_name in enumerate(col_names[1:], start=1):
        raw_vals = SubN[:, i]
        print(SubV[:, i]) 
        scaled_vals = SubV[:, i]
    
    # Combine them into a "Raw / Scaled" string format
    # (Using int() on raw values since tiers are whole numbers, and .1f for scaled)
        combined_df[col_name] = [
            " " if int(r) == 0 else f"{int(r)} ({s:.1f}%)" 
            for r, s in zip(raw_vals, scaled_vals)
        ]
    
    st.divider()
    st.subheader("Results")
    st.write("This is optimising for the highest DPS, which sometimes lowers speed for bigger hits. This has the trade-off of hampering survivability if the enemy can hit you multiple times between your lifesteal activating. \n\nHere are the number of slots that should be given to each substat if the required level of perfection is reached, plus the raw substat value:")
    st.dataframe(
        combined_df, 
        width="stretch", 
        height="content", 
        hide_index=True
    )

    st.write("Below we look at the PvP capabilities of these builds. \n\nNote: standard health is 8x damage, with a 5x multiplier in PvP. Pet typing and equipped items levels can change this distribution. These percentages assume health is the standard 40x base damage before modifiers.") 

    col_names = ["% Perf", "Speed", "APS", "DPS normal", "DPS v shield", "Lifesteal", "Regen/s", "Regen/hit"] 
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
    second_df['DPS normal'] = SubV[:,7]
    second_df['DPS v shield'] = SubV[:,8]
    second_df['Lifesteal'] = lifesteal 
    second_df['Regen/s'] = regenS
    second_df['Regen/hit'] = regenH

    


    st.dataframe(
        second_df.style.format({
        '% Perf': '{:.2f}',
        'APS': '{:.2f}',
        'DPS normal': '{:.2f}',
        'DPS v shield': '{:.2f}',
        'Lifesteal': '{:.1f}%',
        'Regen/s': '{:.2f}%',
        'Regen/hit': '{:.2f}%'
    }),  
        width="stretch", 
        height="content", 
        hide_index=True
    )

    if fairy_choice == "5th hit boost":
        st.write("This DPS value is the average over the 5 hits from the fairies boost. The first 4 hits will be 69.4% of the average, and the 5th is 2.22x the average")
    elif fairy_choice == "Shield":
        st.write("This assumes 4 slots for skill cooldown used.")

    if fairy_shield == "Mixed" and melee_bad == "Melee":
        st.write("A minimum acceptable DPS vs the crit shielded fairy has been set to 10.19, the max achievable by an 84% perfect, melee shielding fairy build.")
    elif fairy_shield == "Mixed" and melee_bad == "Ranged":
        st.write("A minimum acceptable DPS vs the crit shielded fairy has been set to 5.26, the max achievable by an 84% perfect, ranged shielding fairy build." )



    st.markdown("### Compare Your Current Build")
    st.write("Do you want to compare your current build? Enter your substats below:")

    left_pane, right_pane = st.columns([1.8, 1], wrap=False)

    with left_pane:
  # --- ROW 1 of the 2x3 grid ---
        r1_c1, r1_c2 = st.columns(2, wrap=False)
        with r1_c1:
            crit_chance = dynamic_number_input("Crit Chance", "crit_chance")
        with r1_c2:
            crit_damage = dynamic_number_input("Crit Damage", "crit_damage")
  # --- ROW 2 of the 2x3 grid ---
        r2_c1, r2_c2 = st.columns(2, wrap=False) 
        with r2_c1:
            damage = dynamic_number_input("Damage", "damage")
        with r2_c2:
            ranged_damage = dynamic_number_input("Ranged Damage", "ranged_damage")
        r3_c1, r3_c2 = st.columns(2, wrap=False) 
        with r3_c1:
            double_stat = dynamic_number_input("Double Stat", "double_stat")
        with r3_c2:
            attack_speed = dynamic_number_input("Attack Speed", "attack_speed")

  # --- Optional Box Below ---
        single_hit_damage = st.number_input(
            "Single hit damage in-game (Optional)",
            value=0.0,
            help="Enter your observed in-game damage to get your exact DPS."
        ) 


    with right_pane:
        st.markdown("#### 📊 Results Panel") 
  





    st.divider()
    st.write("Here is the full breakpoint table for your build:")
    st.dataframe(df, width="stretch", height="content", hide_index=True)



st.divider()

st.markdown(
    """
    <div style="text-align: center; color: #888888; font-size: 0.85rem;">
        Special thanks and credit to the community tools that inspired and aided this project:<br>
        <a href="https://1vcian.me/fm/" target="_blank" style="color: #888888; text-decoration: underline;">1vcian's FM Tool</a> 
        &nbsp;|&nbsp; 
        <a href="https://uncledanny.github.io/ForgeMasterTools/" target="_blank" style="color: #888888; text-decoration: underline;">UncleDanny's Forge Master Tool</a>
    </div>
    """,
    unsafe_allow_html=True
)

    
print(st.session_state.clicked, flush=True) 



