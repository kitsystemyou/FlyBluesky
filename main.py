from atproto import Client
import os
import time
from datetime import datetime
from zoneinfo import ZoneInfo

client = Client(base_url='https://bsky.social')
client.login(os.environ['MAIL'],
             os.environ['PASS'])

tl = time.localtime(time.time())

nowtime = datetime.now(ZoneInfo("Asia/Tokyo")).strftime('%Y-%M-%D %H:%M:%S')
post: str = "now! " + nowtime
print("post: ", post)
post = client.send_post(post)
