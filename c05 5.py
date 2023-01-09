import csv

file=[{'Name':'Polo GT','Colour' : 'Red', 'Year':2022},
{'Name':'BAleno','Colour' : 'Black', 'Year':2014},
{'Name':'Swift','Colour' : 'White', 'Year':2020}]
#Write csv
with open('films.csv','w') as csvfile:
    hnames=['Name','Colour','Year']
    x = csv.DictWriter(csvfile, fieldnames=hnames)
    x.writeheader()
    for row in file:
        x.writerow(row)

# Read from CSV file and print contents
with open('films.csv', 'r') as csvfile:
    y = csv.DictReader(csvfile)
    for row in y:
        print(row)