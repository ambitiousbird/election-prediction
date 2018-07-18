import tweepy
import json
import pymysql

conn = pymysql.connect(
    db='FA15_5015_tuf68743',
    user='tuf68743',
    passwd='ohogoofu',
    host='cis-linux2.temple.edu')
c = conn.cursor()

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'd6ny2hN8tby3gX6qAjMmAICuq'
consumer_secret = 'Ff4NG8aIbPbOnN7HrrX1sTAfGVEwVX40dDle0Ovx0vSOZVvgzw'
access_token = '2768297009-j2oBCLtuWq8XBxGUPn45rnO6siW7gLiw2M9Qi9D'
access_token_secret = 'qJDzeOMmciw2RBaASoWAvjQ2bSqPh7W5pmRA71yYAHjSf'

# This is the listener, responsible for receiving data
class StdOutListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(StdOutListener, self).__init__()
        self.num_tweets = 1

    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        tweet = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
	#if tweet['coordinates']:
	#    print '***Coords:', tweet['coordinates'] 
        c.execute("INSERT INTO Tweets(ScreenName, Text) values ('" +\
	    tweet['user'] ['screen_name']+"','')")
	#    "')")
	conn.commit()
	print '@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore'))
        print ''
	if self.num_tweets <50:
 	    self.num_tweets +=1
	else:
	    return False

    def on_error(self, status):
        print status
	return False


if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "Showing all new tweets for #election:"

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l, timeout=None, compression=False)
    stream.filter(track=['election','Clinton'])
