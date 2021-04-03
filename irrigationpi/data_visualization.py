import csv

import matplotlib.pyplot as plt

time = []
temperature = []
humidity = []

# loading data from csv
with open('data.csv', newline='') as data_file:
    reader = csv.reader(data_file)
    for row in reader:
        time.append(list(row)[0])
        temperature.append(list(row)[1])
        humidity.append(list(row)[2])

# selecting only number value for time, temperature and humidity
time_str = time[1:]
temperature_str = temperature[1:]
humidity_str = humidity[1:]

# converting string to float
time = list(map(float, time_str))
temperature = list(map(float, temperature_str))
humidity = list(map(float, humidity_str))

# plotting
# time vs temperature
plt.title("time vs temperature")
plt.xlabel("time")
plt.ylabel("temperature")
plt.scatter(time, temperature)
plt.plot(time, temperature)
plt.show()

# time vs humidity
plt.title("time vs humidity")
plt.xlabel("time")
plt.ylabel("humidity")
plt.scatter(time, humidity)
plt.plot(time, humidity)
plt.show()

# temperature vs humidity
plt.title("temperature vs humidity")
plt.xlabel("temperature")
plt.ylabel("humidity")
plt.scatter(temperature, humidity)
plt.show()
