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
The execution done based on the flag value:
1. If flag is True
```
The inappropriate words are replaced as xxx.
```

2. If flag is False
```
The tweet is not posted
```