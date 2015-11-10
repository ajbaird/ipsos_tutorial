# reponding to the requested problems: 

import numpy as np 
import pandas as pd 
import sys

def q1(): 
	# import the data into a panda dataframe: 
	data = pd.read_csv('example_data.csv')
	predict = []

	# preform the loop over all rows and compute abs diff 
	for j in np.arange(250):
		store = []   #temp arrray to store index values 
		for i in np.arange(250):	
			if j != i: 
				temp = np.abs(data.loc[j]-data.loc[i])   # take the difference of each row
				temp = temp.sum()   # sum the differences
				store.append(temp)   # add them to an array 
		index = np.argsort(store)   # sort the array to get the original indeces 
		#print index
		# compute the mean of the outcomes for the smallest differences
		sum = 0
		for i in np.arange(4):
			sum = sum + data.loc[index[i],'OUTCOME']
			#print sum
		print 'predicted outcome for' + str(j) + '= ' + str(sum/5.0) 
		predict.append(sum/5.0)   # store the sums for computation of r^2 values in main routine 
	#x = test.loc(:,'OUTCOME') 
	#mu = mean(x)
	return predict, data.var(), data.mean()


if __name__ == '__main__':
	#name = input("enter file name:")
	#print 'loading file' + name
	predict, sigma, mu = q1()		
	y = np.shape(predict)
#compute r^2 value: 
	temp = 0
	for i in np.arange(y[0]): 
		# for each predicted value take the (mean-predicted)^2
		temp = (predict[i]-mu[24])**2

	# print value: 
	print 'R^2 = ' + str(1-(sigma[24]/temp))


