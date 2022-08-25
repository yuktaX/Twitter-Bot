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
7. Bot will reply to the tweet with a brief description of the weather

# Documentation
### What the bot does
This bot will give you the weather of a city that the user specifies. It follows a ***fixed syntax*** so adhereing to it will get you a reply from the bot or else it will be ignored.
>Syntax: @bot_name -(cityname)
### How it works
We are using 2 APIs here, Twitter and Openweather. 
- Once we authenticate the Twitter API, we can send and recieve tweet requests and responses.
- Fetch the mentions time line of the bot
- Scan the tweet and get the city name
- Using Weather API, send request for data and get response
- Update user_status i.e reply to the tweet
There is an overall communication between user, Twitter API and Openweather API through exchange of response and requests.

### Code



