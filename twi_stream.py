from tweepy.streaming import StreamListener
from tweepy  import   OAuthHandler
from tweepy  import Stream
import authe


class StdOutListener(StreamListener):
    
    def on_data(self, data):
        print data
        return True
    
    def on_error(self, status):
        print status
        

l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)

stream.filter(track=['studypool', 'eduboard', 'tutoring'])