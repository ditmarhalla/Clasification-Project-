from nearest_neighbor import Nearest_Neighbour
import numpy as np
import time 


trained_data ='C:\\Users\\Ditmar\\Desktop\\University\\2 Semester\\Introduction to Programing\\Clasification-Project-\\trained.txt'
untraiend_data = 'C:\\Users\\Ditmar\\Desktop\\University\\2 Semester\\Introduction to Programing\\Clasification-Project-\\untrained.txt'

trained_file = np.loadtxt(trained_data,dtype=np.float16)
untrained_file= np.loadtxt(untraiend_data,dtype=np.float16)


number_trained= 100 
number_untrained = 1000


for n in range (number_untrained):
    classification = Nearest_Neighbour(trained_file,untrained_file[n])
    #print("The final vector is :",classification.distance())

