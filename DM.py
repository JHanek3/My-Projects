import tweepy
import random
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys["access_token_secret"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)



def picker():
    with open("nice.txt", 'r') as f:
        h = f.readlines()
        x = random.choice(h)
        return x


def replacer(x):
    with open("nice.txt", 'r') as f:
        newText=f.read().replace(x, '')
    with open("nice.txt", 'w') as f:
        f.write(newText)


def rewrite():
    with open("nice_key.txt", 'r') as f:
        with open("nice.txt", 'w') as g:
            for line in f:
                g.write(line)

def event(msg):
    event = {
        "event": {
            "type": "message_create",
            "message_create": {
                "target": {
                    "recipient_id": '##########'  # gf's unique ID that I send to
                },
                "message_data": {
                    "text": msg
                }
            }
        }
    }
    return event


def main():
    count = len(open('nice.txt').readlines()) - 1
    my_statement = picker()
    api.send_direct_message_new(event(my_statement))
    print("You sent: {}You have {} DMs remaining.".format(my_statement, count))
    replacer(my_statement)
    if count <= 0:
        rewrite()
    else:
        pass


main()

