#!/usr/bin/python3.1
# This program should be run with python 2.6, but it would work with any
# version after 2.5.  The reason it doesnt work with earlier versions is the
# "any" command, which could probably be replaced
#import urllib2 as url
#import datetime as dt
import csv 
import subprocess as sp
import datetime as dt

#outfiles = {}
#times = []
#a = csv.DictReader(open('output.csv','r'))
#for i in a.fieldnames:
    #if i != "date":
        #outfiles[i] = open(i + '.spc','w')
        #outfiles[i].writelines('series { title = \"' + i + '\"\n')
        #outfiles[i].writelines('\tdata = (\n')


#for line in a:
    #date = line['date']
    #times.append(date)
    #for field,v in line.items():
        
        #if field != "date":
            #outfiles[field].write('\t\t' + v + '\n')

#print(times)
#times.sort()
#startDate = times[1]
#endDate = times[len(times)-1]
#print(startDate)
#print(endDate)

outfile = open('women-output.csv','w')
outfile.write('Date,Value\n')
#for filename, file in outfiles.items():
    #file.writelines('\t\t)\n\tstart = ' + startDate + '}\nx11{}\n\n')
    #a = sp.call(['/home/jborowitz/bin/x12a/x12a', filename])
filename = '/home/jborowitz/python/women'
f = open(filename + '.out','r')
line = f.readline()
year = -1
finished = 0
while line.find('D 11') < 0:
    line = f.readline()
# Get up to section D 11, the final seasonally adjusted data
#while line.find('D 12') < 0:
    #while not line[0:5] = '------':
        #line = f.readline()
        # Get to the first headers of the table"
    #while not line[0:5] = '------':
        #months1 = line[6:-10].split()
        #months1 = line[6:-10].split()

    while not line[2:6].isdigit():
        line = f.readline()
    year = int(line[2:6])
    #print(year)
    yearStartDate = dt.date(year,1,1)
    d=[]
    while len(line) > 10:
        try:
            #d.append(float(line[6:21].strip()))
            #d.append(float(line[22:34].strip()))
            #d.append(float(line[35:47].strip()))
            #d.append(float(line[48:60].strip()))
            
            d.extend(line[6:-10].split())
            #d.append(float(line[6:18].strip()))
            #d.append(float(line[19:27].strip()))
            #d.append(float(line[28:36].strip()))
            #d.append(float(line[37:45].strip()))
            #d.append(float(line[46:54].strip()))
            #d.append(float(line[55:63].strip()))
            line = f.readline()
        except ValueError: 
            while line.find('D 12') < 0:
                #print(line)
                line = f.readline()
            #print(line)
            #finished = 1
            #print(line)
            #line = f.readline()
            break
    for index in range(len(d)):
        monthDate = dt.date(year,index+1,1)
        dstring = monthDate.strftime('%Y-%m')
        print(dstring)
        outfile.write(dstring + ',' + str(d[index]) + '\n')
    #line = f.readline()
    #print(line)
#print(line)
#line = f.readline()
