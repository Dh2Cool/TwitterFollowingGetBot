# import the module
import tweepy
import pandas as pd
# assign the values accordingly
consumer_key = "otGx8bQYhUQi7md46ZTgoP4sl"
consumer_secret = "OAzkurTIwQhPFoGDdtVKxU8JvTg8Bw17iGp3NvSFyu4OeOjr99"
access_token = "767751198552186880-si284W5JFiBZsOpfgp1hGHFPlONK6Hy"
access_token_secret = "6YcnoPsuiW7blPR3pynU3nVFK9KSgX07HyBK7SZ9USQQ6"

# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

# screen name of the user
#screen_name = "elonmusk"

# getting the followers list
followers = api.get_friend_ids(screen_name='carnaugh1893',stringify_ids='true')

foll_lup = api.lookup_users(user_id=followers)
users = []
for user in foll_lup:
	users.append(user.screen_name)

col1 = "Followers:"
data = pd.DataFrame({col1:users})
data.to_excel('tweepytrial.xlsx', sheet_name='sheet1',index =False)

retrieved_list = pd.read_excel('./tweepytrial.xlsx')
users_old = retrieved_list["Followers:"].tolist()
print(users_old)

