import tweepy
import openai

# Twitter API認証情報
API_KEY = "zsbLZ4etWifwmQKT4spK3Rfjq"
API_SECRET = "Dqj5kAW4qgEjWcHG8HZg3d4KA5aqLEgPYPQb9w3oEDgW1XEf7C"
ACCESS_TOKEN = "1915735394819428352-P4rQxI4FUcR8Havt4Wovea6JATwhex"
ACCESS_

openai.api_key = "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"

# 認証
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN,
                                ACCESS_SECRET)
api = tweepy.API(auth)


# 翻訳する関数
def translate_to_japanese(text):
    try:
        print("翻訳リクエスト送信中...")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "system",
                "content": "あなたは優秀な日本語翻訳者です。自然で面白く翻訳してください。"
            }, {
                "role": "user",
                "content": f"以下の英語ツイートを日本語に翻訳してください：\n{text}"
            }])
        print("翻訳成功！")
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print("翻訳エラー:", e)
        return None


# テスト用投稿
original_text = "This cat completely lost its mind 😂"
original_url = "https://twitter.com/TheFigen_/status/1779880272713456091"

# 処理本体
translated = translate_to_japanese(original_text)

if translated:
    tweet = f"{translated}\n\n🔁元ツイート：{original_url}"
    try:
        api.update_status(status=tweet)
        print("投稿完了！")
    except Exception as e:
        print("ツイートエラー:", e)
else:
    print("翻訳できなかったので投稿しませんでした。")
