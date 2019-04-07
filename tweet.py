
import tweepy

access_token = "1372259486-SjppHKngTYOE0yeCVKiIIMP5XnL4RyHqNx92YQV"
access_token_secret = "1Ee1KKaPtUixMI718ROVGKn26PZbdZTgStfVyVxYwZlVB"
consumer_key = "q1OjBG5T0DRk6g9mLkOuQfzXJ"
consumer_secret = "A5vbpHqa6iVmjiCC1JhWeqcPOjpxhGac4mwcO3e5zb6et4RCgc"

def OAuth():
	try:
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		return auth
	except Exception as e:
		return None

oauth = OAuth()
api = tweepy.API(oauth)

api.update_status('Hello Tis is Vigneshwar Ravichandran')