import streamlit as st

st.title("🎈 Beardy Does Maths")
st.write(
    "Built using streamlit: [docs.streamlit.io](https://docs.streamlit.io/) \n\nFirst, select your weapon:\n"
)
selected_era = st.selectbox(
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
        "Weapon Skins",
    ],
) 