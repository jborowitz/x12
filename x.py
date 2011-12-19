#!/usr/bin/python2.6 
#import urllib2 as url
#import datetime as dt
import csv, os, subprocess, sys, time
from datetime import datetime
import datetime as dt

outfiles = {}
times = []
a = csv.DictReader(open(sys.argv[1],'rb'))
for i in a.fieldnames:
    if i != "date":
        outfiles[i] = open(i + '.spc','w')
        outfiles[i].writelines('series { title = \"' + i + '\"\n')
        outfiles[i].writelines('\tdata = (\n')


for line in a:
    date = datetime.strptime(line['date'],'%Y-%m')
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
    file.writelines('\t\t)\n\tstart = ' + startDate + '\n\tdecimals = 2}\nx11{}\n\n')
    file.close()
    subprocess.call(['/home/jborowitz/bin/x12a/x12a',filename])


for filestub in outfiles.iterkeys():
    x12out = open(filestub + '.out','r')
    line = x12out.readline()
    year = -1
    outputcsv = open(filestub + '.csv','w')
    outputcsv.write('date,' + filestub + '\n')
    while line.find('D 11') < 0:
        line = x12out.readline()
        #print(line)

    while year < maxyear:
        while not line[2:6].isdigit():
            line = x12out.readline()
        year = int(line[2:6])
        d=[]
        while len(line) > 10:
            st = line[9:66].split()
            d.extend(st)
            line = x12out.readline()
        for index in range(len(d)):
            if year < maxyear:
                monthDate = dt.date(year,index + 13 - len(d),1)
            else:
                monthDate = dt.date(year,index + 1,1)
            dstring = monthDate.strftime('%Y-%m')
            outputcsv.write(dstring + ',' + str(d[index]) + '\n')
