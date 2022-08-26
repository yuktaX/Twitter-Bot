import tweepy       #importing needed libraries and modules
import config       #API key file
import manage_tweets
import requests, json

FILE_NAME = 'latest.txt'  #file stores all the tweet ids which have

consumer_key = config.API_KEY
consumer_secret = config.API_SECRET
access_token = config.ACCESS_TOKEN
access_secret = config.ACCESS_SECRET

api_weather = config.WEATHER_API
weather_url = "http://api.openweathermap.org/data/2.5/weather?"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #authorise API keys 
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth) #API object used to access twt API


def execute():

    mentions = api.mentions_timeline()  #fetching all mentions of the bot from timeline

    for mention in (mentions):
        if manage_tweets.has_replied(FILE_NAME, mention.id) == True:  #do nothing if bot has already replied to a tweet
            continue

        tweet = mention.text.split('-')

        if len(tweet) != 2:  #checking syntax, if not correct do nothing
            #print('Invalid tweet syntax')
            continue
        
        city = tweet[1]

        complete_url = weather_url + 'appid=' + api_weather + '&q=' + city  #sending request to weather API
        response = requests.get(complete_url)

        data = response.json() #fetching response from url
        #print(data)

        if data['cod'] != '404':  #if code is not an error
            req_data = data['main']

            temperature_k = req_data['temp']  #fetching required data to display
            humidity = req_data['humidity']
            sky = data['weather'][0]['main']
            descp = data['weather'][0]['description']
            try:
                api.update_status('\nToday in ' + str(city).capitalize() + ',' + '\nTemperature = ' + str(round(temperature_k - 273.15)) +  ' \u00B0' +'C' + '\nSky = ' + str(sky) + '\nDescription = ' + str(descp) + '\nHumidity = ' + str(humidity) + ' %' '\nHave a nice day!', in_reply_to_status_id = mention.id, auto_populate_reply_metadata = True)
                manage_tweets.add_id(FILE_NAME, mention.id)  #adding tweet_id to list of replied tweets so we dont reply to it again
                print('sucessfully replied')
            except:
                print('This has been tweeted recently---cool down time') #to avoid error 403, repeated tweet within few seconds
        
        if data['cod'] == '404':
            try:
                api.update_status('Sorry, city was not found',in_reply_to_status_id = mention.id, auto_populate_reply_metadata = True)
                manage_tweets.add_id(FILE_NAME, mention.id)
            except:
                print('This has been tweeted recently---cool down time')

execute() #run code to reply to any new tweets