import matplotlib.pyplot as plt
import pandas as panda

years = []
co2 = []
temp = []

data_frame = panda.read_csv('.\climate.csv')
# print(data_frame)

years = data_frame['Year'].tolist()
co2 = data_frame['CO2'].tolist()
temp = data_frame['Temperature'].tolist()
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
plt.savefig("co2_temp_2.png")

