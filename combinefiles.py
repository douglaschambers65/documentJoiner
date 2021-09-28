#!/usr/bin/python
#----------------------------------------------------------------------------
# Created By  : Douglas Chambers   
# Created Date: 27/09/2021
# version ='1.0'
# ---------------------------------------------------------------------------
# ShareFinder 5 (sharefinderpro.com) imports daily stock market data from investordata.co.za.
# The data is provided in the form of a zip file. Inside the zip are normally two files, 
# namely yyyymmdd.edh and yyyymmdd.edd . 
# .edh contains changes to the stock market symbols and names of companies.
# .edd contains changes and additions to the stock market prices and other data for each symbol.
# ---------------------------------------------------------------------------
# Here, individual .edh files containing symbol change data are compiled into one large flat text file.

import os

# Create a list of all .edh files in the folder "edhfiles"
pathToFiles = "edhfiles"
edhfiles = os.listdir(pathToFiles)

#Open the output file and wipe it
outputFile = open("output.txt", "a")
outputFile.truncate(0)

# This would print all the .edh files in the edhfiles directory.
for edhFile in edhfiles:
    print(edhFile)

    with open(pathToFiles + "/" + edhFile) as fileToRead:
        
        contentsOfFile = fileToRead.read()
        individualLinesOfFile = contentsOfFile.splitlines()

        #The file is named yyyymmdd.edh . Extract the time periods with a substring.
        year = edhFile[0:4]
        month = edhFile[4:6]
        day = edhFile[6:8]
        
        for individualLine in individualLinesOfFile:
            
            #Don't include the line in the output if it contains no text or starts with an asterisk *
            if not individualLine:
                continue
            elif "*" in individualLine[0]:
                continue
            else:
                outputFile.write(day+"-"+month+"-"+year+" "+individualLine+"\n")
        
outputFile.close()


# ORIGINAL CODE MARKED FOR REMOVAL
# original_file = "text.txt"
# temp_file = "sample.txt"


# string_to_delete = ["*************************************************************************",          "*                                                                       *",
#                     "*    Software and Parameter file copyright InvestorData (Pty) Ltd 2021  *", "*    All JSE originated data copyright JSE (Pty) Ltd                    *", "*    Report piracy to BSA          on (080) 011-0447 OR                 *", "*                     Mike Jenkins on (082) 785-1977                    *",  "*    and receive a reward of up to R25,000 for a conviction !           *","*    Software and Parameter file copyright InvestorData (Pty) Ltd 2019  *"]
# with open(original_file, "r") as input:
#     with open(temp_file, "w") as output:
#         for line in input:
#             for word in string_to_delete:
#                 line = line.replace(word, "")
#             output.write(line)
# # replace file with original name
# os.replace('sample.txt', 'text.txt')


# with open('text.txt', 'r') as fileRead:
#     with open('test.txt', 'w') as fileWrite:
#         for line in fileRead:
#             line = line.strip()
#             if line:
#                 fileWrite.write(line)
#                 fileWrite.write('\n')
