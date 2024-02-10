import http.client
import os
import json


def completion() -> str:
    url = "https://api.openai.com/v1/chat/completions"
    host = "api.openai.com"
    conn = http.client.HTTPSConnection(host)
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    headers = {"Authorization": f"Bearer {openai_api_key}", "Content-Type": "application/json"}
    body_json = {"model": "gpt-3.5-turbo",
                 "messages": [
                     {"role": "user",
                      "content": "あなたはカモメの化身です。カモメから人間になった青年のようなつぶやきを100文字以内で考えてください。なお、青年は現在プログラマとして働いています。職業に関係する内容を考えるかどうかはあなたの判断に任せます。セリフのように書いて欲しいですが、前後に「」は付けないでください。",
                      }],
                 "temperature": 0.7}
    print(body_json)
    conn.request("POST", url, headers=headers, body=json.dumps(body_json))

    res = conn.getresponse()
    response_body = json.loads(res.read())
    content = response_body['choices'][0]['message']['content']
    return content
