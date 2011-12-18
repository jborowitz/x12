#!/usr/bin/python3.1
# This program should be run with python 2.6, but it would work with any
# version after 2.5.  The reason it doesnt work with earlier versions is the
# "any" command, which could probably be replaced
#import urllib2 as url
#import datetime as dt
import csv 
import datetime 
import sys

maxyear = 2011
outfile = open(sys.argv[2],'w')
outfile.write('Date,' + sys.argv[2].split('.')[0] + '\n')
filename = sys.argv[1]
f = open(filename,'r')
line = f.readline()
year = -1
finished = 0
while line.find('D 11') < 0:
    line = f.readline()
# Get up to section D 11, the final seasonally adjusted data
while year < maxyear:
    while not line[2:6].isdigit():
        line = f.readline()
    year = int(line[2:6])
    d=[]
    while len(line) > 10:
        st = line[9:66].split()
        d.extend(st)
        line = f.readline()
    for index in range(len(d)):
        monthDate = datetime.date(year,index + 13 - len(d),1)
        dstring = monthDate.strftime('%Y-%m')
        outfile.write(dstring + ',' + str(d[index]) + '\n')
