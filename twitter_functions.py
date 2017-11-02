import constants
import time
import csv
import tweepy


def get_user_ids(number_of_ids_to_get, get_user_profile = False):
    ids = []

    # text file to save verified user ID's
    verified_user_ids = open("VerifiedUserIDs_Sample.csv", "w")
    writer = csv.writer(verified_user_ids)

    for page in tweepy.Cursor(constants.api.followers_ids, screen_name="verified").pages():
        # print(page)
        for id_number in page:
            writer.writerow([id_number])
        ids.extend(page)
        if len(ids) >= number_of_ids_to_get:
            print(number_of_ids_to_get + " ids acquired")
            break
        time.sleep(60)
        print("Current number of ids " + str(len(ids)))
    # END
    if get_user_profile:
        get_user_profiles(ids)


def get_user_profiles(ids):
    verified_screen_names = open("userData.csv", "w")
    user_data_writer = csv.writer(verified_screen_names)
    header = ["id", "username", "screen_name", "location", "url", "description", "followers", "following",
              "favorite_count", "tweet_count", "created_at", "time_zone", "geo_enabled", "language",
              "profile_image_url", "default_profile", "default_profile_image"]

    user_data_writer.writerow(header)

    # lookup users is limited to 100 per request so this has to be chopped up and sent 100 at a time
    sliced_ids = [ids[x:x + 100] for x in range(0, len(ids), 100)]
    # print(sliced_ids)

    for id_slice in sliced_ids:
        user_slice = constants.api.lookup_users(user_ids=id_slice)
        for user in user_slice:
            # Twitter User Model https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object
            user_data = [user.id_str, user.name, user.screen_name, user.location,
                         user.url, user.description, user.followers_count, user.friends_count,
                         user.favourites_count, user.statuses_count, user.created_at, user.time_zone,
                         user.geo_enabled, user.lang, user.profile_image_url, user.default_profile,
                         user.default_profile_image]
            user_data_writer.writerow(user_data)

    print("Done")
    # END
