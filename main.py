import sys
import collections

import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

from sklearn.feature_extraction.text import CountVectorizer

from tokenize_module import tokenize_sp
from tokenize_module import tokenize_mecab


def is_len_over_n(input_text: str, n: int) -> bool:
    return True if len(input_text) > n else False


if __name__ == "__main__":

    # 引数を受け取る
    tokenizer = sys.argv[1]
    word_len = int(sys.argv[2])

    # tweetの読み込み
    with open('all_tweet.txt', 'r') as f:
        # 一つのstrとして読み込み
        all_tweet = f.read()

    # 分かち書き
    if tokenizer == 'sp':
        tokenized_all_tweet = tokenize_sp(
            input_text=all_tweet, model_path="sentencepiece.model")
    elif tokenizer == 'mecab':
        tokenized_all_tweet = tokenize_mecab(input_text=all_tweet)
    else:
        raise ValueError(f"No tokenizer {tokenizer}")

    # 長さがword_len以下のテキストは削除
    tokenized_tweet = [
        txt for txt in tokenized_all_tweet if is_len_over_n(txt, word_len)]

    # 数の集計
    collect = collections.Counter(tokenized_tweet)

    # 描画用のDataFrameを生成
    collect_df = pd.DataFrame(
        {
            'vocab': dict(collect).keys(),
            'cnt': dict(collect).values()
        }
    )

    collect_df = collect_df.sort_values('cnt', ascending=False)

    # 文字の大きさを変更
    plt.rcParams["font.size"] = 14

    # top20を棒グラフで描画
    plt.barh(collect_df['vocab'][:20], collect_df['cnt'][:20])
    plt.xlabel('count')
    plt.ylabel('vocab')
    plt.title(f'My tweet top20 vocab by {tokenizer}, len>{word_len}')
    plt.gca().invert_yaxis()

    # 文字の位置の調整
    plt.tight_layout()

    # 画像の保存
    save_path = f'image/result_{tokenizer}_len_over{word_len}.png'
    print(f'output {save_path}')
    plt.savefig(save_path)
