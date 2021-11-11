import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

df = pd.read_csv("Dataset-data.csv")

print('Cantidad de Filas y columnas:',df.shape)
print('Nombre columnas:',df.columns)

df = df.drop(['Media Event C','First Offer Date C','Campaign ID','Age C','Partnership Discount Amount C','Payment Plan C','Financing Options C','Financing Option Discount C'],axis=1)

print('INFORMACIÓN GENERAL')
print(df.info())

wins = df[df['Is Won'] == True]

notWins = df[df['Is Won'] == False]

print('INFORMACIÓN GENERAL WINS')
print(wins.info())

print('INÚMERO DROPS')
print(wins['Drop'].value_counts())

print('INÚMERO Drop Reason C (wins)')
print(wins['Drop Reason C'].value_counts())
print('INÚMERO Lost Deal Reason C (wins)')
print(wins['Lost Deal Reason C'].value_counts())

print('INÚMERO Lost Deal Reason C (notWins)')
print(notWins['Lost Deal Reason C'].value_counts())
print('INÚMERO Lost Reason Notes C (notWins)')
print(notWins['Lost Reason Notes C'].value_counts())









