import matplotlib.pyplot as plt
import sqlite3

years = []
co2 = []
temp = []

data_connecting = sqlite3.connect(r".\climate.db")
cursor = data_connecting.cursor()
cursor.execute("SELECT * FROM climatedata")
climate_data = cursor.fetchall()

# print(climate_data)

for a in climate_data:
    years.append(a[0])
    co2.append(a[1])
    temp.append(a[2])

# print(years, co2, temp)

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
