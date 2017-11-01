import time
import tweepy
import csv
import numpy

# Variables that contains the user credentials to access Twitter API

access_token = "974217668-Dishu2YGNKL0ojsyZhdz2HLzqgVE3yIGFWCm40pt"
access_token_secret = "zC4FccmKS1u7GRfs1S7bisWgWLXcxMeKY87ZN01T0mAbS"
consumer_key = "jk2HV3gzk62PvJbfzdNvJgBD8"
consumer_secret = "7HTz9u2LqlEXBNKToaafO552vmKnX956Z0Odh8UoT9HJ1zV4R0"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
ids = []

# text file to save verified user ID's
verified_user_ids = open("verifiedUserIDs.csv", "w")
writer = csv.writer(verified_user_ids)


for page in tweepy.Cursor(api.followers_ids, screen_name="verified").pages():
    print(page)
    for id in page:
        writer.writerow([id])
    ids.extend(page)
    if len(ids) > 200000:
        break
    time.sleep(60)


id_chunks = numpy.array_split(ids, 100)
print(id_chunks)
verified_screen_names = open("userData.csv", "w")
user_data_writer = csv.writer(verified_screen_names)
header = ["id", "username", "screen_name", "location", "url", "description", "followers", "following",
          "favorite_count", "tweet_count", "created_at", "time_zone", "geo_enabled", "language",
          "profile_image_url", "default_profile", "default_profile_image"]

user_data_writer.writerow(header)

# lookup users is limited to 100 per request so this has to be chopped up and sent 100 at a time
sliced_ids = [ids[x:x+100] for x in range(0, len(ids), 100)]
print(sliced_ids)

for id_slice in sliced_ids:
    user_slice = api.lookup_users(user_ids=id_slice)
    for user in user_slice:
        # Twitter User Model https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object
        userData = [user.id_str, user.name, user.screen_name, user.location,
                    user.url, user.description, user.followers_count, user.friends_count,
                    user.favourites_count, user.statuses_count, user.created_at, user.time_zone,
                    user.geo_enabled, user.lang, user.profile_image_url, user.default_profile,
                    user.default_profile_image]
        user_data_writer.writerow(userData)



# screen_names = [user.screen_name for user in api.lookup_users(user_ids=ids)]

# for name in screen_names:
#     screen_name_writer.writerow([name])

print("Done")
# END
