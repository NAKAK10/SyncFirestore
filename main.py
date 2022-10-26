from setFirestore.main import funSetFirestore
from getFirestore.main import funGetFirestore


collectionsName = ['Message']


for collentionName in collectionsName:
    print('【' + collentionName + '】' + 'コピー開始')
    getdata = funGetFirestore(collentionName)
    funSetFirestore(collentionName, getdata)
    print('【' + collentionName + '】' + 'コピー完了')


print('終了')
