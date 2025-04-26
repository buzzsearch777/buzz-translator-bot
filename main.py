import tweepy
import openai

# Twitter API認証情報
API_KEY = "zsbLZ4etWifwmQKT4spK3Rfjq"
API_SECRET = "Dqj5kAW4qgEjWcHG8HZg3d4KA5aqLEgPYPQb9w3oEDgW1XEf7C"
ACCESS_TOKEN = "1915735394819428352-P4rQxI4FUcR8Havt4Wovea6JATwhex"
ACCESS_SECRET = "Yn5cFB0hxWoWRZEvY0tqjBFcAmdTfziLOsJ1DD9B8HdnF"

# OpenAI API認証情報
openai.api_key = "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"
openai.organization = "org-rPcV99pmwk39M3t4TTArjtkf"
openai.project = "proj_nJFkdxEwnrfmQxfbB3magVC8"

# Twitter API 認証
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# 翻訳する関数
def translate_to_japanese(text):
    try:
        print("翻訳リクエスト送信中...")
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "あなたは優秀な日本語翻訳者です。自然で面白く翻訳してください。"},
                {"role": "user", "content": f"以下の英語ツイートを日本語に翻訳してください：\n{text}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("翻訳エラー:", e)
        return None

# テスト用のバズ投稿
original_text = "This cat completely lost its mind 😂"
original_url = "https://twitter.com/TheFigen_/status/1779880272713456091"

# 翻訳実行
translated = translate_to_japanese(original_text)

if translated:
    tweet = f"{translated}\n\n🔁元ツイート：{original_url}"
    api.update_status(status=tweet)
    print("投稿完了！")
else:
    print("翻訳できなかったので投稿しませんでした。")
