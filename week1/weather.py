import pandas as pd
import matplotlib.pyplot as plt

# load data
weather = pd.read_csv('wetter.csv')

# converting to datetime
weather['Datum'] = pd.to_datetime(weather['Datum'])

# filter dataset & calculate
july = weather[weather['Datum'].dt.month == 7]
avg_july_temp = round(july['Temperatur'].mean(), 2)
print(f"The mean temperature for July is: ", avg_july_temp)

# calculate mean temp of Mai 
may = weather[weather['Datum'].dt.month == 5]
avg_may_temp = round(may['Temperatur'].mean(), 2)
print(f"The mean temperature for May is: ", avg_may_temp)

# calculate difference
print(f"There is a", avg_july_temp - avg_may_temp, "degree difference between May and July.")


###############
# Solultion:
# The mean temperature for July is:  20.75
# The mean temperature for May is:  15.24
# There is a 5.51 degree difference between May and July.