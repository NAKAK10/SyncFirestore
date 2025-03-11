import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.collection import CollectionReference

from typing import Literal

# cred = credentials.Certificate("./getFirestore/getConfig.json")
cred = credentials.Certificate("./getFirestore/BBB.json")
firebase_admin.initialize_app(cred)
db = firestore.client()  # firestore接続


# 情報を取得
def funGetFirestore(collection, is_have_id=False) -> list[dict]:
    collectionRef: Literal[None, CollectionReference] = None

    data = collection.split('/')
    for i in range(len(data)):
        if data[i] == '':
            continue
        if collectionRef is None:
            collectionRef = db.collection(data[i])
        elif isinstance(collectionRef, CollectionReference):
            collectionRef = collectionRef.document(data[i])
        else:
            collectionRef = collectionRef.collection(data[i])

    d = {} if is_have_id else []

    if isinstance(collectionRef, CollectionReference):
        docs = collectionRef.get()
        for doc in docs:
            if is_have_id:
                d[doc.id] = doc.to_dict()
            else:
                d.append(doc.to_dict())
    elif collectionRef is not None:
        doc = collectionRef.get()
        if is_have_id:
            d[doc.id] = doc.to_dict()
        else:
            d.append(doc.to_dict())

    return d
