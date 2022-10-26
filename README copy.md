# firestore のバックアップできるよ

- ①json ファイルを作成
  `./getFirestore/getConfig.json`

- ②`main.backup.py` に コレクション名を追加

  ```py
  backupCollection = ['your Collection Name', 'your Collection Name']
  ```

- ③ 実行
  ```bash
  python main.backup.py
  ```

# 2 つの firestore の情報を移せるよ

- ①json ファイルを作成
  `./getFirestore/getConfig.json` -> 情報を取得する firestroe
  `./setFirestore/setConfig.json` -> 情報を登録する firestore

- ②`main.py`に情報を移したいコレクション名を記入

  ```py
  collectionsName = ['your Collection Name', 'your Collection Name']
  ```

- ③ 実行
  ```py
  python main.py
  ```
