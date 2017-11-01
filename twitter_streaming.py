# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains the user credentials to access Twitter API
access_token = "974217668-Dishu2YGNKL0ojsyZhdz2HLzqgVE3yIGFWCm40pt"
access_token_secret = "zC4FccmKS1u7GRfs1S7bisWgWLXcxMeKY87ZN01T0mAbS"
consumer_key = "jk2HV3gzk62PvJbfzdNvJgBD8"
consumer_secret = "7HTz9u2LqlEXBNKToaafO552vmKnX956Z0Odh8UoT9HJ1zV4R0"


# This is a basic listener that just prints received tweets to stdout.

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'trump', 'russia', 'clinton'
    stream.filter(track=['trump', 'russia', 'clinton'])