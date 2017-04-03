import scraperwiki
import csv
data = scraperwiki.scrape('https://data.birmingham.gov.uk/dataset/14492d37-1a77-4d46-9204-27363fc62149/resource/bacf38dd-3530-4c95-a0c3-83e21c9b2259/download/sgmsreportsvcsfreportsvcsfreports201415vcsfreport2014qtr1final.csv')

reader = csv.DictReader(data.splitlines())
for key, value in reader.items():
    print key

for row in reader:
    print row["Annual Total 2012/2013"]
    print "Row item 3:", row['Actual Funding Award'][2:]
    for num in range(0,8):
        print "column %d : " % num, type(row.keys()[num]) 
    row['Actual Funding Award'] = row['Actual Funding Award'].decode("latin-1")
    row['Annual Total 2012/2013'] = row['Annual Total 2012/2013'].decode("latin-1")
    row['Annual Total 2013/2014'] = row['Annual Total 2013/2014'].decode("latin-1")
    row['Annual Total 2014/2015'] = row['Annual Total 2014/2015'].decode("latin-1")
    row['Overall Total Paid'] = row['Overall Total Paid'].decode("latin-1")
    print row['Ref. No.']
    scraperwiki.sqlite.save(['Ref. No.'], row)
