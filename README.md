# try_sentencepiece
sentencepieceとmecabによるtweetの比較

```python

# 自身のtweetを取得、twitter APIの設定と環境変数の指定が必要
python get_my_tweet.py

```

```python

# sentencepieceの学習
python train_sentencepiece.py

```

```python

# 特定の文章のtoken化
python tokenize_test.py {分かち書きの方法} {文章}

### 例
### mecabでの分かち書き
python tokenize_test.py mecab '平和な部屋の中で雨が降っているのをぼーっと眺めることが大好きです'

### sentencepieceでの分かち書き
python tokenize_test.py sp '平和な部屋の中で雨が降っているのをぼーっと眺めることが大好きです'

```

```python

# 分かち書きの実施、単語頻度の画像の生成
python main.py {分かち書きの方法} {単語の長さ}

### 例
### mecabでの分かち書き、単語の長さは0より上（=指定なし）
python main.py mecab 0

### sentencepieceでの分かち書き、単語の長さは2より上
python main.py sp 2

```