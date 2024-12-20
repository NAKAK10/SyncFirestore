import firebase_admin
from firebase_admin import credentials
from firebase_admin.auth import update_user


cred = credentials.Certificate("setFirestore/AAA.json")
firebase_admin.initialize_app(cred)

res = update_user(
    uid='AAAAA',
    password='123456',
)

print(res)
