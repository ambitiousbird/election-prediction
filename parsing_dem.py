import csv
count=0
f=open('tweet_dem2text.txt','w')
with open('tweet_all.csv') as csvfile:
     #reader = csv.DictReader(csvfile)
     reader = csv.reader(csvfile)
     for row in reader:
         count=count+1
         try:
              string1=row[1].replace("RT", "")
              string2=string1.replace("https://t.co/","")
              #print(string2)
              f.write(string2)
         except UnicodeEncodeError:
              continue

print(count)
f.close()
