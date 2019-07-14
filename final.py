import tweepy
from keys import keys
# Basic template for sending a twitter DM in python


# This is where you put the keys generated from twitter, for this code it was placed in a separate file with
# a corresponding dictionary
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys["access_token_secret"]

# Authentication of the keys
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# This functions uses the api.get_user to find the screen-name's unique ID to send a message
# You will need to input the users screen name that can be found on the twitter website with the @
def recipient():
    x = input("Enter in the screen-name you would like to direct message: ")
    tweeter = api.get_user(x)
    print(type(tweeter.id_str))
    return tweeter.id_str


def msg():
    x = input("What message would you like to send? ")
    return x


def event(x, y):
    event = {
        "event": {
            "type": "message_create",
            "message_create": {
                "target": {
                    "recipient_id": x
                },
                "message_data": {
                    "text": y
                }
            }
        }
    }
    return event


def main():
    who = recipient()
    what = msg()
    api.send_direct_message_new(event(who, what))
    print("Your message has been sent!")


main()

