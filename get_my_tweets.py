import os
import pickle
import re

import pandas as pd

import tweepy
import texthero as hero

def remove_digits(input_text: str) -> str:
    return re.sub(r"\d+","", input_text)

def preprocess(input_text):
    """前処理"""
    text = hero.clean(input_text, pipeline=[
        hero.preprocessing.fillna,
        hero.preprocessing.lowercase,
        hero.preprocessing.remove_urls,
        hero.preprocessing.remove_whitespace
        # hero.preprocessing.remove_brackets
        ])

    # Tweet内の数字を削除
    clean_text = text.apply(remove_digits)

    return clean_text

def preprocess_for_tweet(input_text: str):
    """前処理"""
    # Tweet内の改行コードの削除
    input_text = input_text.replace('\n','')
    # ハッシュタグ削除
    input_text = re.sub(r'#.*', "", input_text)
    return input_text

def get_my_tweets() -> list:
    """TwitterAPIを用いて自身のTweet全件を取得する"""
    env = os.environ

    # 認証に必要なキーとトークン
    API_KEY = env['TWITTER_API_KEY']
    API_SECRET = env['TWITTER_API_SECRET_KEY']
    ACCESS_TOKEN = env['TWITTER_ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = env['TWITTER_ACCESS_TOKEN_SECRET']

    # APIの認証
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # キーワードからツイートを取得
    # countの最大値は200, pageをずらすことで全件を取得する。
    max_cnt = 200
    all_tweet_num = api.user_timeline(count=1)[0]._json['user']['statuses_count']
    page_num = (all_tweet_num // max_cnt) + 1

    # debug
    # max_cnt = 30
    # page_num = 1

    all_tweet = []

    for page in range(page_num):
        tweets = api.user_timeline(count=200, page=page, exclude_replies=True, include_rts=False)
        tweets_list = [tweet.text for tweet in tweets]
        all_tweet.extend(tweets_list)

    return all_tweet

if __name__ == "__main__":

    # Tweetの取得
    all_tweet = get_my_tweets()

    # Tweet用の前処理
    all_tweet = [preprocess_for_tweet(tweet) for tweet in all_tweet]
    # テキストの前処理
    all_tweet_sr = preprocess(pd.Series(all_tweet))
    
    # 空白以外の要素をlistに変換する
    all_tweet = [tweet for tweet in all_tweet_sr if tweet != ""]

    # リストの保存
    with open('all_tweet.txt', 'w') as f:
        # 1tweet1行にするため、要素毎に改行を追加する。
        f.write('\n'.join(all_tweet))