import numpy as np
import weightedstats as ws

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

ev = np.array([164.25, 95.83, 86.20, 60.70, 50.99, 111.54, 58.87,
				30.91, 88.93, 85.06, 60.03, 165.95, 41.74, 52.56,
				209.30, 260.78, 53.08, 79.53, 119.21, 147.03, 152.79,
				56.22, 61.34, 108.69, 234.42, 239.53, 235.34, 58.87,
				34.30, 82.18, 168.41, 29.38, 48.06, 278.27])

box = np.array([177.99, 119.99, 109.99, 92.99, 89.99, 159.99,
				94.99, 69.99, 108.96, 89.99, 104.95, 389.95,
				77.00, 87.50, 199.99, 399.99, 89.95, 79.95, 323.95,
				179.99, 300, 76.95, 109.95, 200, 249.95, 254.99, 425,
				79.99, 82.99, 87, 218.90, 69.99, 79.95, 499.85])

weight = np.array([1, 1, 1, 2, 2, 1, 6, 7, 2, 2, 3, 1, 7, 7,
					1, 1, 7, 7, 1, 1, 1, 7, 1, 1, 1, 1, 1, 6,
					2, 7, 1, 2, 7, 1])
humanreadable = np.array(["2011 Core Edition M11", "2012 Core Edition M12", "2013 Core Edition M13", "2014 Core Edition M14",
						  "2015 Core Edition M15", "Avacyn Restored", "Battle for Zendikar", "Born of the Gods", "Conspiracy",
						  "Conspiracy 2", "Dark Ascension", "Dissension", "Dragon's Maze", "Dragon's of Tarkir", "Eternal Masters",
						  "Eventide", "Fate Reforged", "Gatecrash", "Guildpact", "Iconic Masters", "Innistrad", "Journey Into Nyx",
						  "Khans of Tarkir", "Mirrodin Besieged", "Modern Masters 2015", "Modern Masters 2017", "Morningtide",
						  "Oath of the Gatewatch", "Origins", "Return to Ravnica", "Scars of Mirrodin", "Shadows over Innistrad",
						  "Theros", "Zendikar"])
def sortByEV(a, weight):
	joined = np.asarray(list(zip(a, weight)))
	joined = joined[np.argsort(a)]
	return joined

def returnSample(numSamples):
	boxes = np.asarray(['Name'])
	for b in np.arange(weight.size):
		temp = (np.tile(humanreadable[b],(weight[b],1)))
		boxes = np.vstack((boxes,temp))

	sample = (np.random.choice(np.concatenate(boxes[1:]), size=numSamples,replace=False))
	index = np.where(humanreadable == sample[0])[0][0]
	indices = [np.where(humanreadable == sample[i])[0][0] for i in np.arange(numSamples)]
	sample_table = (np.hstack((np.reshape(humanreadable[indices],(numSamples,1)),
					np.reshape(ev[indices],(numSamples,1)),
					np.reshape(box[indices],(numSamples,1)),
					np.reshape(weight[indices]/100,(numSamples,1)))))
	return sample_table

print("Mean EV: {}".format(np.mean(ev)))
print("Median EV: {}".format(np.median(ev)))
print("Weighted Average EV: {}".format(np.average(ev, weights=weight)))
print("Weighted Median EV: {}".format(ws.numpy_weighted_median(ev, weights=weight)))
joined = sortByEV(ev,weight)
print("Percentage of boxes under the median EV: {}".format(np.sum(joined[:9,1])/100))
print("Percentage of boxes with EV over cost: {}".format(np.sum(joined[-12:,1])/100))

print("Mean Box: {}".format(np.mean(box)))
print("Median Box: {}".format(np.median(box)))
print("Weighted Average Box: {}".format(np.average(box, weights=weight)))
print("Weighted Median Box: {}".format(ws.numpy_weighted_median(box, weights=weight)))
joinedBox = sortByEV(box,weight)
print("Percentage of boxes under the median Cost: {}".format(np.sum(joinedBox[:8,1])/100))
print("Percentage of boxes with Cost >= 109.99: {}".format(np.sum(joined[-16:,1])/100))

# boxes = np.asarray(['Name'])
# for b in np.arange(weight.size):
# 	temp = (np.tile(humanreadable[b],(weight[b],1)))
# 	boxes = np.vstack((boxes,temp))

# sample = (np.random.choice(np.concatenate(boxes[1:]), size=49,replace=False))
# index = np.where(humanreadable == sample[0])[0][0]
# indices = [np.where(humanreadable == sample[i])[0][0] for i in np.arange(49)]
# sample_table = (np.hstack((np.reshape(humanreadable[indices],(49,1)),
# 				np.reshape(ev[indices],(49,1)),
# 				np.reshape(box[indices],(49,1)),
# 				np.reshape(weight[indices]/100,(49,1)))))
sample_table = returnSample(13)
# print(sample_table[:,0])
print(sample_table[sample_table[:,1].astype(np.float).argsort()])
print(np.mean(sample_table[:,1].astype(np.float)),np.median(sample_table[:,1].astype(np.float)))
# print(np.arange(1,101,3).shape)
labels = np.asarray(["People","Mean of Means","Median of Means","Standard Deviation of Means",
					"Mean of Medians","Median of Medians","Standard Deviation of Medians"])
result = np.zeros((1,7))
# print(result)
#34 rows containing [mean mean, median mean, std mean, mean median, median median, std median]

for n in np.arange(1,101,3):
	row = np.empty((100,2))

	for i in np.arange(100):
		sample_table = returnSample(n)
		# print(sample_table[sample_table[:,1].astype(np.float).argsort()])
		row[i] = [np.mean(sample_table[:,1].astype(np.float)), np.median(sample_table[:,1].astype(np.float))]
	# result = np.concatenate((result,[n,np.mean(row[:,0]), np.median(row[:,0]), np.std(row[:,0]), np.mean(row[:,1]),np.median(row[:,1]),np.std(row[:,1])]),axis=0)
	result = np.r_['0,2',result,[n,np.mean(row[:,0]), np.median(row[:,0]), np.std(row[:,0]), np.mean(row[:,1]),np.median(row[:,1]),np.std(row[:,1])]]

'''
def plot_data(result):
	labels = ["People", "Dollars"]
'''

# plt.scatter(result[1:,0],result[1:,1], label='Mean of Means', color='k', s=25, marker='o')
plt.scatter(result[1:,0],result[1:,2],label='Median of Means', color='r', s=25, marker='*')
yerror = result[1:,3].astype(np.float)*0.1
plt.errorbar(result[1:,0],result[1:,1],yerr=yerror,label="Median Error")

'''
# plt.scatter(result[1:,0],result[1:,4],label='Mean of Medians', color='r', s=25, marker='o')
plt.scatter(result[1:,0],result[1:,5],label='Median of Medians', color='r', s=25, marker='*')
yerror = result[1:,6].astype(np.float)*0.1
# print(result[1:,0].dtype, result[1:,1].dtype, yerror.dtype)
plt.errorbar(result[1:,0],result[1:,4],yerr=yerror,label="Median Error")
'''
plt.xlabel('People')
plt.xticks(np.arange(1,101,9))
plt.ylabel('Dollars')
plt.yticks(np.arange(55,86,3))
plt.title('Medians')
plt.legend()
plt.show()