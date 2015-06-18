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
auth = OAuthHandler(authe.consumer_key, authe.consumer_secret)
auth.set_access_token(authe.access_token, authe.access_token_secret)
stream = Stream(auth, l)

stream.filter(track=['studypool', 'eduboard','chegg', 'tutoring'])