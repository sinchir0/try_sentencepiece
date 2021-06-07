import sentencepiece as spm

# モデルの学習
spm.SentencePieceTrainer.Train(
    input='all_tweet.txt',
    model_prefix='sentencepiece',
    vocab_size=2000,
    character_coverage=0.9995
    )