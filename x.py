#!/usr/bin/python2.6 
# This program should be run with python 2.6, but it would work with any
# version after 2.5.  The reason it doesnt work with earlier versions is the
# "any" command, which could probably be replaced
#import urllib2 as url
#import datetime as dt
import csv 
import subprocess as sp

outfiles = {}
times = []
a = csv.DictReader(open('lfp_malefemale.csv','rb'))
for i in a.fieldnames:
    if i != "date":
        outfiles[i] = open(i + '.spc','w')
        outfiles[i].writelines('series { title = \"' + i + '\"\n')
        outfiles[i].writelines('\tdata = (\n')


for line in a:
    date = line['date']
    times.append(date)
    for field,v in line.items():        
        if field != "date":
            outfiles[field].write('\t\t' + v + '\n')

print(times)
times.sort()
startDate = times[1]
endDate = times[len(times)-1]
print(startDate)
print(endDate)

for filename, file in outfiles.items():
    file.writelines('\t\t)\n\tstart = ' + startDate + '}\nx11{}\n\n')
    #a = sp.call(['/home/jborowitz/bin/x12a/x12a', filename])
    

    


#for i,j in outfiles.items():
    #print(i)
    #print(j)
#def fred(series_id): 
    #api_key = 'f778a39f92e4e71d27b54ca4b613c28f'
    #site_stub = 'http://api.stlouisfed.org/fred/'
    ##series_id = 'GNPCA'
    #realtime = '&realtime_start=1776-07-04&realtime_end=9999-12-31'
    #file = series_id + '.csv'
    #csvwriter = csv.writer(open(file, 'wb'), dialect = 'excel')
    ##series_id = 'MTUR'
    #start = '1776-07-04'
    #end = '9999-12-31'
    #url_string = (site_stub + 'series/observations?' + 'series_id=' + series_id +
                 #realtime + '&api_key=' + api_key)
    #print('Downloading from: ' + url_string)
    #U = url.urlopen(url_string)
    ##year = []
    ##month = [] #day = []
    #dates = []
    #startdates = []
    #enddates = []
    #value = []
    #U.readline
    #csvwriter.writerow(['Year', 'Month', 'Day','Date',
        #'Start_Year','Start_Month','Start_Day','Start_Date','End_Year','End_Month','End_Day', 'End_Date', series_id])
    #for u in U.readlines():
        #print(u)
        #elements=u.strip().split(' ')
        #if any((elements[0].find('xml') >= 0, elements[0].find('observations') >= 0,
                #len(elements) <= 1)) : continue
        #obs, rt_start, rt_end, date, val = u.strip().split(' ')
        #y, m, d = date.split('\"')[1].split('-')
        #date = dt.datetime(int(y), int(m), int(d))
        #rtsy, rtsm, rtsd = rt_start.split('\"')[1].split('-')
        #rtsdate = dt.datetime(int(rtsy), int(rtsm), int(rtsd))
        #rtey, rtem, rted = rt_end.split('\"')[1].split('-')
        #rtedate = dt.datetime(int(rtey), int(rtem), int(rted))
        #dates.append(date)
        #startdates.append(rtsdate)
        #enddates.append(rtedate)
        #value.append(val.split('\"')[1])
        #csvwriter.writerow([y, m, d, date, rtsy, rtsm, rtsd, rtsdate, rtey, rtem, rted, rtedate, val.split('\"')[1]])
    #return dates, value, startdates, enddates

#m = fred('USPRIV')
#The function fred returns the history of published parameter values from
#ALFRED.  It also writes a csv file to series_id.csv
