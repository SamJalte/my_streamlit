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

#Description des variables :

#mpg (miles per gallon) : la consommation d'essence d'une voiture.
#cylinders : le nombre de cylindres du moteur.
#cubicinches (cylindrée): le volume interne du moteur à combustion (souvent en cm3).
#hp (horsepower) : la puissance du moteur en chevaux.
#weightlbs : le poids de la voiture.
#time-to-60 (accélération) : la durée en seconde pour passer de l'arrêt (0 km/h) à 60 mph (environ 97 km/h).
#year : l'année de production du modèle.
#continent : origine des constructeurs.

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

#Remarques :
#Forte corrélation positive : entre les variables cylinder, cubicinches, hp et weightlbs.

#Forte corrélation négative : mpg avec cylinder, weightlbs, cubicinches et hp.

#Attention, ces corrélations varient selon les continents.








