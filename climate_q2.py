import matplotlib.pyplot as plt
import pandas as panda
import sqlite3

years = []
co2 = []
temp = []

data_connecting = sqlite3.connect(r".\climate.db")
cursor = data_connecting.cursor()
cursor.execute("SELECT * FROM climatedata")

data_frame = panda.DataFrame(cursor.fetchall(), columns=['Year', 'Co2', 'Temperature'])
# print(data_frame)

years = data_frame['Year'].tolist()
co2 = data_frame['Co2'].tolist()
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

