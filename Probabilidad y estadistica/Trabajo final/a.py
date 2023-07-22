import pandas as pd
import os

__dirname = os.path.dirname(__file__) + '/'
dataframe = pd.read_csv(__dirname + 'SOCR-HeightWeight.csv')

dataframe = dataframe.drop(columns=['Index'])

dataframe['Height'] = dataframe['Height'] * 2.54 # pulgada -> centimetro
dataframe['Weight'] = dataframe['Weight'] * 0.453592 # libra -> kilogramo

print(dataframe)

dataframe = dataframe.round(2)

if os.path.exists(__dirname + 'PesoAltura.csv'):
	os.remove(__dirname + 'PesoAltura.csv')

dataframe.to_csv(__dirname + 'PesoAltura.csv', index=False)


