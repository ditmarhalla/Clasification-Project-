from nearest_neighbor import Nearest_Neighbour
import numpy as np
import time 



print ("-"*100)

start = time.time()
#root
trained_data ='C:\\Users\\Ditmar\\Desktop\\University\\2 Semester\\Introduction to Programing\\Clasification-Project-\\trained.txt'
untraiend_data = 'C:\\Users\\Ditmar\\Desktop\\University\\2 Semester\\Introduction to Programing\\Clasification-Project-\\untrained.txt'

#Load the data
trained_file = np.loadtxt(trained_data,dtype=np.float16)
untrained_file= np.loadtxt(untraiend_data,dtype=np.float16)
time_data_load = time.time()
print("Time it takes to load the data",round(time_data_load - start,1)," seconds")

#Classifie the data
time_start_classifie = time.time()
classification = Nearest_Neighbour(trained_file,untrained_file)
time_end_classifie = time.time()
print("Time it takes to load the data",round(time_end_classifie -time_start_classifie,5)," seconds")
