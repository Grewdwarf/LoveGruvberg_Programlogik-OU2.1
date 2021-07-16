import datetime

datum = datetime.datetime.now()
date = datum.date()
nutid = date.strftime("%Y")
print('Current Year -> ') + nutid;