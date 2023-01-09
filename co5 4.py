import csv
#specifying the columns indices u wanna read

col2read=[0,1,-1]   #(1 symbolises last column)
#opening the csv file and reading contents

with open('cars.csv','r')as x:
    reader=csv.reader(x)

    #Iterate over the rows of the CSV
    for row in reader:
        #Print the specified indices of the specified columns
        print([row[i] for i in col2read])
