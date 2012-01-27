#!/usr/bin/python3.1
#import urllib2 as url
#import datetime as dt
import csv, os, subprocess, sys, time
from datetime import datetime
import datetime as dt

spc1="series {\n\t title = \""
spc2="\n\tdecimals=2\n\tdata = (\n"
spc3="\t\t)\n\tstart = "
#spc2="\n\tperiod = 12\n\tstart = "
spc4= "\n\t}\nx11{}"
 
if len(sys.argv) <= 2:
    outname = sys.argv[1].split('.')[0] + '-out.csv'
else:
    outname = sys.argv[2]
outfiles = {}
times = []
a = csv.DictReader(open(sys.argv[1],'r'))
for i in list(a.fieldnames):
    if i != "date":
        outfiles[i] = open(i + '.spc','w')
        outfiles[i].writelines(spc1 + i + '\"\n')
        outfiles[i].writelines(spc2)


for line in a:
    date = datetime.strptime(line['date'],'%b-%Y')
    times.append(date)
    for field,v in line.items():        
        if field != "date":
            outfiles[field].write('\t\t' + v + '\n')

times.sort()
startDate = times[0].strftime('%Y.%m')
endDate = times[len(times)-1]
maxyear = endDate.year
print(maxyear)

for filename, file in outfiles.items():
    file.writelines(spc3 + startDate + spc4)
    #file.writelines('\t\t)\n\tstart = ' + startDate + '\n\tdecimals = 4}\nx11{}\n\n')
    file.close()
    subprocess.call(['/home/jborowitz/bin/x12a/x12a',filename])


headdict={'date':'date'}
for i in outfiles.keys():
    headdict[i + 'sa'] = i + 'sa'
allout = csv.DictWriter(open(outname,'w'),headdict.keys())
allout.writerow( headdict)
outvars = {}
for filestub in outfiles.keys():
    print(filestub)
    x12out = open(filestub + '.out','r')
    line = x12out.readline()
    year = -1
    outputcsv = open(filestub + '.csv','w')
    outputcsv.write('date,' + filestub + '\n')
    while line.find('D 11') < 0:
        line = x12out.readline()

    outvars[filestub]=[]
    while year < maxyear:
        while not line[2:6].isdigit():
            line = x12out.readline()
        year = int(line[2:6])
        yearout=[]
        while len(line) > 10:
            st = line[9:64].split()
            outvars[filestub].extend(st)
            yearout.extend(st)
            line = x12out.readline()
        for index in range(len(yearout)):
            if year < maxyear:
                monthDate = dt.date(year,index + 13 - len(yearout),1)
            else:
                monthDate = dt.date(year,index + 1,1)
            dstring = monthDate.strftime('%Y-%m-%d')
            outputcsv.write(dstring + ',' + str(yearout[index]) + '\n')
    outputcsv.close()
for j in range(len(times)):
    row = {}
    row['date']=times[j].strftime('%Y-%m-%d')
    for i in outfiles.keys():
        row[i+'sa']=outvars[i][j]
    allout.writerow(row)
