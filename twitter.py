import tweepy
import time 

auth = tweepy.OAuthHandler('4THPjvTQau3r3DizFKllxFt9L', 's1l7E1OW47SWDpl7utEyiXkSoAdtZYlG166WPCB901tZTX0df0')
auth.set_access_token('1487423447504498688-yj6SfMZtWaLgAOCy65swxTxE4m88T7', 'cnVQz7OpzkVyusglH78sPm7uUtGKnbG2UD8mV55gcwEJ9')

api = tweepy.API(auth, wait_on_rate_limit=True)


# user = api.get_user(screen_name='elainelokeee')
# userID = user.id 


# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#     print(friend.screen_name)

search = 'Shawn Mendes'
nrTweets = 10

for tweet in tweepy.Cursor(api.search_tweets, search).items(nrTweets):
    try: 
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    # except tweepy.TweepyException as e:
    #     print(e.__cause__)
    except StopIteration:
        break