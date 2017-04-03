import scraperwiki
import csv
data = scraperwiki.scrape('https://data.birmingham.gov.uk/dataset/14492d37-1a77-4d46-9204-27363fc62149/resource/bacf38dd-3530-4c95-a0c3-83e21c9b2259/download/sgmsreportsvcsfreportsvcsfreports201415vcsfreport2014qtr1final.csv')

reader = csv.DictReader(data.splitlines())

record = {}

for row in reader:
    print "Row item 3:", row[' Invoice Amount '][2:]
    for num in range(0,8):
        print "column %d : " % num, type(row.keys()[num]) 
    row[' Invoice Amount '] = row[' Invoice Amount '][2:]
    print row['Doc Number']
    scraperwiki.sqlite.save(['Doc Number'], row)
