# Social Media Automation Script

This Python script uses the official APIs of Instagram, YouTube, and Twitter to automate the following tasks legally and ethically:

1. **Search** for a user-provided query on the respective platforms.
2. **Like** and **comment** on the top 10 results.
3. **Follow** the accounts associated with the top results (where applicable).

## Prerequisites

### API Access
You need API credentials for the following platforms:
- **Instagram**: Obtain access tokens via the [Meta for Developers](https://developers.facebook.com/).
- **YouTube**: Get an API key from the [Google Cloud Console](https://console.cloud.google.com/).
- **Twitter**: Set up an app at the [Twitter Developer Platform](https://developer.twitter.com/) to obtain API keys and access tokens.

### Python Dependencies
Install the required libraries:
```bash
pip install requests google-api-python-client tweepy python-dotenv
```

### Environment Variables
Create a `.env` file in the project directory to securely store your API credentials:

```env
# Instagram
INSTAGRAM_ACCESS_TOKEN=your_instagram_token

# YouTube
YOUTUBE_API_KEY=your_youtube_api_key

# Twitter
TWITTER_BEARER_TOKEN=your_twitter_bearer_token
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_SECRET=your_twitter_access_secret
```

Make sure to include the `.env` file in your `.gitignore` to prevent it from being uploaded to GitHub.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/social-media-automation.git
   cd social-media-automation
   ```

2. Set up your environment variables in the `.env` file.

3. Run the script:
   ```bash
   python main.py
   ```

4. Enter your search query when prompted. The script will:
   - Search for the query on Instagram, YouTube, and Twitter.
   - Like and comment on the top 10 results.
   - Follow the creators or accounts associated with the results (if applicable).

## API Integration

### Instagram API
- Searches for hashtags related to the query.
- Likes and comments on top posts.

### YouTube Data API
- Retrieves videos matching the query.
- Simulates liking and commenting (requires OAuth for real interactions).

### Twitter API
- Searches for recent tweets matching the query.
- Likes, comments, and follows the authors of the tweets.

## Notes

- **Rate Limits**: Ensure your usage complies with the rate limits imposed by each platform.
- **Permissions**: Verify that your API keys and tokens have the necessary permissions for actions like liking, commenting, and following.
- **Ethical Use**: Use this script responsibly and ensure it aligns with the terms of service of each platform.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
