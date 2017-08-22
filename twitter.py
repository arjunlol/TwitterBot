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

if __name__ == '__main__':
  twitter_account = authorize_account()
  twitter_account.update_status('TEST')