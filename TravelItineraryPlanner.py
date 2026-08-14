import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Weather Dataset.csv")
df["month"] = pd.to_numeric(df["month"],
            errors="coerce").astype("Int64")
df_group = df.groupby("month")["Humidity"].mean().reset_index()
df_group.plot.area(x="month",y="Humidity",alpha=0.5)
plt.xlabel("Month")
plt.ylabel("Average Humidity")
plt.title("Average Humidity by Month")
plt.show()
plt.plot(df["Temperature (C)"])
plt.xlabel("Reading Number Over Time")
plt.ylabel("Temperature (C)")
plt.title("Temperature Over Time")
plt.show()