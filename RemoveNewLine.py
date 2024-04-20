"""
指定したテキストから改行を削除するプログラム
"""

# 改行を削除したいテキストが書かれたファイルを開く
with open("read.txt","r",encoding="utf-8") as readFile:
    text = list(readFile.read())
    # 改行があったら改行を削除する
    # result = [word for word in text if word!="\n"]  # 改行を削除する
    result = [" " if word == "\n" else word for word in text]   # 改行を空白に置き換える(英語用)
    # result = [word for word in text if word!="\n" and word!=" "]    # 改行と空白を削除する(日本語用)
    result = "".join(result)

# 結果書き込み用ファイルを開く
with open("write.txt","w",encoding="utf-8") as writeFile:
# with open("write.txt","w") as writeFile:
    # 結果を書き込む
    writeFile.write(result)
    # 結果を表示する
    print(result)
    print()
