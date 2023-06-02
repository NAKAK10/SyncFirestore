"""
バックアップのみを行う
"""

import datetime
from backup.file import funWriteFile
from backup.date import funDateFormat
from getFirestore.main import funGetFirestore

"""
if is_have_id is True, funGetFirestore return dict
if is_have_id is False, funGetFirestore return list
"""
is_have_id = True

backupCollection = ['AAAA']

for collentionName in backupCollection:
    getCollettion = funGetFirestore(collentionName, is_have_id)
    fileName = 'backupDate/' + funDateFormat(datetime.datetime.now(), 'YYYY年MM月DD日/') + collentionName + '.json'
    print(fileName)
    funWriteFile(getCollettion, fileName)


print('完了')
