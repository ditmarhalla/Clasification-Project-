# Clasification-Project

Python project intended as an introduction into machine learning and classification (Part of the University Curuculum)


In this classification we have an array of data. Each array is composed by 7 numbers in the trained.txt dataset and by 6 numbers in the untrained.txt dataset. In the trained dataset we have 15 000 array and in the untrained one we have 3.4 million array. Using python we have to classify the untrained data using the trained data that we have and calculate the 7th value which is the classification of the array.

In the first iteration I used the python intgrated methods and alos only using functions. To convert the file takes very little time, around 1.0 secons.
But when we try and classify the untraind vectors than we see the problem. It takes 47.9 secons just to classify 1000 untrained vectors.
That is why we define a fuction that removes the same value from each vector and also check that the accuracy is still intact. This will make the program run faster as it has less calculations

Then we implement the NumPy library. This makes the program run much faster. So fast that we dont need to remove any dimanesions. But we see that loading all the array of 3.4 million takes a long time. Around 11 seconds. But that is not a problem since the calculation is so fast that it shows up as 0.0 seconds.


