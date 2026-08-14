import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("gapminder(2007).csv")
data.head()
data.groupby("continent").size().plot(kind="pie",autopct="%.3g")
plt.pie(data.groupby("continent").size(),autopct="%.3g",
       labeldistance=1.15,
       wedgeprops={"linewidth":2,"edgecolor":"white"})
plt.show()