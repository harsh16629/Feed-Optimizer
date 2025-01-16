import requests
from googleapiclient.discovery import build
import tweepy
import os

# 1. Instagram Graph API
class InstagramAPI:
    def __init__(self, access_token):
        self.base_url = "https://graph.facebook.com/v16.0"
        self.access_token = access_token

    def search_hashtag(self, query):
        # Search for a hashtag ID
        url = f"{self.base_url}/ig_hashtag_search?q={query}&access_token={self.access_token}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("data", [])
        else:
            print(f"Instagram search error: {response.json()}")
            return []

    def get_top_posts(self, hashtag_id):
        # Get top posts for a hashtag
        url = f"{self.base_url}/{hashtag_id}/top_media?fields=id,caption&access_token={self.access_token}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("data", [])
        else:
            print(f"Instagram posts error: {response.json()}")
            return []

    def like_post(self, post_id):
        # Like a post
        url = f"{self.base_url}/{post_id}/likes?access_token={self.access_token}"
        response = requests.post(url)
        return response.status_code == 200

    def comment_post(self, post_id, comment):
        # Comment on a post
        url = f"{self.base_url}/{post_id}/comments"
        data = {"message": comment, "access_token": self.access_token}
        response = requests.post(url, data=data)
        return response.status_code == 200

# 2. YouTube Data API
class YouTubeAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.service = build("youtube", "v3", developerKey=self.api_key)

    def search_videos(self, query):
        request = self.service.search().list(
            q=query,
            part="snippet",
            type="video",
            maxResults=10
        )
        response = request.execute()
        return response.get("items", [])

    def like_video(self, video_id):
        # Liking a video requires OAuth credentials
        print(f"Like video: https://www.youtube.com/watch?v={video_id}")

    def comment_video(self, video_id, comment):
        # Commenting on a video
        print(f"Comment on video: https://www.youtube.com/watch?v={video_id} - Comment: {comment}")

# 3. Twitter API v2
class TwitterAPI:
    def __init__(self, bearer_token, api_key, api_key_secret, access_token, access_token_secret):
        self.client = tweepy.Client(bearer_token=bearer_token)
        self.auth_client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_key_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )

    def search_tweets(self, query):
        tweets = self.client.search_recent_tweets(query=query, max_results=10)
        return tweets.data if tweets else []

    def like_tweet(self, tweet_id):
        self.auth_client.like(tweet_id)
        print(f"Liked tweet ID: {tweet_id}")

    def comment_tweet(self, tweet_id, comment):
        self.auth_client.create_tweet(text=comment, in_reply_to_tweet_id=tweet_id)
        print(f"Commented on tweet ID: {tweet_id}")

    def follow_user(self, user_id):
        self.auth_client.follow_user(user_id)
        print(f"Followed user ID: {user_id}")


if __name__ == "__main__":
    query = "example_topic"

    # Instagram
    print("\n--- Instagram ---")
    instagram_token = os.getenv("IG_API_KEY")
    instagram_api = InstagramAPI(instagram_token)
    hashtags = instagram_api.search_hashtag(query)
    if hashtags:
        top_posts = instagram_api.get_top_posts(hashtags[0]["id"])
        for post in top_posts[:10]:
            instagram_api.like_post(post["id"])
            instagram_api.comment_post(post["id"], "Great post!")

    # YouTube
    print("\n--- YouTube ---")
    youtube_api_key = os.getenv("YT_API_KEY")
    youtube_api = YouTubeAPI(youtube_api_key)
    videos = youtube_api.search_videos(query)
    for video in videos:
        youtube_api.like_video(video["id"]["videoId"])
        youtube_api.comment_video(video["id"]["videoId"], "Awesome video!")

    # Twitter
    print("\n--- Twitter ---")
    twitter_bearer_token = os.getenv("TW_BEARER_TOKEN")
    twitter_api_key = os.getenv("TW_API_KEY")
    twitter_api_secret = os.getenv("TW_API_SECRET")
    twitter_access_token = os.getenv("TW_ACCESS_TOKEN")
    twitter_access_token_secret = os.getenv("TW_ACCESS_TOKEN_SECRET")
    twitter_api = TwitterAPI(twitter_bearer_token, twitter_api_key, twitter_api_secret, twitter_access_token, twitter_access_token_secret)
    tweets = twitter_api.search_tweets(query)
    for tweet in tweets[:10]:
        twitter_api.like_tweet(tweet.id)
        twitter_api.comment_tweet(tweet.id, "Interesting tweet!")
        twitter_api.follow_user(tweet.author_id)
