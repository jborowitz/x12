#!/usr/bin/python2.6 
#import urllib2 as url
#import datetime as dt
import csv, os, subprocess, sys, time
from datetime import datetime

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
startDate = times[1].strftime('%Y.%m')
endDate = times[len(times)-1]

for filename, file in outfiles.items():
    file.writelines('\t\t)\n\tstart = ' + startDate + '}\nx11{}\n\n')
    #string = ['/home/jborowitz/bin/x12a/x12a' , filename]
    string = 'nohup /home/jborowitz/bin/x12a/x12a ' + filename + ' &'
    print(string)
    #a = subprocess.Popen(string)
    #a.communicate()
    a = subprocess.Popen(string,shell=True)
    #a = subprocess.call(string)
    
    #a.wait()
    #a.wait()
    #print(a.returncode)
    #a.terminate()
    #while a.poll() is None:
    #time.sleep(3)
        #print(time.time())
    #a.wait()
    #a.communicate() #will not pass this line until the process above terminates

    #a = sp.call(['/home/jborowitz/bin/x12a/x12a', filename])
    #a = sp.call(string, shell=True)
    #print(a)
    
