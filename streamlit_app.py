import streamlit as st

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
    "Blowgun": 1.0,
    "Rock": 1.0,
    "Slinger": 1.0,
    # Medieval
    "Bow": 1.0,
    "Tomahawk": 1.0,
    # Early-Modern
    "Crossbow": 1.0,
    "Dual Pistols": 1.0,
    "Musket": 1.0,
    # Modern
    "AK": 1.0,
    "M4": 1.0,
    "Sniper": 1.0,
    "Uzi": 1.0,
    # Space
    "Blaster": 1.0,
    "Space Gun": 1.0,
    "Space Pistol": 1.0,
    # Interstellar
    "Ionic Blaster": 1.0,
    "Plasma Rifle": 1.0,
    "Ray Gun": 1.0,
    # Multiverse
    "Virtual Gun": 1.0,
    "Virtual Bow": 1.0,
    # Quantum
    "Black Bow": 1.0,
    "Black Gun": 1.0,
    "Black Staff": 1.0,
    # Underworld
    "Abyssal Fork": 1.0,
    "Abyssal Trident": 1.0,
    # Divine
    "Staff": 1.0,
    "Staff of Wisdom": 1.0,
}
 
item_windup = weapon_windups.get(selected_item, 1.0)

# Display it to test
st.write(f"Item Windup for {selected_item}: **{item_windup}s**")

# 1. Dictionary for all skin modifiers
skin_modifiers = {
    "Anubis": 1.0,
    "Boxer": 1.0,
    "Bunny": 1.0,
    "Cat": 1.0,
    "Chef": 1.0,
    "Clown": 1.0,
    "Cubeguy": 1.0,
    "Dark Planet Warrior": 1.0,
    "Demon": 1.0,
    "Druid": 1.0,
    "Eagle": 1.0,
    "Fishbowl": 1.0,
    "Flower": 1.0,
    "King": 1.0,
    "Knight": 1.0,
    "Lavaman": 1.0,
    "Leprechaun": 1.0,
    "Millionaire": 1.0,
    "Mummy": 1.0,
    "Mushroom": 1.0,
    "Reaper": 1.0,
    "Shark": 1.0,
    "Skater": 1.0,
    "Skeleton": 1.0,
}

if skin_q != "None":
  skin_windup = skin_modifiers.get(skin_q, 1.0)
  st.write(f"Active Skin: **{skin_q}** (Windup: {skin_windup})")

