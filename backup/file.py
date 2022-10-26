import json
import os


# ディレクトリの存在を確認
# true:
#    存在します
# false:
#    存在しません
def funCheckDir(dir: str):
    return os.path.isdir(dir)


# ディレクトリを作成
def funCreateDir(dir: str):
    if not os.path.exists(dir):
        os.makedirs(dir)


# 書き込み
def funWriteFile(data, setFile: str):

    fileArr = setFile.split('/')

    for index in range(len(fileArr)):
        if (index == len(fileArr) - 1):
            break

        funCreateDir('/'.join(fileArr[:index + 1]))

    with open(setFile, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)
    return 'ok'
