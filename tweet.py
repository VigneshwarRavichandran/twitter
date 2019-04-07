
import tweepy
from security import Secure
from config import Validate


def auth():
	try:
		tweet = Secure()
		auth = tweepy.OAuthHandler(tweet.get_consumer_key(), tweet.get_consumer_secret())
		auth.set_access_token(tweet.get_access_token(), tweet.get_access_token_secret())
		return auth
	except Exception as e:
		return None

oauth = auth()
api = tweepy.API(oauth)
msg = "hello Tis is Vigneshwar Ravichandran hai"
validate = Validate() 
result = validate.check(msg)
if(result):
	api.update_status(result)
else:
	print("Use appropriate words")
	