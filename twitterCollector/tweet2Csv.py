#!/usr/bin/python
import tweepy
import csv #Import csv

#Twitter API credentials
consumer_key = "1A7AejBl1wC1qOYUZMXPTnILV"
consumer_secret = "AAGiSYwlMjuQfIGml294n16XOqonully88cO8lKmtRMDEOG5UR"
access_key = "150794348-XwK0DEgeWmDCCNk7JYBGKDaSVw3wjCbKzz2pMNek"
access_secret = "wTLu7c0kSriOlBIyz7ZZ7vvfQfTmJtlsjVj3l2Sp80OnD"

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# Open/create a file to append data to
csvFile = open('lateTweets.csv', 'a', newline='', encoding='utf-8')

#Use csv writer
csvWriter = csv.writer(csvFile)
# csvWriter.writerow(['TweetCreatedDate', 'TweetId', 'TweetIdStr', 'TweetText', 'TweetTruncated',
#                             'InReplyToSatusId', 'InReplyToSatusIdStr', 'InReplyToUserId',
#                             'InReplyToUserIdStr', 'InReplyToScreenName', 'TweetSource', 'UserId',
#                             'UserIdStr', 'UserName', 'UserScreenName', 'UserLocation',
#                             'UserUrl', 'UserDescription', 'UserVerified', 'UserFollowersCount',
#                             'UserFriendsCount', 'UserListedCount', 'UserFavouriteCount',
#                             'UserStatusesCount', 'UserCreatedAt', 'UTC_OFFSET', 'UserTimeZone',
#                             'Geo_enabled', 'ProfileImageUrl', 'tweetCoordinates', 'Country', 'ISO', 'Country_Full',
#                             'PlaceId', 'PlaceName', 'PlaceType', 'PlaceUrl'])
for tweet in tweepy.Cursor(api.search, q='#LateLateToyShow', since="2018-12-01", until="2018-12-07", lang="en").items():
    # Write a row to the CSV file. I use encode UTF-8
    if tweet.place is None:
        csvWriter.writerow([tweet.created_at, tweet.id, tweet.id_str, tweet.text, tweet.truncated,
                            tweet.in_reply_to_status_id, tweet.in_reply_to_status_id_str, tweet.in_reply_to_user_id,
                            tweet.in_reply_to_user_id_str, tweet.in_reply_to_screen_name, tweet.source, tweet.user.id,
                            tweet.user.id_str, tweet.user.name, tweet.user.screen_name, tweet.user.location,
                            tweet.user.url, tweet.user.description, tweet.user.verified, tweet.user.followers_count,
                            tweet.user.friends_count, tweet.user.listed_count, tweet.user.favourites_count,
                            tweet.user.statuses_count, tweet.user.created_at, tweet.user.utc_offset, tweet.user.time_zone,
                            tweet.user.geo_enabled, tweet.user.profile_image_url_https, tweet.coordinates])
    else:
        csvWriter.writerow([tweet.created_at, tweet.id, tweet.id_str, tweet.text, tweet.truncated,
                            tweet.in_reply_to_status_id, tweet.in_reply_to_status_id_str, tweet.in_reply_to_user_id,
                            tweet.in_reply_to_user_id_str, tweet.in_reply_to_screen_name, tweet.source, tweet.user.id,
                            tweet.user.id_str, tweet.user.name, tweet.user.screen_name, tweet.user.location,
                            tweet.user.url, tweet.user.description, tweet.user.verified, tweet.user.followers_count,
                            tweet.user.friends_count, tweet.user.listed_count, tweet.user.favourites_count,
                            tweet.user.statuses_count, tweet.user.created_at, tweet.user.utc_offset, tweet.user.time_zone,
                            tweet.user.geo_enabled, tweet.user.profile_image_url_https, tweet.coordinates,
                            tweet.place.country, tweet.place.country_code, tweet.place.full_name,
                            tweet.place.id, tweet.place.name, tweet.place.place_type, tweet.place.url])
    print(tweet.created_at, tweet.text, tweet.user.screen_name)
csvFile.close()

