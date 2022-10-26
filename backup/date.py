import datetime


# 日付を形成する
# YYYY/MM/DD hh:mm:ss
def funDateFormat(d: datetime = datetime.datetime.now(), formatstr: str = 'YYYYMMDD'):

    def set(subDateFormat):
        return ('0' + str(subDateFormat))[-2:]

    if (isinstance(d, str)):
        return ''

    if (isinstance(d, datetime.datetime)):  # datetimeの場合
        formatstr = formatstr.replace('YYYY', str(d.year))
        formatstr = formatstr.replace('MM', set(d.month))
        formatstr = formatstr.replace('DD', set(d.day))
        formatstr = formatstr.replace('hh', set(d.hour))
        formatstr = formatstr.replace('mm', set(d.minute))
        formatstr = formatstr.replace('ss', set(d.second))

    else:  # Timestampの場合
        formatstr = formatstr.replace('YYYY', d.strftime('%Y'))
        formatstr = formatstr.replace('MM', d.strftime('%m'))
        formatstr = formatstr.replace('DD', d.strftime('%d'))
        formatstr = formatstr.replace('hh', d.strftime('%H'))
        formatstr = formatstr.replace('mm', d.strftime('%M'))
        formatstr = formatstr.replace('ss', d.strftime('%S'))

    return formatstr
