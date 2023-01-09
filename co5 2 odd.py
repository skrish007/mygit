#Program to copy odd lines of one file to another

#Open files to read and write

inputfile=open('score.txt')
outputfile=open('newscore.txt','w')

#Copying contents to new file
copyfile=inputfile.readlines()
print("\n Original File Content :\n")
print(copyfile)

for i in range(0,len(copyfile )):
    if i%2 == 0:
        outputfile.write(copyfile[i])
    else:
        pass

#Closing file after operation
outputfile.close()

#Opening write file in read mode and printing values

outputfile=open('newscore.txt','r')
print("Odd lines are:\n",outputfile.read())

#Closing files
inputfile.close()
outputfile.close()


