#! /usr/bin/env python
import numpy as np

#age, height in meters
person = [[11,1.56],[4, 0.80], [44, 1.88], [23, 1.68], [55, 1.74]]

np_person = np.array(person)

print(np_person)

age = np_person[:,0]

height = np_person[:,1]
 
 #average
print("average age: " + str(np.mean(age)))
print("average height: " + str(np.mean(height)))

#the standard deviation is also rounded to two decimals only.
std_height= round(np.std(height),2)

print("standard deviation of the height: "+ str(std_height))

#correlation
corr = np.corrcoef(np_person[:,0], np_person[:,1])
print("Correlation: " + str(corr))