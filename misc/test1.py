import tweepy
import config
import x
import requests, json

FILE_NAME = 'latest.txt'

consumer_key = config.API_KEY
consumer_secret = config.API_SECRET
access_token = config.ACCESS_TOKEN
access_secret = config.ACCESS_SECRET

api_weather = 'bee52814dff08c1d5fd02e22f95b778c'
weather_url = "http://api.openweathermap.org/data/2.5/weather?"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)



def execute():

    mentions = api.mentions_timeline()

    for mention in (mentions):
        #if x.has_replied(FILE_NAME, mention.id):
           # continue

        lst = mention.text.split('-')

        if len(lst) != 2 or x.has_replied(FILE_NAME, mention.id):
            continue
        
        city = lst[1]

        complete_url = weather_url + 'appid=' + api_weather + '&q=' + city
        response = requests.get(complete_url)

        data = response.json()

        if data['cod'] != '404':
            req_data = data['main']

            temperature_k = req_data['temp']
            humidity = req_data['humidity']
            sky = data['weather'][0]['main']
            descp = data['weather'][0]['description']
            try:
                api.update_status('\nToday in ' + str(city) + ',' + '\nTemperature = ' + str(round(temperature_k - 273.15)) +  ' \u00B0' +'C' + '\nSky = ' + str(sky) + '\nHumidity = ' + str(humidity) + ' %' + '\nDescription = ' + str(descp) + '\nHave a nice day!', in_reply_to_status_id = mention.id)
                x.add_id(FILE_NAME, mention.id)
            except:
                print('This has been tweeted recently so cool down time')
    

execute()