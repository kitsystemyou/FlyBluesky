from atproto import Client
import os
import time

client = Client(base_url='https://bsky.social')
client.login(os.environ['MAIL'],
             os.environ['PASS'])

nowtime = time.strftime('%Y-%M-%D %H:%M:%S', time.localtime(time.time()))
post: str = "now! " + nowtime
print("post: ", post)
post = client.send_post(post)
