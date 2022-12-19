
from numpy import char
import praw
import login_credentials

def login():
    r = praw.Reddit(username = login_credentials.username,
                password = login_credentials.password,
                client_id = login_credentials.client_id,
                client_secret = login_credentials.client_key,
                user_agent = "test")
    print("Logged in!")
    return r

def start_bot(r, replied):
    for test in r.subreddit("myBotTests").comments(limit = 100):
        if (search=="joke" or search=="jokes" or search == "funny") and search in test.body and test.id not in replied and test.author != r.user.me():
            print(test.id)
            replied.append(test.id)
            test.reply("Here's a joke:\n  >I have a joke about time travel, but I'm not gonna share it. You guys didn't like it.")
        elif (search=="inspiration" or search=="motivation") and search in test.body and test.id not in replied and test.author != r.user.me():
            print(test.id)
            replied.append(test.id)
            test.reply("Hope this quote motivates you:\n  >“Don't settle for average. Bring your best to the moment. Then, whether it fails or succeeds, at least you know you gave all you had.”\n\t—Angela Bassett ")
        elif search in test.body and test.id not in replied and test.author != r.user.me(): 
            print(test.id)
            replied.append(test.id)
            test.reply( search+" is the best thing on this planet. [Here](https://unsplash.com/s/photos/"+search+") are a few images of "+search+".")

            
r = login()
search = input("What are you looking for?")
replied = []
while True:
    start_bot(r, replied)
