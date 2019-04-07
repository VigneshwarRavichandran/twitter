
import tweepy
from security import Secure


def OAuth():
	try:
		tweet = Secure()
		auth = tweepy.OAuthHandler(tweet.get_consumer_key(), tweet.get_consumer_secret())
		auth.set_access_token(tweet.get_access_token(), tweet.get_access_token_secret())
		return auth
	except Exception as e:
		return None

oauth = OAuth()
api = tweepy.API(oauth)
api.update_status('Hello Tis is Vigneshwar Ravichandran')