# Tweet

This is solution for posting tweet with filtering some set of words.

## Installation
Programming Logic requires python3.

This install all the necessary dependancies:
```
$ pip install -r requirements.txt
```


## Get Started

#### To send tweet run the ``tweet.py`` file

If the tweet contains inappropriate text as mention in the set of words.``config.py``

1. If there is no inappropriate words in the message:
```
The tweet is posted as it is.
```

2. If there is inappropriate words in the message:

The execution done based on the flag value:

	a. If flag is True
```
	The inappropriate words are replaced as xxx.
```

	b. If flag is False
```
	The tweet is not posted
```