import streamlit as st
import json

# Chargement des prompts
with open("prompts.json", "r") as f:
    prompts = json.load(f)

st.set_page_config(page_title="Proto Cadrage Automatisé", layout="wide")
st.title("🛠️ Proto Cadrage Automatisé")

st.markdown("""
Ce prototype te permet de :
1. Choisir un type de scénario.
2. Coller tes notes / pitch.
3. Générer le prompt complet prêt à copier-coller vers GPT.
""")

# Choix du scénario
scenarios = list(prompts.keys())
selected_scenario = st.selectbox("Choisir le type de traitement :", scenarios)

# Affichage de la description
st.info(prompts[selected_scenario]["description"])

# Entrée des notes / pitch
user_input = st.text_area("Coller vos notes ou pitch ici", height=200)

# Bouton de génération
if st.button("Générer prompt + notes"):
    if user_input.strip() == "":
        st.warning("Veuillez coller vos notes ou pitch avant de générer le prompt.")
    else:
        full_prompt = prompts[selected_scenario]["prompt"] + "\n\n" + user_input
        st.text_area("Prompt prêt à envoyer à GPT :", value=full_prompt, height=400)
