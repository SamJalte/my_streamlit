# Imortant pour l'utilisation de streamlit : il faut ouvrir le terminal sur mac 
#1. Lancer : cd /Users/jalte/Desktop/WCS/test_streamlit
#2. streamlit run my_streamlit_app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title('Application qui analyse et visualise les données des voitures !')

st.write("Chargement des données")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_voiture = pd.read_csv(link)

#df_voiture

#df_voiture.dtypes   

# Convertir la colonne 'continent' pour une meilleurs lecture
region_mapping = {' US.': 'US', ' Europe.': 'Europe', ' Japan.': 'Japan'}
df_voiture['continent'] = df_voiture['continent'].map(region_mapping)

df_voiture

# Sélection de la région

region = st.sidebar.multiselect('Selection des regions:', options=df_voiture['continent'].unique(), default=df_voiture['continent'].unique())

st.write("Filtrage des données selon la sélection de la région")

filtered_data = df_voiture[df_voiture['continent'].isin(region)]

filtered_data

st.write("Visualisation des données")

st.subheader('Histogramme de la distribution des mpg')
fig, ax = plt.subplots()
sns.histplot(filtered_data['mpg'], kde=True, ax=ax)
st.pyplot(fig)

st.subheader('Diagramme de la corrélation')

# Convertir 'continent' en valeurs numériques catégorielles
filtered_data['continent'] = filtered_data['continent'].astype('category').cat.codes

# Calcul de la matrice de corrélation
corr_matrix = filtered_data.corr()
# Création du heatmap
plt.figure(figsize=(10, 8))
viz_correlation = sns.heatmap(corr_matrix,
                              center=0,
                              cmap=sns.color_palette('vlag',as_cmap=True),
)
st.pyplot(viz_correlation.figure)








