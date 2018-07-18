import tweepy
import csv
import time
import pymysql
# datebase connection 
conn = pymysql.connect(host='cis-linux2.temple.edu',  user='tuf68743', passwd='ohogoofu', db='FA15_5015_tuf68743')
cur = conn.cursor()

# Consumer keys and access tokens, used for OAuth----------tweepy intial
consumer_key = 'd6ny2hN8tby3gX6qAjMmAICuq'
consumer_secret = 'Ff4NG8aIbPbOnN7HrrX1sTAfGVEwVX40dDle0Ovx0vSOZVvgzw'
access_token = '2768297009-j2oBCLtuWq8XBxGUPn45rnO6siW7gLiw2M9Qi9D'
access_token_secret = 'qJDzeOMmciw2RBaASoWAvjQ2bSqPh7W5pmRA71yYAHjSf'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#qurey start 
places = api.geo_search(query="USA", granularity="country")
place_id = places[0].id
print(place_id)
qurey0="place:%s" % place_id
count=0
c= tweepy.Cursor(api.search,
	q=qurey0,
	since="2015-11-11",
	until="2015-12-11",
        #geocode="40.199117, -96.292006,100km",
	lang="en").items()
csvFile = open('tweet_all.csv', 'a')
csvwriter = csv.writer(csvFile)
while True:
    try:
        tweet = c.next()
	
	if (tweet.geo !=None):
		print (tweet.geo['coordinates'])
		count=count+1
        	csvwriter.writerow([tweet.created_at,tweet.text.encode('utf-8'),tweet.geo['coordinates']])
		tweet_string=tweet.text.encode('utf-8')
		lat=tweet.geo['coordinates'][0]
		log=tweet.geo['coordinates'][1]
		cur.execute("INSERT INTO Tweets(Text,Lat,Lon) VALUES (%s,%s,%s);",(tweet_string,lat,log))
		conn.commit()
                cur.execute("INSERT INTO Tweets2(Text,Lat,Lon) VALUES (%s,%s,%s);",(tweet_string,lat,log))
                conn.commit()
		if (count>50):
			cur.close()
			break
    except tweepy.TweepError:
        print("sleeping .....")
        time.sleep(60 * 15)
        continue
    except StopIteration:
        break

