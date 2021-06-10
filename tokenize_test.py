import sys

import pandas as pd

from get_my_tweets import preprocess
from get_my_tweets import preprocess_for_tweet

from tokenize_module import tokenize_sp
from tokenize_module import tokenize_mecab

if __name__ == "__main__":
    
    # 引数を受け取る
    tokenizer = sys.argv[1]
    input_text = sys.argv[2]

    # 学習時と同様の前処理
    input_text = preprocess_for_tweet(input_text)
    input_text = str(preprocess(pd.Series(input_text))[0])

    # 分かち書き
    if tokenizer == 'sp':
        tokenized_text = tokenize_sp(input_text=input_text, model_path="sentencepiece.model")
    elif tokenizer == 'mecab':
        tokenized_text = tokenize_mecab(input_text=input_text)
    else:
        raise ValueError(f"No tokenizer {tokenizer}")

    print(tokenized_text)