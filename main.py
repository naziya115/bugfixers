# libraries
import pandas as pd
import matplotlib.pyplot as plt


# import data
data = pd.read_csv("task3.csv")

# task 3
res = pd.DataFrame()
goods = data[['Region', 'Goods sales']].groupby(by="Region")
population = data[['Region', 'Population']].groupby(by="Region")
res = goods['Goods sales'].sum() / population['Population'].sum()
res.sort_values(ascending=False, inplace=True)

# Showing on the bar chart
plt.bar(res.index, res.values)
plt.title('Average goods per capita by region')
plt.xlabel('Regions')
plt.ylabel('Average goods  per capita')
plt.show()

# task 4
data['UrbanRural'] = 'Rural'
data.loc[data['Population Density'] > 100, ['UrbanRural']] = "Urban"
res = pd.DataFrame()
goods = data[['UrbanRural', 'Goods sales']].groupby(by="UrbanRural")
population = data[['UrbanRural', 'Population']].groupby(by="UrbanRural")
res = goods['Goods sales'].sum() / population['Population'].sum()
res.sort_values(ascending=False, inplace=True)

plt.bar(res.index, res.values)
plt.title('Average goods per capita by Urban and Rural')
plt.xlabel('Country areas')
plt.ylabel('Average goods per capita')
plt.show()
