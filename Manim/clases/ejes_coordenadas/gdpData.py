import pandas as pd
import numpy as np

data = pd.read_csv('C:\\Users\\Bonoc\\Documents\\GitHub\\Animation_Python\\Manim\\ejes_coordenadas\\gdp_per_country.csv')

paises = ['Argentina', 'Chile', 'Uruguay', 'Brazil', 'Finland', 'France', 'Germany', 'Spain']

cleanedData = data.query('`Country Name` in @paises')

cambioGDP = (cleanedData['2021'].astype(float) - cleanedData['2020'].astype(float))

print(cambioGDP)