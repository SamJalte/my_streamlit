import streamlit as st
import pandas as pd

''' Imortant pour l'utilisation de streamlit : il faut ouvrir le terminal sur mac 
1. Lancer : cd /Users/jalte/Desktop/WCS/test_streamlit
2. streamlit run my_streamlit_app.py
'''

st.title('Hello Wilders, welcome to my application!')
name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")



st.write("I enjoy to discover stremalit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
st.write(df_weather)

# Here we use "magic commands":
df_weather

#Identifier les colonnes non-numériques
df_weather.dtypes   

# Exclure les colonnes non-numériques
import numpy as np
df_numeric = df_weather.select_dtypes(include=[np.number])
#Calculer la matrice de corrélation
correlation_matrix = df_numeric.corr()


st.line_chart(df_weather['MAX_TEMPERATURE_C'])

# Utiliser Seaborn pour la heatmap
import seaborn as sns
import matplotlib.pyplot as plt

viz_correlation = sns.heatmap(correlation_matrix, center=0, cmap=sns.color_palette("vlag", as_cmap=True))
plt.show()
st.pyplot(viz_correlation.figure)




