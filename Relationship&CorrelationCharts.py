import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
data = pd.read_csv("FuelConsumption.csv")
data.head()
data.isnull().any()
data.info()
sns.lineplot(x=data["CO2EMISSIONS"],y=data["FUELCONSUMPTION_COMB_MPG"])
plt.show()
sns.lineplot(x=data["CO2EMISSIONS"],y=data["FUELCONSUMPTION_COMB_MPG"],
         hue=data["FUELTYPE"])
plt.show()
sns.histplot(x=data["CO2EMISSIONS"],y=data["FUELCONSUMPTION_COMB_MPG"],
         hue=data["FUELTYPE"],color=data["ENGINESIZE"])
plt.show()
sns.scatterplot(data=data)
plt.show()
sns.barplot(x=data["CO2EMISSIONS"],y=data["FUELCONSUMPTION_COMB_MPG"],
         hue=data["FUELTYPE"])
plt.show()
sns.histplot(data=data,hue=data["FUELTYPE"])
plt.show()