import tweepy

auth = tweepy.OAuth1UserHandler(
   "R3CXjoaNJVGBpgLDCMAt5C4xa", "tTvTCzq9iOJmBDkLt6xnIinGBJztyNxOiYmL8PscZnYaGirDHJ", "767751198552186880-KDUM8fcsfZ9cdoUv1T03YBZr8O0V9dS", "Z1PtKE2QStAwDURqqpKXFAEd6vXxaVxwoFjTt3idYWm7Z"
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)