import MeCab
import sentencepiece as spm


def tokenize_mecab(input_text: str) -> list:
    '''mecabによる分かち書き'''
    # 分かち書きの単語のみを返す設定にする
    mecab = MeCab.Tagger('-Owakati')
    # 分かち書きの実施
    tokenize_list = mecab.parse(input_text).split()
    return tokenize_list


def tokenize_sp(input_text: str, model_path: str) -> list:
    '''SentencePieceによる分かち書き'''
    # モデルの読み込み
    sp = spm.SentencePieceProcessor()
    sp.Load(model_path)

    # sentencepieceによる分かち書き
    tokenize_list = sp.EncodeAsPieces(input_text)

    # 必ず最初に'▁'が入るため削除
    tokenize_list = [token.replace(
        '▁', '') for token in tokenize_list if token.replace('▁', '') != ""]

    return tokenize_list
