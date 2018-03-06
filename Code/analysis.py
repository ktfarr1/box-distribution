import numpy as np
import pandas as pd
import weightedstats as ws

ev = pd.Series([164.25, 95.83, 86.20, 60.70, 50.99, 111.54, 58.87,
				30.91, 88.93, 85.06, 60.03, 165.95, 41.74, 52.56,
				209.30, 260.78, 53.08, 79.53, 119.21, 147.03, 152.79,
				56.22, 61.34, 108.69, 234.42, 239.53, 235.34, 58.87,
				34.30, 82.18, 168.41, 29.38, 48.06, 278.27])
box = pd.Series([177.99, 119.99, 109.99, 92.99, 89.99, 159.99,
				94.99, 69.99, 108.96, 89.99, 104.95, 389.95,
				77.00, 87.50, 199.99, 399.99, 89.95, 79.95, 323.95,
				179.99, 300, 76.95, 109.95, 200, 249.95, 254.99, 425,
				79.99, 82.99, 87, 218.90, 69.99, 79.95, 499.85])
weight = np.array([1, 1, 1, 2, 2, 1, 6, 7, 2, 2, 3, 1, 7, 7,
					1, 1, 7, 7, 1, 1, 1, 7, 1, 1, 1, 1, 1, 6,
					2, 7, 1, 2, 7, 1])
label = pd.Series(["2011 Core Edition M11", "2012 Core Edition M12", "2013 Core Edition M13", "2014 Core Edition M14",
				   "2015 Core Edition M15", "Avacyn Restored", "Battle for Zendikar", "Born of the Gods", "Conspiracy",
				   "Conspiracy 2", "Dark Ascension", "Dissension", "Dragon's Maze", "Dragon's of Tarkir", "Eternal Masters",
				   "Eventide", "Fate Reforged", "Gatecrash", "Guildpact", "Iconic Masters", "Innistrad", "Journey Into Nyx",
				   "Khans of Tarkir", "Mirrodin Besieged", "Modern Masters 2015", "Modern Masters 2017", "Morningtide",
				   "Oath of the Gatewatch", "Origins", "Return to Ravnica", "Scars of Mirrodin", "Shadows over Innistrad",
				   "Theros", "Zendikar"])

data = pd.DataFrame({ 'Label': label,
					  'Expected Value': ev,
					  'Box Price': box,
					  'Weight': weight })

all = data.copy()
for i in range(34):
	copies = all.iloc[i]['Weight'] - 1
	print(copies)
	for j in range(copies):
		all = all.append(all.iloc[i], ignore_index=True)
print(all.describe())
del all['Weight']
print(all.describe())
