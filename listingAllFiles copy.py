#!/usr/bin/python
# https://www.tutorialspoint.com/python/os_listdir.htm
# Got the listing code from here
import os
import sys
import time

# Open a file
pathToFile = "zips"
dirs = os.listdir(pathToFile)



# This would print all the files and directories
for edhFile in dirs:
    #print(edhFile)
    # https://www.pythontutorial.net/python-basics/python-read-text-file/
    # Got the code from here.
    print(edhFile)
    with open("zips/" + edhFile) as fileToRead:
        contentsOfFile = fileToRead.read()

        # print(contents)

    # https://www.w3schools.com/python/python_file_write.asp
    # Writing contents to file from here
        fileToRead = open("text.txt", "a")

        getDateStep1 = edhFile.split(".")
        getDateStep2 = getDateStep1[0]
        fileDateNumbers = list(getDateStep2)
        dd = fileDateNumbers[6]+""+fileDateNumbers[7]
        mm = fileDateNumbers[4]+""+fileDateNumbers[5]
        yyyy = fileDateNumbers[0]+""+fileDateNumbers[1] + \
            ""+fileDateNumbers[2]+""+fileDateNumbers[3]

        indvLinesOfFileArray = contentsOfFile.splitlines()

        for indvLine in indvLinesOfFileArray:
            #print(indvLine)
            if "*" in indvLine:
                fileToRead.write(indvLine+'\n')

            elif not indvLine:
                fileToRead.write(indvLine+'\n')
            else:
                fileToRead.write(dd+"-"+mm+"-"+yyyy+" "+indvLine+"\n")
        # f.write(contents)
        fileToRead.close()


original_file = "text.txt"
temp_file = "sample.txt"


string_to_delete = ["*************************************************************************",          "*                                                                       *",
                    "*    Software and Parameter file copyright InvestorData (Pty) Ltd 2021  *", "*    All JSE originated data copyright JSE (Pty) Ltd                    *", "*    Report piracy to BSA          on (080) 011-0447 OR                 *", "*                     Mike Jenkins on (082) 785-1977                    *",  "*    and receive a reward of up to R25,000 for a conviction !           *"]
with open(original_file, "r") as input:
    with open(temp_file, "w") as output:
        for line in input:
            for word in string_to_delete:
                line = line.replace(word, "")
            output.write(line)
# replace file with original name
os.replace('sample.txt', 'text.txt')


with open('text.txt', 'r') as fileRead:
    with open('test.txt', 'w') as fileWrite:
        for line in fileRead:
            line = line.strip()
            if line:
                fileWrite.write(line)
                fileWrite.write('\n')
