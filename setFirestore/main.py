import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./setFirestore/setConfig.json")

appsetFirestore = firebase_admin.initialize_app(cred, name='setFirestore')
db = firestore.client(appsetFirestore)  # firestore接続


# 情報を取得
def funSetFirestore(collection, docs):
    collectionRref = db.collection(collection)

    for doc in docs:
        collectionRref.document(doc['id']).set(doc)
        print('登録→' + doc['id'])
