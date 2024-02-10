from atproto import Client
import os
from openai import completion


def main():
    client = Client(base_url='https://bsky.social')
    client.login(os.environ['MAIL'], os.environ['PASS'])

    content = completion()
    print(content)
    post = content[1:len(content) - 1] + " <bot with gpt-3.5-turbo>"
    post_result = client.send_post(post)
    print(post_result)


if __name__ == "__main__":
    main()
