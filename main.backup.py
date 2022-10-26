import datetime
from backup.file import funWriteFile
from backup.date import funDateFormat
from getFirestore.main import funGetFirestore


backupCollection = ['AAAA']


for collentionName in backupCollection:
    getCollettion = funGetFirestore(collentionName)
    fileName = 'backupDate/' + funDateFormat(datetime.datetime.now(), 'YYYY年MM月DD日/') + collentionName + '.json'
    print(fileName)
    funWriteFile(getCollettion, fileName)


print('完了')
