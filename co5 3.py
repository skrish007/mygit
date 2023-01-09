import csv
#Open the csv file
with open('cars.csv','r') as file:
    #Creating a csv reader
    reader=csv.reader(file)

#Iterate over the rows of csv file
    for row in reader:
        print(row)