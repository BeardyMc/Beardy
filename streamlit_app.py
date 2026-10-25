import streamlit as st

st.title("🎈 Beardy Does Maths")
st.write(
    "Built using streamlit: [docs.streamlit.io](https://docs.streamlit.io/) \n\nFirst, select your weapon:\n"
)
era = st.selectbox(
    "Age:",
    [
        "Primitive",
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

if era == "Primative"
items = ["Blowgun", "Rock", "Slinger"] 
elif era =="Medieval"
items = ["Bow", "Tomahawk"] 
elif era == "Early-Modern" 
items = ["Crossbow", "Dual Pistols", "Musket"]
elif era == "Modern"
items = ["AK", "M4", "Sniper", "Uzi"]
elif era == "Space" 
items = ["Blaster", "Space Gun", "Space Pistol"] 
elif era == "Interstellar"
items = ["Ionic Blaster", "Plasma Rifle", "Ray Gun"]
elif era == "Multiverse" 
items = ["Virtual Gun", "Virtual Bow"] 
elif era == "Quantum" 
items = ["Black Bow", "Black Gun", "Black Staff"] 
elif era == "Underworld" 
items = ["Abyssal Fork", "Abyssal Trident"] 
elif era == "Divine" 
items = ["Staff", "Staff of Wisdom"]
else 
items = [] 

selected_item = st.selectbox(f"Select specific {category}:", items)

