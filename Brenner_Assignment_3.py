# Adam Brenner
# Assignment 3

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# PART 1

filePath = os.path.abspath('mpg.csv')
mpgData = pd.read_csv(filePath)

# correlation heatmap
plt.figure(figsize = (12,10))
corrHeat = sns.heatmap(mpgData[['mpg', 'cylinders', 'displacement',
                        'horsepower', 'weight', 'acceleration', 'model_year']])
plt.title('Heatmap Correlation of Numeric Columns in MPG')
plt.show()

# correlation pairplot
corrPair = sns.pairplot(mpgData[['mpg', 'cylinders', 'displacement',
                        'horsepower', 'weight', 'acceleration', 'model_year']],
                        height = 1.1)
plt.suptitle('Correlation Pairplot by Numeric Columns')
plt.show()

# PART 2

diaData = sns.load_dataset('diamonds')

diaData2 = diaData[(~diaData.color.isin(["D","E"])) & (diaData.cut!="Fair")]
diaData2["color"] = diaData2["color"].cat.remove_unused_categories()
diaData2["cut"] = diaData2["cut"].cat.remove_unused_categories()

facetDia = sns.FacetGrid(diaData2, col = "cut", row = "color", height = 2)
facetDia.map(sns.scatterplot, "price", "carat")
plt.suptitle('Price vs Carat by Cut and Color')
plt.show()

# PART 3

carCrash = sns.load_dataset('car_crashes')

plt.title('Total Car Crashes based on Speeding')
scat = sns.regplot(x = "total", y = "speeding", data = carCrash)
plt.show()

plt.title('Total Car Crashes based on Alcohol')
scat = sns.regplot(x = "total", y = "alcohol", data = carCrash)
plt.show()

# PART 4

# iris = sns.load_dataset('iris')

fig, axes = plt.subplots(2,2,figsize = (10,10))
fig.suptitle('Numeric Column Distribution by Species')
sns.boxplot(ax = axes[0,0], data = iris, x = 'species', y = 'sepal_length')
sns.boxplot(ax = axes[0,1], data = iris, x = 'species', y = 'sepal_width')
sns.boxplot(ax = axes[1,0], data = iris, x = 'species', y = 'petal_length')
sns.boxplot(ax = axes[1,1], data = iris, x = 'species', y = 'petal_width')
plt.show()
