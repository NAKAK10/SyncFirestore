import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./getFirestore/getConfig.json")
firebase_admin.initialize_app(cred)
db = firestore.client()  # firestore接続


# 情報を取得
def funGetFirestore(collection):
    docs = db.collection(collection).get()
    d = []
    for doc in docs:
        d.append(doc.to_dict())
    if d == []:
        return []
    return d
