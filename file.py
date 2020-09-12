def file_to_list(name):
    vector = []                                  # create an empty list that we need in line 10 to append the vectors
    count = 0                               # define the variable count that we need in line 7
    file = open(name,  "r")                  # open the file in read form
    for i,  line in enumerate(file):         # i - the number of lines we want to convert
        if i <10:                           # define the number of lines
            count += 1                      # this is a counter of how many times the program runs. As a result counts the number of lines
            line = line.strip("\n")         # removes enters
            line = line.strip("\t")         # removes extra spaces (Usualy after the 6th variable)
            #line = int(line) ask Mr.Ibrahim why this does not work
            vector.append(line.split())          # after it is done we inseart all the lists into the list called "A"
        else:                               # this brakes the loop after i is no longer smaller then the specified times we want the program to run
            break
    file.close()
    print ("The number of vectors converted is ",  count) # checks if we have the correct number of vectors
    return vector
########################################

# Calculating the distance
def euclidian_distance(vector1,  vector2):   # should take 2 values
    value = 0                               # define the variable
    for i in range(len(vector1)):           # the for loop will run for the distnace of vector1 so 6 times
        value += (vector1[i] - vector2[i])  # this will calculate the distance
    return value


##############################################

def neighbor(trained_data,  untrained_vector):
    distance_vector = []
    for vectors in trained_data:
        distance = euclidian_distance(vectors[0:6], untrained_vector)   #here we run the fuction to calculate the distance of all the vectors in the trained dataset with one vector that we define
        distance_vector.append([vectors,  [distance]])
        nearest = []
        #print("Sorted vectors" , distnace_vector)
    for i in range (1):  # the number of neighbors that we will append # we just need one vector that is enough
        nearest.append(distance_vector)
    #print("This are the 3 nearest vectors",  nearest)
    return nearest

################################################


# we run a test to see if the fuctions work together

dataset = [[1,  4,  5,  62,  34,  54,  1], [1, 34, 5, 72, 34, 23, 2], [21, 64, 5, 81, 34, 98, 5], [4, 64, 57, 34, 34, 54, 6], [16, 41, 55, 12, 45, 43, 11], [21, 45, 56, 12, 76, 12, 3]]
v=[1, 4, 5, 62, 34, 54]
print(neighbor(dataset,v))
