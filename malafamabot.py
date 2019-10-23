import tweepy
import time
from timeloop import Timeloop
from datetime import timedelta
import glob
import random
import os

#autenthication information
api_key = "yZ7kIih32AaevYeYQXJCAJkKM"
api_secret = "V6xmvCj1DShPNX2UJwYNKZph8o2euT2sFyWb5J8nnqY40YoGlb"
oauth_token = "1186104614124445696-XGgv5TanFbtAjUGgQPlJgACvJOfRdm" # Access Token
oauth_token_secret = "wraKJnhh9twuSqjup1iwfSUQMxWhB91wP7u3yxm7giYJr" # Access Token Secret

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(oauth_token, oauth_token_secret)
api = tweepy.API(auth)

t1 = Timeloop()
images = glob.glob("./images/" + "*")

def first_post():
    images_aux = glob.glob("./images/" + "*")
    image_open = images_aux[random.randint(0,len(images_aux)-1)]
    api.update_with_media(image_open)
    print( "Image posted at : %s, %s" % (time.ctime(), image_open))

@t1.job(interval=timedelta(hours=12))
def sample_job_every_1m():
    image_idx = random.randint(0,len(images)-1)
    image_open = images[image_idx]
    api.update_with_media(image_open)
    del images[image_idx]
    if len(images) == 1:
        images = glob.glob("./images/" + "*")
    print( "Image posted at : %s, %s" % (time.ctime(), image_open))

if __name__ == "__main__":
    first_post()
    t1.start(block=True)
#api.update_with_media("./images/pepe.jpg")
