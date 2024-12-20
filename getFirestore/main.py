import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# cred = credentials.Certificate("./getFirestore/getConfig.json")
cred = credentials.Certificate("./getFirestore/AAA.json")
firebase_admin.initialize_app(cred)
db = firestore.client()  # firestore接続


# 情報を取得
def funGetFirestore(collection, is_have_id=False):
    docs = db.collection(collection).get()
    d = {} if is_have_id else []
    for doc in docs:
        if is_have_id:
            d[doc.id] = doc.to_dict()
        else:
            d.append(doc.to_dict())
    return d
