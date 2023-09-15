import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("climate.csv")

years = []
co2 = []
temp = []

df_Years = df["Year"]
for x in df_Years:
    years.append(x)

df_CO2 = df["CO2"]
for y in df_CO2:
    co2.append(y)

df_Temp = df["Temperature"]
for z in df_Temp:
    temp.append(z)

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

