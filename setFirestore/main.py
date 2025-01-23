import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.collection import CollectionReference

from typing import Literal

cred = credentials.Certificate("./setFirestore/AAA.json")

appsetFirestore = firebase_admin.initialize_app(cred, name='setFirestore')
db = firestore.client(appsetFirestore)  # firestore接続


# 情報を取得
def funSetFirestore(collection: str, docs):
    """
    cocumentを入力された場合は、collectionに変換する
    """
    collectionRef: Literal[None, CollectionReference] = None
    prevCollectionRef: Literal[None, CollectionReference] = None

    data = collection.split('/')

    for n in range(len(data)):
        if data[n] == '':
            continue
        prevCollectionRef = collectionRef
        if collectionRef is None:
            collectionRef = db.collection(data[n])
        elif isinstance(collectionRef, CollectionReference):
            collectionRef = collectionRef.document(data[n])
        else:
            collectionRef = collectionRef.collection(data[n])

    if isinstance(prevCollectionRef, CollectionReference):
        collectionRef = prevCollectionRef

    for doc in docs:
        collectionRef.document(doc['id']).set(doc)
        print(f'登録→{doc["id"]}')
