# Twitter-Bot
>*Motivation : Wanting to explore different APIs and see what I could build*
# Tech Used:
- Python 3.8
- Python Libraries: Tweepy 4.10, Requests 2.28
- Opensource API's: Openweather API, Twitter API (Elevated access)

# Setup and How to Run
1. Install the required Packages
```
pip install tweepy
pip install requests
```
2. Clone the repo into your local system
3. The Twitter API keys are linked to your Twitter Developer account so these are secret and cannot be made public. To make a clone of this bot create your own Dev account and store the following set of keys in your local >config.py
- consumer key (API key)
- consumer secret key (API secret key)
- access token
- access secret token
4. To use Openweather API, create an account and use the given API key. Store the key in `config.py` like above.
5. Create a .txt file where all the tweet_ids which have already been seen by the bot get stored. Mention the file name in `FILE_NAME` in `main.py`
6. From any twitter account, tweet the following
```
@bot_name -(cityname)
```
7. 

# Documentation
### What the bot does
This bot will give you the weather of a city that the user specifies. It follows a ***fixed syntax*** so adhereing to it will get you a reply from the bot or else it will be ignored.
>Syntax: @bot_name -(cityname)
### How it works


