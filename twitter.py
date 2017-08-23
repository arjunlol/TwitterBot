import tweepy

consumer_key = 'POsewQPQ002zo4VOwAe9mMcD9'
consumer_secret = 'SeOcAFedIfgtj97zTO1ylVjMjOPIpV12GhTLq9NK4gfFephG1Q'
access_key = '899879013749010432-5HnKcG2Q0QbhUPsGgfjEld5SVuxmMoX'
access_secret = 'eeM1RwjRj86OAc1HhjP5vjAXWgnQWhjPNVzrm6ylmcZ8I'

def authorize_account(consumer_key = consumer_key, consumer_secret = consumer_secret,
                      access_key = access_key, access_secret = access_secret):
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  return tweepy.API(auth)

def read_messages(twitter_account, since = 0):
  mentions = tweepy.Cursor(twitter_account.mentions_timeline, since_id = str(since)).items()
  tweets = []

  for tweet in tweets:
    tweets.append(tweet.text)
    if (tweet.id > since):
      since = tweet.id

  return {"messages": tweets, "since_id": since}

if __name__ == "__main__":

    twitter_account = authorize_account()
    since = 1

    while(True):
        #read all mentions since we last checked
        tweets = read_messages(twitter_account, since)
        since = tweets['since_id']

        #iterate through messages, updating status
        for message in tweets['messages']:
            twitter_account.update_status(message[::-1])

        #sleep 15 minutes and check again
        time.sleep(60 * 15)