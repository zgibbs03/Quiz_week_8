import matplotlib.pyplot as plt
import sqlite3
connection = sqlite3.connect("climate.db")
cursor = connection.cursor()

years = []
co2 = []
temp = []

cursor.execute("SELECT Year FROM ClimateData")
year_Results = cursor.fetchall()
for x in year_Results:
    years.append(x)

cursor.execute("SELECT CO2 FROM ClimateData")
CO2_Results = cursor.fetchall()
for y in CO2_Results:
    co2.append(y)

cursor.execute("SELECT Temperature FROM ClimateData")
temp_Results = cursor.fetchall()
for z in temp_Results:
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
plt.savefig("co2_temp_1.png") 
