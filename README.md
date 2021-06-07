# try_sentencepiece
sentencepieceとmecabによるtweetの比較

```python

# 自身のtweetを取得、twitter APIの設定と環境変数の指定が必要
python get_my_tweet.py

# sentencepieceの学習
python train_sentencepiece.py

# 分かち書きの実施、単語頻度の画像の生成
### 引数1 分かち書きの方法：mecab or sp
### 引数2 単語頻度を算出する際に、指定した長さを超える単語のみを確認：int

### 例
### mecabでの分かち書き、単語の長さは0以上（=指定なし）
python main.py mecab 0

### sentencepieceでの分かち書き、単語の長さは2以上
python main.py sp 2