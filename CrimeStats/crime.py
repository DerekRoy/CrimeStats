import pandas as pd
import matplotlib.pyplot as plt 

# Data Info
# https://data.vancouver.ca/datacatalogue/crime-data-attributes.htm#X

c = pd.read_csv("crime_csv_all_years.csv")
c = c[c['YEAR'] != 2018]

bneC = c[c['TYPE'] == "Break and Enter Commercial"] # 36010
bneR = c[c['TYPE'] == "Break and Enter Residential/Other"] # 63362
kill = c[c['TYPE'] == "Homicide"] # 236
mischief = c[c['TYPE'] == "Mischief"] # 76205
offence = c[c['TYPE'] == "Offence Against a Person"] # 57279
theftO = c[c['TYPE'] == "Other Theft"] # 57526
theftFromV = c[c['TYPE'] == "Theft from Vehicle"] # 187232
theftB = c[c['TYPE'] == "Theft of Bicycle"] # 27900
theftV = c[c['TYPE'] == "Theft of Vehicle"]# 39775
injusyCollision = c[c['TYPE'] == "Vehicle Collision or Pedestrian Struck (with Injury)"] # 23444
fatalCollision = c[c['TYPE'] == "Vehicle Collision or Pedestrian Struck (with Fatality)"]# 269

b1 = bneC.groupby(['YEAR']).count()
b2 = bneR.groupby(['YEAR']).count()
k = kill.groupby(['YEAR']).count()
m = mischief.groupby(['YEAR']).count()
o = offence.groupby(['YEAR']).count()
t1 = theftO.groupby(['YEAR']).count()
t2 = theftFromV.groupby(['YEAR']).count()
t3 = theftB.groupby(['YEAR']).count()
t4 = theftV.groupby(['YEAR']).count()
c1 = injusyCollision.groupby(['YEAR']).count()
c2 = fatalCollision.groupby(['YEAR']).count()

plt.figure(figsize=(7.5,3.5))
plt.subplot(1,3,1)
plt.plot(o.index, o['TYPE'], linewidth = 2)
plt.plot(t1.index, t1['TYPE'], linewidth = 2)
plt.plot(t2.index, t2['TYPE'], linewidth = 2)
plt.plot(t3.index, t3['TYPE'], linewidth = 2)
plt.legend(['Offence', 'Other Theft', 'Theft from Vehicle', 'Bike Theft'])

plt.subplot(1,3,2)
plt.plot(b1.index, b1['TYPE'], linewidth = 2) # 3
plt.plot(b2.index, b2['TYPE'], linewidth = 2) # 2
plt.plot(m.index, m['TYPE'], linewidth = 2) # 1
plt.plot(t4.index, t4['TYPE'], linewidth = 2) # 5
plt.plot(c1.index, c1['TYPE'], linewidth = 2) # 4
plt.legend(['BNE Commercial', 'BNE Residential', 'Mischief', 'Vehicle Theft', 'Collision Injury'])

plt.subplot(1,3,3)
plt.plot(k.index, k['TYPE'], linewidth = 2)
plt.plot(c2.index, c2['TYPE'], linewidth = 2)
plt.legend(['Murder', 'Fatal Collision'])

plt.savefig('CrimeTrend')