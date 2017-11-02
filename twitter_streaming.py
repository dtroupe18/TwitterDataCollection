from tweepy.streaming import StreamListener
from tweepy import Stream
import constants
# This is a basic listener that just prints received tweets


class PrintTwitterStream(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # This handles Twitter authentication and the connection to Twitter Streaming API
    l = PrintTwitterStream()
    stream = Stream(constants.auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'trump', 'russia', 'clinton'
    stream.filter(track=['trump', 'russia', 'clinton'])