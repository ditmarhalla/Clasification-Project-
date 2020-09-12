import time
import random
import math

'''
This progam reads vectors from 2 files, converts them to lists of class instances to then find the a corresponding
value for the untrained vectors using a simplified k-nearest algorithm (1 for k) and modifies the data by erasing
one dimension. It prints the probatility of the correct prediction. Every step from reading the file to finding
the probality of the number of correct values gets messured by time.

This program will run with 15k trained and 1k untrained vectors around 7 * 40 seconds.
'''

class Vector:
    knearest = 1
    #initiates the vector. If no values are given, the vector array is empty and the value is -1.
    def __init__(self,vector,value = -1):
        self.vector = vector #sets the arrays as numpy array with the vector values
        self.value = value #value i.e. grass, trees, rock,...

    #Ditmar
    #computes the norm
    def euclidian_distance(self,point):
        distance = 0
        for vector_1,vector_2 in zip(self.vector,point.vector):
            distance += abs(vector_1-vector_2)

        return distance

    #Ditmar
    # determines the nearest vector and stores it with the value of the vector in an tuple
    def set_value(self,trained):
        distance = [(train.value,self.euclidian_distance(train)) for train in trained]
        distance.sort(key=lambda tup: tup[1]) #sorts the tuple
        self.value = distance[0][0] #sets the value to the nearest vector

#Ditmar
#converts file to a string of numbers
def file_to_string(name,numbervec):
    sstring = []

    file = open(name, "r")
    for line in file:
        #removes spaces and line break and stores it in A
        line = line.replace('\n','')
        sstring.append(line.replace('\t',''))

        #breaks if the numbervec is 0, so that only n vectors are taken from the file
        if type(numbervec)==int:
            numbervec -=1
            if numbervec<1:
                break
    file.close()

    return sstring

#Ditmar
#converts string to a list of instances of vectors
def string_to_list(sstring,non = False):
    vector_list = [] #list of class instances
    for line in sstring:
        number_list = []
        #converts line to list of numbers (vector)
        for i in line.split(' '):
            if len(i)==0:
                del i
            else:
                number_list.append(int(i))
        #converts list to class instance. If non is True (trained data)
        #the last list index becomes the value
        if non == True:
            vec = Vector(tuple(number_list[:-1]),number_list[-1])
        else:
            vec = Vector(tuple(number_list))
        vector_list.append(vec)
    return vector_list


#Eric
# converts seconds in (days, hours, minutes and seconds) a string
def convert(seconds):
    days = (seconds-seconds%24)/24
    seconds = seconds - days*24
    hour = (seconds-seconds%3600)/3600
    seconds = seconds - hour*3600
    minutes = (seconds-seconds%60)/60
    seconds = seconds - minutes*60
    return "%d:%02d:%02d:%02d" % (days,hour, minutes, seconds)


#Eric
def elimdim(data,dimension):
    for element in data:
        element.vector = element.vector[:dimension-1]+element.vector[dimension:]



#Eric
#creates a list with length n of random integers between 0 & leng,
# if n = leng, the random list is 0,1,...,n
def randomindexing(maximum,n):
    if maximum == n:
        a = [i for i in range(n)]
    else:
        a = [random.randint(0,maximum) for i in range(n)]
    return a



#Eric
#determines for all untrained data indexed by random_sequence the nearest value
def data_analysis(trained_data,untraind_data,random_sequence):
    t3 = time.time()
    [untraind_data[i].set_value(trained_data) for i in random_sequence]

    print("Time for indexing",len(random_sequence),"vectors:",round(time.time()-t3,3),"seconds")



#Eric
#determines the Percentag of correct values using 2 data sets and the random series
def datapercentage(original,data2,random_sequence):
    valid_counter = 0
    unvalid_counter = 0

    for i in random_sequence:
        if original[i].value == data2[i].value:
            valid_counter += 1
        else:
            unvalid_counter +=1
    print("Percentage of correct values:",valid_counter/(valid_counter+unvalid_counter))



print("Start")

number_of_vectors = 1000 #number of vectors
list_length = 8 # number-1 of trainedlist length

#random_sequence = randomindexing(indexrange,numberofelements)
random_sequence = randomindexing(number_of_vectors,number_of_vectors)


##############################################################

#converts the trained.txt to string
t0 = time.time()
trainedstring = file_to_string("trained.txt",'')
print("time for reading trained.txt",round(time.time()-t0,3),"seconds")

t0 = time.time()
#converts the untrained.txt to string
untrainedstring = file_to_string("untrained.txt",number_of_vectors)
print("time for reading untrained.txt",round(time.time()-t0,3),"seconds")
print("-----------------")


##############################################################


#creates list of lists of vectors and erases one dimension of the trained data
trainedlist = []
t1 = time.time()
for i in range(1,list_length):
    trainedlist.append(string_to_list(trainedstring,True))
    elimdim(trainedlist[i-1],i)
print("trained data, converting string to list",round(time.time()-t1,3),"seconds")

t1 = time.time()
#creates list of lists of vectors and erases one dimension of the untrained data
untrainedlist = []
for i in range(1,list_length):
    untrainedlist.append(string_to_list(untrainedstring))
    elimdim(untrainedlist[i-1],i)
print("untrained data,converting string to list",round(time.time()-t1,3),"seconds")
print("-----------------")


##############################################################


#Analysis the trained data to find the value of the untrained vectors
for i in range(len(untrainedlist)):
    print("Erased dimension",i+1)
    print("trained data points:",len(trainedlist[i]))
    print("untrained data points:",len(untrainedlist[i]))
    data_analysis(trainedlist[i],untrainedlist[i],random_sequence)
    print("-----------------")



##############################################################


#prints the percentage of correct vectors compared to the last list of vectors in the untrained list
#if the list has length 7, the last list of this list will have all 6 dimensions
for i in range(len(untrainedlist)):
    t2 = time.time()
    print("Erased dimension:",i+1)
    datapercentage(untrainedlist[-1],untrainedlist[i],random_sequence)
    print("time for percentage:",round(time.time()-t2,3),"seconds")
    print("-----------------")



print("Finish")
