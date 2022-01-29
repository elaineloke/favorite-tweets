import tweepy
import time 

auth = tweepy.OAuthHandler #removed for safeguarding
auth.set_access_token #removed for safeguarding

api = tweepy.API(auth, wait_on_rate_limit=True)


# user = api.get_user(screen_name='elainelokeee')
# userID = user.id 


# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#     print(friend.screen_name)

search = '#insert search keywords here'
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
