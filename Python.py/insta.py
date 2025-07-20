from instabot import Bot
import time

def unfollow_non_followers(bot):
    # Get your followers and following lists
    followers = bot.get_user_followers(bot.user_id)
    following = bot.get_user_following(bot.user_id)

    # Identify non-followers
    non_followers = list(set(following) - set(followers))

    # Unfollow non-followers
    for user_id in non_followers:
        bot.unfollow(user_id)
        print(f"Unfollowed user: {user_id}")
        time.sleep(360)  # Add a delay to avoid rate limiting

# Create an instance of the Bot class
bot = Bot()

# Login to your Instagram account
username = "aviraj_virape35"
password = "UNIin@ppp5"
bot.login(username=username, password=password)

# Call the unfollow_non_followers function
unfollow_non_followers(bot)

# Logout after performing the actions
bot.logout()
