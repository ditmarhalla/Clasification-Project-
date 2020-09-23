#File Conversion
def file_to_list(name):
    vector = []
    file = open(name,  "r")
    for line in file:
        line = list(line.split())
        vector.append(line)
    file.close()
    return vector

##################################################
# Calculating the distance

def euclidian_distance(vector1, vector2):   # The two vectors we want to compare
    value = 0                               # we start the variable to calculate the sum 
    for i in range(len(vector1)):           # The loop will run till the length of vector 1
        value += abs(int(vector1[i]) - int(vector2[i]))  # distance calculation
    return value
##############################################
# Calculating the untrained vectors class

def neighbor(traned_data,  untrained_vector):
    distnace_vector = []
    the_class = []
    for vectors in traned_data:
        distnace = euclidian_distance(vectors[0:5], untrained_vector)   #here we run the fuction to calculate the distance of all the vectors in the trained dataset with one vector that we define
        distnace_vector.append((distnace,vectors[6]))
    min_val = distnace_vector[0]
    for i in range(len (distnace_vector)):
        if min_val[0] > (distnace_vector[i][0]):
            min_val = distnace_vector[i]
    print(untrained_vector)
    untrained_vector.append(min_val[1])
    return untrained_vector


# test run with some data
dataset = file_to_list("trained.txt")
v = ['50', '31', '13', '48', '22', '23']
print("The class is:"(neighbor(dataset,v)))
